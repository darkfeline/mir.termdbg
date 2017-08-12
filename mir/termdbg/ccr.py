# Copyright (C) 2017 Allen Li
# Copyright (C) 2013 Python Software Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Control code revealer.

Usage: ccr FILE PROG [ARG]...

Run a program with arguments and pretend to be a terminal, teeing output
to a file.

This can be used to debug what control codes a troublesome program is
emitting when it thinks it's talking to a terminal.
"""

import argparse
import os
import pty
from select import select
import sys

_STDIN_FD = 0
_STDOUT_FD = 1


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('argv', nargs=argparse.REMAINDER)
    args = parser.parse_args(args)
    with open(args.file, 'wb') as f:
        return _spawn_with_tty_copy(args.argv, f)


def _read(fd):
    """Default read function."""
    return os.read(fd, 1024)


def _spawn_with_tty_copy(argv, file):
    """Create a process sharing the same tty, but copying output to a file."""
    pid, master_fd = pty.fork()
    if pid == 0:
        os.execlp(argv[0], *argv)
    try:
        _copy(master_fd, file)
    finally:
        os.close(master_fd)
        ret, _pid = os.waitpid(pid, 0)
    return ret


def _copy(master_fd, file):
    """Parent copy loop."""
    fds = [master_fd, _STDIN_FD]
    while True:
        rfds, wfds, xfds = select(fds, [], [])
        if master_fd in rfds:
            data = os.read(master_fd, 1024)
            if not data:  # Reached EOF.
                fds.remove(master_fd)
            else:
                file.write(data)
                os.write(_STDOUT_FD, data)
        if _STDIN_FD in rfds:
            data = os.read(_STDIN_FD, 1024)
            if not data:
                fds.remove(_STDIN_FD)
            else:
                _writen(master_fd, data)


def _writen(fd, data):
    """Write all the data to a descriptor."""
    while data:
        n = os.write(fd, data)
        data = data[n:]


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
