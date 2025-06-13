"""
ANSI

A library for working with ANSI escape sequences. Implementing Microsoft's
documented version [here][ms-docs]

[ms-docs]: https://learn.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences#cursor-visibility
"""

ESC = "\x1b"
CSI = ESC + "["  # Control Sequence Introducer
OSC = ESC + "]"  # Operating System Command


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


def default() -> str:
    return CSI + "0m"


# def bold(enable: True) -> str:
#     code = "1" if enable else "22"
#     return CSI +
