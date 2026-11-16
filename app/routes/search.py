from fastapi import APIRouter, Query

from app.services.catalog import search_subjects as find_subjects

router = APIRouter()


@router.get("/")
def search_subjects(
    q: str = Query(default="", min_length=0, max_length=100),
    limit: int = Query(default=10, ge=1, le=100),
):
    results = find_subjects(q, limit)

    return {
        "query": q,
        "count": len(results),
        "results": [
            {
                "name": item["name"],
                "slug": item["slug"],
                "category": item["category_name"],
                "summary": item["summary"],
                "icon": item["icon"],
            }
            for item in results
        ],
    }
