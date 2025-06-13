"""
ANSI

A library for working with ANSI escape sequences. Implementing Microsoft's
documented version [here][ms-docs]

[ms-docs]: https://learn.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences#cursor-visibility
"""

from typing import Final, Literal


ESC: Final[str] = "\x1b"
CSI: Final[str] = ESC + "["  # Control Sequence Introducer
OSC: Final[str] = ESC + "]"  # Operating System Command


# Simple Cursor Positioning
def reverse_index() -> str:
    """
    Reverse Index - RI

    Performs the reverse operation of \\n, moves the cursor up one line,
    maintains horizontal position, scrolls buffer if necessary.
    """
    return ESC + "M"


def save_cursor():
    """
    Save Cursor - DESCS

    Save cursor position in memory
    """
    return ESC + "7"


def restore_cursor():
    """
    Restore Cursor - DESCR

    Restore cursor position from memory
    """
    return ESC + "8"


# Cursor Positioning
def cursor_up(n: int = 1) -> str:
    """
    Cursor Up - CUU

    Move the cursor up by <n>
    """
    return CSI + str(n) + "A"


def cursor_down(n: int = 1) -> str:
    """
    Cursor Down - CUD

    Move the cursor down by <n>
    """
    return CSI + str(n) + "B"


def cursor_forward(n: int = 1) -> str:
    """
    Cursor Forward - CUF

    Move the cursor forward (Right) by <n>
    """
    return CSI + str(n) + "C"


def cursor_backward(n: int = 1) -> str:
    """
    Cursor Backward - CUB

    Move the cursor backward (Left) by <n>
    """
    return CSI + str(n) + "D"


def cursos_next_line(n: int = 1) -> str:
    """
    Cursor Next Line - CNL

    Move the cursor down by <n> lines
    """
    return CSI + str(n) + "D"


def cursor_prev_line(n: int = 1) -> str:
    """
    Cursor Previous Line - CPL

    Move the cursor up by <n> lines
    """
    return CSI + str(n) + "D"


def cursor_horz_abs(n: int = 1) -> str:
    """
    Cursor Horizontal Absolute - CHA

    Cursor moves to <n>th position horizontally in the current line
    """
    return CSI + str(n) + "G"


def cursor_vert_abs(n: int = 1) -> str:
    """
    Vertical Line Position Absolute - VPA

    Cursor moves to the <n>th position vertically in the current column
    """
    return CSI + str(n) + "d"


def cursor_pos(y: int = 1, x: int = 1) -> str:
    """
    Cursor Position - CUP

    Cursor moves to <x>; <y> coordinate within the viewport, where <x> is the
    column of the <y> line
    """
    return CSI + str(y) + ";" + str(x) + "H"


def cursor_hvp(y: int = 1, x: int = 1) -> str:
    """
    Horizontal Vertical Position - HVP

    Cursor moves to <x>; <y> coordinate within the viewport, where <x> is the
    column of the <y> line. Same as `CUP`, but is treated as a format effector
    function (CR or LF) instead of an editor function (CUD or CNL).
    """
    return CSI + str(y) + ";" + str(x) + "m"


# Cursor Visibility
def blink_on() -> str:
    """
    Text Cursor Enable Blinking - ATT160

    Start blinking the cursor.
    """
    return CSI + "?12h"


def blink_off() -> str:
    """
    Text Cursor Disable Blinking - ATT160

    Stop blinking the cursor.
    """
    return CSI + "?12l"


def show_cursor() -> str:
    """
    Text Cursor Enable Mode Show - DECTCEM

    Show the cursor.
    """
    return CSI + "?25h"


def hide_cursor() -> str:
    """
    Text Cursor Disable Mode Show - DECTCEM

    Hide the cursor.
    """
    return CSI + "?25l"


# Cursor Shape
def decscusr(n: int) -> str:
    return CSI + str(n) + " q"


def user_shape() -> str:
    """
    User Shape - DECSCUSR

    Default cursor shape configured by the user.
    """
    return decscusr(0)


def blinking_block() -> str:
    """
    Blinking Block - DECSCUSR

    Blinking block cursor shape.
    """
    return decscusr(1)


def steady_block() -> str:
    """
    Steady Block - DECSCUSR

    Steady block cursor shape.
    """
    return decscusr(2)


def blinking_underline() -> str:
    """
    Blinking Underline - DECSCUSR

    Blinking underline cursor shape.
    """
    return decscusr(3)


def steady_underline() -> str:
    """
    Steady Underline - DECSCUSR

    Steady underline cursor shape.
    """
    return decscusr(4)


def blinking_bar() -> str:
    """
    Blinking Bar - DECSCUSR

    Blinking bar cursor shape.
    """
    return decscusr(5)


def steady_bar() -> str:
    """
    Steady Bar - DECSCUSR

    Steady bar cursor shape.
    """
    return decscusr(6)


# Viewport Positioning
def scroll_up(n: int = 1) -> str:
    """
    Scroll Up - SU

    Scroll text up by <n>. Also known as pan down, new lines will in from the
    bottom fo the screen.
    """
    return CSI + str(n) + "S"


def scroll_down(n: int = 1) -> str:
    """
    Scroll Down - SD

    Scroll text down by <n>. Also known as pan up, new lines will in from the
    bottom fo the screen.
    """
    return CSI + str(n) + "T"


# Text Modification
def insert_character(n: int = 1) -> str:
    """
    Insert Character - ICH

    Insert <n> spaces at the current cursor position, shifting all existing text
    to the right. Text exiting the screen to the right is removed.
    """
    return CSI + str(n) + "@"


def delete_character(n: int = 1) -> str:
    """
    Delete Character - DCH

    Delete <n> characters at the current cursor position, shifting in space
    characters from the right edge of the screen.
    """
    return CSI + str(n) + "P"


def erase_character(n: int = 1) -> str:
    """
    Erase Character - ECH

    Erase <n> characters from the current cursor position by overwriting them
    with a space character.
    """
    return CSI + str(n) + "X"


def insert_line(n: int = 1) -> str:
    """
    Insert Line - IL

    Inserts <n> lines into the buffer at the cursor position. The line the
    cursor is on, and lines below it, will be shifted downwards.
    """
    return CSI + str(n) + "L"


def delete_line(n: int = 1) -> str:
    """
    Delete Line - DL

    Deletes <n> lines from the buffer, starting with the row the cursor is on.
    """
    return CSI + str(n) + "M"


# For the following two commands the parameter <n> has 3 valid values
# 0 erases from the current cursor position (inclusive) to the end of the
#   line/display
# 1 erases from the beginning of the line/display up to and including the
#   current cursor position
# 2 erases the entire line/display


def erase_in_display(n: Literal[0, 1, 2]) -> str:
    """
    Erase in Display - ED

    Replace all text in the current viewport/screen specified by <n> with space
    characters
    """
    return CSI + str(n) + "J"


def erase_in_line(n: Literal[0, 1, 2]) -> str:
    """
    Erase in Line - EL

    Replace all text on the line with the cursor specified by <n> with space
    characters
    """
    return CSI + str(n) + "K"


def default() -> str:
    return CSI + "0m"


# def bold(enable: True) -> str:
#     code = "1" if enable else "22"
#     return CSI +
