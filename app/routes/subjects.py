from fastapi import APIRouter, HTTPException

from app.schemas.subject import Subject
from app.services.catalog import SUBJECTS, get_subject

router = APIRouter()


@router.get("/")
def list_subjects():
    return {"subjects": SUBJECTS}


@router.get("/{subject_name}")
def get_subject_api(subject_name: str):
    subject = get_subject(subject_name.lower().replace(" ", "-"))

    if subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")

    return subject


@router.post("/")
def create_subject(subject: Subject):
    return {
        "message": (
            "Subject received. This is a temporary demonstration; "
            "it has not been saved."
        ),
        "subject": subject,
    }
