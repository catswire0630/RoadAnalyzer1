from fastapi import APIRouter
from utils.inference import run_inference

router = APIRouter()

@router.get("/detect/{image_name}")
async def detect_objects(image_name: str):
    """检测图片中的目标并返回标注图片路径"""
    image_path = f"static/uploads/{image_name}"
    results = run_inference(image_path)
    return results  # 包含 annotated_image_path