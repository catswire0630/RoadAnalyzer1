# -* coding: gbk *-
from unittest import result
import torch
import cv2
import numpy as np
from ultralytics import YOLO
import yolov8_heatmap



def draw_heatmap(model_path, img_path):
    params = yolov8_heatmap.get_params(model_path= "models/best.pt")
    model = yolov8_heatmap.yolo_heatmap(**params)
    model(img_path,r"D:\AAbackend\static\heatmap")
        


if __name__ == '__main__':
    model_path = r"D:\Test\Python\yolov8\yolov8_test\yolov8_test\runs\detect\train\yolo11v8CBAM_20epochs_32batch_4workers_adam\weights\best.pt"
    img_path = r"D:\Test\Python\yolov8\yolov8_test\yolov8_test\datasets\car\3.jpg"
    model =YOLO(model_path)
    # draw_heatmap(model_path, img_path)
    # print(torch.cuda.is_available())
    # model = YOLO(model_path)
    # print(type(model.model))
    # print(model.model)                                                                                    
    # test(model)
    # train()
    result = model.predict(img_path, save = True, project="./runs/detect/predict/road_detection")