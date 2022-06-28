from typing import NamedTuple


class PositionInfo(NamedTuple):
    name: str
    price: int
    position_id: int
    category_id: int


class CategoryInfo(NamedTuple):
    id: int
    name: str
