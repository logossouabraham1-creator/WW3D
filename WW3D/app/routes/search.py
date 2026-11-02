from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/")
def search_subjects(
    category: str | None = None,
    limit: int = Query(default=10, ge=1, le=100)
):
    return {
        "category": category,
        "limit": limit
    }