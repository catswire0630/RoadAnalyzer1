# [��Ŀ����] - YOLO��·���Web���� :heart: :heart: :heart:
![����](����.png)

## :rocket:��Ŀ����
- **���Ĺ���**������YOLOģ�ͣ�ʵ�ֵ�·�������˼��������ͼ��ʾ���ܣ���ͨ��FastAPI�ṩWeb����
- **��Ҫ����**��Ultralytics��Grand-CAM��FastAPI��JavaScript��HTML��CSS��

## :bulb:��װ����
```
pip install -r requirements.txt #����ultralytics��fastapi������
```

## :hammer_and_wrench:��Ŀ�ṹ
backend/  

������ main.py              # ����ļ�  
������ models/              # ���ѵ���õ� YOLO ģ��  
������ static/              # ���ǰ�˾�̬��Դ����HTML��CSS��JS��  
������ routes/              # API �߼������ϴ�����⣩  
��   ������ upload.py        # ����ͼƬ�ϴ�  
��   ������ detect.py        # ����Ŀ����  
��   ������ websocket.py     # ���� WebSocket ����  
������ utils/               # ����ͼ�������߼�  
��   ������ inference.py     # YOLO ģ�ͼ���������   
������ requirements.txt     # ������  
������ yolov8_heatmap.py    # ����ͼ����


## :handbag:ʹ��˵��
```
1.����FastAPI Web����
cd backend
uvicorn main:app --reload
2.�������������http://127.0.0.1:8000
3.�ϴ�ͼƬ������Ŀ����
4.�鿴���
```

## :star2:�޸�˵��
1. �������滻ģ��
1. ��������������ͼ�������ɲ鿴�ļ�ע��

## :stars:��л
��л[Ultralytics](https://github.com/ultralytics)�ṩ��YOLOģ�͡�  
��л[ħ�����](https://github.com/z1069614715)�ṩ������ͼ���ɴ��롣  
