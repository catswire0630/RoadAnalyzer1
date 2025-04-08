from ultralytics import YOLO
import cv2
import os
import time
import yolov8_heatmap

# 加载预训练的 YOLOv8 模型，路径指向 "models/best.pt"
model = YOLO("models/best.pt")


def draw_heatmap(model_path, img_path):
    """
    生成目标检测的热力图并保存到指定目录。

    Args:
        model_path (str): YOLO 模型的路径。
        img_path (str): 输入图片的路径。

    Returns:
        str or None: 成功时返回热力图保存路径，失败时返回 None。
    """
    try:
        # 获取热力图生成所需的参数（依赖 yolov8_heatmap 模块）
        params = yolov8_heatmap.get_params(model_path=model_path)
        # 初始化热力图生成器
        heatmap_model = yolov8_heatmap.yolo_heatmap(**params)

        heatmap_output_dir = "static/heatmap/"
        os.makedirs(heatmap_output_dir, exist_ok=True)
        temp_dir = os.path.join(heatmap_output_dir, "temp")
        os.makedirs(temp_dir, exist_ok=True)
        heatmap_model(img_path, temp_dir)
        temp_file = os.path.join(temp_dir, "result.png")
        base_name = os.path.splitext(os.path.basename(img_path))[0]
        heatmap_filename = f"{base_name}_heatmap_{int(time.time())}.jpg"
        heatmap_path = os.path.join(heatmap_output_dir, heatmap_filename)  # 最终热力图路径
        if os.path.exists(temp_file):
            if os.path.exists(heatmap_path):
                os.remove(heatmap_path)
            os.rename(temp_file, heatmap_path)
            os.rmdir(temp_dir)
            return heatmap_path  # 返回热力图路径
        else:
            os.rmdir(temp_dir)
            return None
    except Exception as e:
        # 处理异常（例如模型加载失败、文件操作错误等）
        if os.path.exists(temp_dir):
            os.rmdir(temp_dir)
        return None  # 返回 None 表示失败


def run_inference(image_path):
    """
    对输入图片进行目标检测，生成标注图片、热力图和类别统计。

    Args:
        image_path (str): 输入图片的路径。

    Returns:
        dict: 包含标注图片路径、热力图路径和类别统计的字典，失败时返回错误信息。
    """
    try:
        # 使用 OpenCV 读取输入图片
        image = cv2.imread(image_path)
        if image is None:  # 检查图片是否成功加载
            raise ValueError(f"无法读取图片: {image_path}")

        # 使用 YOLO 模型进行目标检测，results[0] 获取第一个结果
        results = model(image)[0]
        annotated_image = results.plot()
        annotated_output_dir = "static/annotated/"
        # 创建目录，如果已存在则跳过
        os.makedirs(annotated_output_dir, exist_ok=True)
        base_name = os.path.basename(image_path)
        annotated_filename = f"{os.path.splitext(base_name)[0]}_annotated_{int(time.time())}.jpg"
        annotated_path = os.path.join(annotated_output_dir, annotated_filename)

        # 如果目标文件已存在，先删除以避免冲突
        if os.path.exists(annotated_path):
            os.remove(annotated_path)
        # 保存标注图片到指定路径
        cv2.imwrite(annotated_path, annotated_image)

        # 统计检测结果中的类别数量
        class_counts = {}
        for box in results.boxes:
            cls_id = int(box.cls[0])  # 获取类别 ID
            class_name = model.names[cls_id]
            class_counts[class_name] = class_counts.get(class_name, 0) + 1

        # 调用热力图生成函数
        heatmap_path = draw_heatmap("models/best.pt", image_path)

        # 返回检测结果，包括标注图片路径、热力图路径和类别统计
        return {
            "annotated_image_path": annotated_path,
            "heatmap_image_path": heatmap_path if heatmap_path else None,  # 如果热力图生成失败则返回 None
            "class_counts": class_counts  # 返回类别统计数据
        }
    except Exception as e:
        # 处理异常（例如图片读取失败、模型推理错误等）
        return {"error": str(e)}  # 返回错误信息