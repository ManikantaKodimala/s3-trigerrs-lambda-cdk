from fastapi import APIRouter
from typing import Union

from model.item import Item

router = APIRouter()


@router.get("/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.put("/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "is_updated": True}


@router.put("/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "is_updated": True}


@router.post("/{item_id}")
def insert_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "is_saved": True}