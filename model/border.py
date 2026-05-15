from dataclasses import dataclass


@dataclass
class Border():
    state1ab: str
    state1nm: str
    state2ab: str
    state2nm: str
    year: int
    conttype: int


