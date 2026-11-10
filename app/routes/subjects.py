from fastapi import APIRouter

from app.schemas.subject import Subject

router = APIRouter()


@router.get("/{subject_name}")
def get_subject(subject_name: str):
    return {
        "subject": subject_name
    }


@router.post("/")
def create_subject(subject: Subject):
    return {
        "message": "Subject received successfully",
        "subject": subject
    }