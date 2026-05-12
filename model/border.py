from dataclasses import dataclass


@dataclass
class Border():
    state1ab: str
    state1nm:  str
    state2ab: str
    year: int
    conttype: int



