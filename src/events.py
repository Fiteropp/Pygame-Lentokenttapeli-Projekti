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
    dt: float = field(init=True, repr=False)


@dataclass(frozen=True, slots=True)
class QuitEvent(Event):
    """
    Quit event
    """

    name = "Quit event"


@dataclass(frozen=True, slots=True)
class KeyInputEvent(Event):
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
    click_pos: tuple[int, int] = field(init=True, repr=True)
    mouse_btn: tuple = field(init=True, repr=True)


@dataclass(frozen=True, slots=True)
class MouseMoveEvent(Event):
    """
    Mouse move event
    """

    name = "Mouse move event"
    mouse_pos: tuple[int, int] = field(init=True, repr=True)


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
    """

    name = "Initialize event"


@dataclass(frozen=True, slots=True)
class PygameReadyEvent(Event):
    """
    Posted once pygame's display and font systems are ready.
    Carries the detected monitor refresh rate.
    """
    name: str = field(default="Pygame Ready event", init=False)
    refresh_rate: int = field(init=True, repr=True)


@dataclass(frozen=True, slots=True)
class AssetsReadyEvent(Event):
    """
    All assets loaded.
    """

    name: str = field(default="Assets Ready event", init=False)

@dataclass(frozen=True, slots=True)
class DBConnect(Event):
    """
        Connection to database.
    """

    db_connected: bool = False
