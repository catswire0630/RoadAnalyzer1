from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from routes.upload import router as upload_router
from routes.detect import router as detect_router
from routes.websocket import router as websocket_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Road Object Detection API")

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 注册路由
app.include_router(upload_router)
app.include_router(detect_router)
app.include_router(websocket_router)

# 服务前端页面
@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:5500",  # Live Server 默认端口
        "http://192.168.43.237",  # 你的 IP
        "http://192.168.43.175"   # 对方的 IP
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)