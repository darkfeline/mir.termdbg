# Copyright (C) 2016 Allen Li
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

"""Simple terminal key press debugger.

termdbg echoes the bytes received directly from the terminal for debugging
exactly what bytes or escape sequences a particular terminal is sending.  The
terminal is set to raw mode if possible.

termdbg's output is intended for human consumption; the output format is not
guaranteed and should not be parsed.

To exit, send the byte value 3.  This is the ASCII encoding for ^C (End Of
Text), or CTRL-C for most terminals.  If you are unable to exit, you can send
SIGINT from a separate terminal.
"""

import os
import sys
import termios
import tty

__version__ = '1.0.1'
STDIN = 0
STDOUT = 1


def main():
    with _RawTerm(STDOUT) as term:
        while True:
            _loop_once(STDIN, term)


def _loop_once(fd, term):
    char = _read_char(fd)
    term.print(_format_char(char))
    if char == 3:  # ^C
        sys.exit(0)


def _read_char(fd):
    """Read a char from the file descriptor."""
    return ord(os.read(fd, 1))


def _format_char(char):
    """Format a char for printing."""
    return '{char:3d}, 0o{char:03o}, 0x{char:02X}'.format(char=char)


class _TermAttrsContext:

    """Restore terminal attributes of fd on context exit."""

    def __init__(self, fd):
        """Initialize instance."""
        self._fd = fd
        self._old_attrs = None

    def __enter__(self):
        self._old_attrs = termios.tcgetattr(self._fd)

    def __exit__(self, exc_type, exc_val, exc_tb):
        termios.tcsetattr(self._fd, termios.TCSAFLUSH, self._old_attrs)


class _RawTerm(_TermAttrsContext):
    """Set terminal to raw mode within the context."""

    def __init__(self, fd):
        """Initialize instance."""
        self._fd = fd
        self._file = None

    def __enter__(self):
        super().__enter__()
        tty.setraw(self._fd)
        self._file = os.fdopen(self._fd, 'w')
        return self

    def print(self, *objects, sep=' ', end='\r\n', flush=False):
        """Print a string to the term while in raw mode."""
        print(*objects, sep=sep, end=end, file=self._file, flush=flush)


if __name__ == '__main__':
    main()
