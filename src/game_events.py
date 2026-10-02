from dataclasses import dataclass, field
from events import Event


@dataclass(frozen=True, slots=True)
class StartGameEvent(Event):
    pass



@dataclass(frozen=True, slots=True)
class ChangeSceneEvent(Event):
    name: str = field(default="Change Scene event", init=False)
    scene_name: str = field(init=True, repr=True)



@dataclass(frozen=True, slots=True)
class SetVolume(Event):
    name: str = field(default="SetVolume", init=False)
    volume: float = field(init=True, repr=True)



@dataclass(frozen=True, slots=True)
class MapMoveEvent(Event):
    name: str = field(default="Map move event", init=False)
    dx: float = field(init=True, repr=True)
    dy: float = field(init=True, repr=True)



@dataclass(frozen=True, slots=True)
class MapScaleEvent(Event):
    name: str = field(default="Map scale event", init=False)
    zoom: float= field(init=True, repr=True)
