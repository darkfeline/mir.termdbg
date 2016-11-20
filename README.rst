mir.termdbg
=============

.. image:: https://circleci.com/gh/project-mir/mir.termdbg.svg?style=shield
   :target: https://circleci.com/gh/project-mir/mir.termdbg
   :alt: CircleCI
.. image:: https://codecov.io/gh/project-mir/mir.termdbg/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/project-mir/mir.termdbg
   :alt: Codecov
.. image:: https://badge.fury.io/py/mir.termdbg.svg
   :target: https://badge.fury.io/py/mir.termdbg
   :alt: PyPi Release

Simple terminal key press debugger.

termdbg echoes the bytes received directly from the terminal for debugging
exactly what bytes or escape sequences a particular terminal is sending.  The
terminal is set to raw mode if possible.

termdbg's output is intended for human consumption; the output format is not
guaranteed and should not be parsed.

To exit, send the byte value 3.  This is the ASCII encoding for ^C (End Of
Text), or CTRL-C for most terminals.  If you are unable to exit, you can send
SIGINT from a separate terminal.
