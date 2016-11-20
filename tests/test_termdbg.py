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

import termios

from mir import termdbg


def test_restore_term_attrs():
    old_attrs = termios.tcgetattr(0)
    new_attrs = old_attrs + 1
    with termdbg.restore_term_attrs(0):
        termios.tcsetattr(0, termios.TCSANOW, new_attrs)
        assert termios.tcgetattr(0) == new_attrs
    assert termios.tcgetattr(0) == old_attrs
