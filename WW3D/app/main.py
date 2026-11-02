from fastapi import FastAPI
from app.routes.subjects import router as subjects_router
from app.routes.search import router as search_router

app = FastAPI(title="WordWorld 3D", description="Explore Everything", version="1.0.0")

app.include_router(
    subjects_router,
    prefix="/api/subjects",
    tags=["Subjects"]
)
app.include_router(
    search_router,
    prefix="/api/search",
    tags=["Search"]
)

@app.get("/")
def home():
    return {"message": "Welcome to WordWorld 3d."}


