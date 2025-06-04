from fastapi import APIRouter

router = APIRouter()

@router.get("/about")
def about() -> dict[str, str]:
    return {"message": "This is the about page."}