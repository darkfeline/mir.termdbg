# Copyright 2016 Allen Li
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

import contextlib
import os
import sys
import termios
import tty

STDIN = 0


@contextlib.contextmanager
def restore_term_attrs(fd):
    old_attrs = termios.tcgetattr(fd)
    try:
        yield
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old_attrs)


def main():
    with restore_term_attrs(STDIN):
        tty.setraw(0)
        while True:
            _loop_once(STDIN)


def _loop_once(fd):
    char = ord(os.read(0, 1))
    print(
        '{char:d}, o{char:o}, 0x{char:X}'
        .format(char=char), end='\r\n')
    if char == 3:  # ^C
        sys.exit(0)


if __name__ == '__main__':
    main()
