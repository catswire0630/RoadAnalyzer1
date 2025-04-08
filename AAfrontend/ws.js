let ws = new WebSocket("ws://127.0.0.1:8000/ws");// 创建 WebSocket 连接，用于实时通信
// 连接到后端的 WebSocket 端点
ws.onopen = () => console.log("WebSocket 已连接");// 打印连接成功的消息

ws.onmessage = (event) => {// 接收 WebSocket 消息并处理检测结果
    let detections = JSON.parse(event.data);// 解析后端发送的 JSON 数据
    drawDetections(detections.detections);
};

// 将上传的图片发送到 WebSocket
function sendImageToWS() {
    let imgElement = document.getElementById("uploadedImage");// 获取已上传的图片元素
    let canvas = document.createElement("canvas");
    let ctx = canvas.getContext("2d");

    canvas.width = imgElement.width;
    canvas.height = imgElement.height;
    ctx.drawImage(imgElement, 0, 0);

    let imageData = canvas.toDataURL("image/jpeg").split(",")[1];
    ws.send(imageData);// 通过 WebSocket 发送图片数据到后端
}
