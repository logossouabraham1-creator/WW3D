from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.pages import router as pages_router
from app.routes.search import router as search_router
from app.routes.subjects import router as subjects_router

app = FastAPI(
    title="WordWorld 3D",
    description="Explore Everything",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(pages_router)
app.include_router(
    subjects_router,
    prefix="/api/subjects",
    tags=["Subjects"],
)
app.include_router(
    search_router,
    prefix="/api/search",
    tags=["Search"],
)
