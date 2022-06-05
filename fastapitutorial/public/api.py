from fastapi import APIRouter

from fastapitutorial.public.endpoints import items

router = APIRouter()

router.include_router(items.router, prefix="/items", tags=["items"])
