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

from mir.termdbg.term import RawTerm
from mir.termdbg.format import format_char

STDIN = 0


def main():
    with RawTerm(STDIN):
        while True:
            _loop_once(STDIN)


def _loop_once(fd):
    char: int = _read_char(fd)
    print(format_char(char), end='\r\n')
    if char == 3:  # ^C
        sys.exit(0)


def _read_char(fd) -> int:
    """Read a char from the file descriptor."""
    return ord(os.read(fd, 1))


if __name__ == '__main__':
    main()
