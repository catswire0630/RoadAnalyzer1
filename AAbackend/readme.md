# [项目名称] - YOLO道路检测Web服务 :heart: :heart: :heart:
![封面](封面.png)

## :rocket:项目概述
- **核心功能**：基于YOLO模型，实现道路车辆行人检测与热力图显示功能，并通过FastAPI提供Web服务。
- **主要技术**：Ultralytics、Grand-CAM、FastAPI、JavaScript、HTML、CSS。

## :bulb:安装依赖
```
pip install -r requirements.txt #包含ultralytics、fastapi等依赖
```

## :hammer_and_wrench:项目结构
backend/  

├── main.py              # 入口文件  
├── models/              # 存放训练好的 YOLO 模型  
├── static/              # 存放前端静态资源（如HTML、CSS、JS）  
├── routes/              # API 逻辑（如上传、检测）  
│   ├── upload.py        # 处理图片上传  
│   ├── detect.py        # 进行目标检测  
│   └── websocket.py     # 处理 WebSocket 连接  
├── utils/               # 处理图像、推理逻辑  
│   ├── inference.py     # YOLO 模型加载与推理   
├── requirements.txt     # 依赖项  
├── yolov8_heatmap.py    # 热力图生成


## :handbag:使用说明
```
1.启动FastAPI Web服务
cd backend
uvicorn main:app --reload
2.打开浏览器，访问http://127.0.0.1:8000
3.上传图片，进行目标检测
4.查看结果
```

## :star2:修改说明
1. 可自主替换模型
1. 可自主调整热力图参数，可查看文件注释

## :stars:感谢
感谢[Ultralytics](https://github.com/ultralytics)提供的YOLO模型。  
感谢[魔鬼面具](https://github.com/z1069614715)提供的热力图生成代码。  
