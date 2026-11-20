from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates

from app.services.catalog import (CATEGORIES,SUBJECTS,get_category,get_subject,get_subjects_for_category,)

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request,name="index.html",
        context={
            "categories": CATEGORIES,
            "featured_subjects": SUBJECTS[:4],
        },
    )


@router.get("/category/{category_slug}")
def category_page(request: Request, category_slug: str):
    category = get_category(category_slug)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return templates.TemplateResponse(
        request=request,
        name="category.html",
        context={
            "category": category,
            "subjects": get_subjects_for_category(category_slug),
        },
    )


@router.get("/subject/{subject_slug}")
def subject_page(request: Request, subject_slug: str):
    subject = get_subject(subject_slug)

    if subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")

    return templates.TemplateResponse(
        request=request,
        name="subject.html",
        context={"subject": subject},
    )
 