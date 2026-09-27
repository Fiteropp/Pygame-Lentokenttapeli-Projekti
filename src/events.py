from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class Event:
    name = "Generic event"



@dataclass(frozen=True, slots=True)
class TickEvent(Event):
    """
    Tick event
    """

    name = "Tick event"



@dataclass(frozen=True, slots=True)
class QuitEvent(Event):
    """
    Quit event
    """

    name = "Quit event"



@dataclass(frozen=True, slots=True)
class InputEvent(Event):
    """
    Keyboard input event
    """

    name = "Keyboard Input event"
    unicodechar: str = field(init=True)



@dataclass(frozen=True, slots=True)
class KeyboardStateEvent(Event):
    """
    Snapshot of which keys are currently held, posted once per tick.
    """
    name: str = field(default="Keyboard State event", init=False)
    keys: frozenset[int] = field(init=True, repr=True)



@dataclass(frozen=True, slots=True)
class MouseInputEvent(Event):
    """
    Mouse input event
    """

    name = "Mouse Input event"
    clickpos: tuple[int, int] = field(init=True, repr=True)
    mouse_btn: tuple = field(init=True, repr=True)



@dataclass(frozen=True, slots=True)
class MouseScrollEvent(Event):
    """
    Mouse scroll wheel event.
    """

    name: str = field(default="Mouse Scroll event", init=False)
    pos: tuple[int, int] = field(init=True, repr=True)
    scroll_y: int = field(init=True, repr=True)  # positive = up, negative = down



@dataclass(frozen=True, slots=True)
class InitializeEvent(Event):
    """
    Tells all listeners to initialize themselves.
    This includes loading libraries and resources.

    Avoid initializing such things within listener __init__ calls
    to minimize snafus (if some rely on others being yet created.)
    """

    name = "Initialize event"
