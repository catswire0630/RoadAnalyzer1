// 主题切换
const themeToggle = document.getElementById('themeToggle');// 获取主题切换按钮元素
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    const icon = themeToggle.querySelector('i');
    if (document.body.classList.contains('dark')) {
        icon.classList.replace('fa-moon', 'fa-sun');
    } else {
        icon.classList.replace('fa-sun', 'fa-moon');
    }
});

// 模拟进度条动画：为异步操作提供视觉反馈
function simulateProgress(progressBar, callback) {
    let width = 0;
    const interval = setInterval(() => {
        width += 10;
        progressBar.style.width = `${width}%`;
        if (width >= 100) {
            clearInterval(interval);
            callback();
        }
    }, 100);
}

// 上传按钮事件：处理图片上传逻辑
document.getElementById('uploadBtn').addEventListener('click', async function() {
    const fileInput = document.getElementById('uploadInput');
    const file = fileInput.files[0];// 获取用户选择的文件

    if (!file) {
        alert('请先选择一个图片文件！');
        return;
    }

    const formData = new FormData();// 创建 FormData 对象，用于上传文件
    formData.append("file", file);

    const progress = document.getElementById('uploadProgress');
    const progressBar = document.getElementById('uploadProgressBar');
    progress.style.display = 'block';
    this.disabled = true;

    try {
        simulateProgress(progressBar, async () => {// 模拟进度条并执行上传
            const response = await axios.post('http://127.0.0.1:8000/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });

            const imagePath = `http://127.0.0.1:8000/${response.data.file_path}`;// 构造上传图片的 URL
            const uploadedImage = document.getElementById('uploadedImage');// 获取显示图片的元素
            uploadedImage.src = imagePath;
            uploadedImage.style.display = 'block';
            setTimeout(() => uploadedImage.classList.add('visible'), 10);

            document.getElementById('detectBtn').dataset.filename = response.data.filename;
            document.getElementById('detectBtn').disabled = false;

            alert('文件上传成功！');
            progress.style.display = 'none';
            progressBar.style.width = '0%';
            this.disabled = false;
        });
    } catch (error) {// 处理上传错误
        console.error('文件上传失败:', error.response ? error.response.data : error.message);
        alert('文件上传失败，请重试！');
        progress.style.display = 'none';
        progressBar.style.width = '0%';
        this.disabled = false;
    }
});


// 检测按钮事件：处理图片检测逻辑
document.getElementById('detectBtn').addEventListener('click', async function() {
    const filename = this.dataset.filename;

    if (!filename) {// 检查是否已上传图片
        alert('请先上传图片！');
        return;
    }

    const loading = document.getElementById('loading');
    const progress = document.getElementById('detectProgress');
    const progressBar = document.getElementById('detectProgressBar');
    loading.style.display = 'inline-block';
    progress.style.display = 'block';
    this.disabled = true;

    try {
        simulateProgress(progressBar, async () => {
            const response = await axios.get(`http://127.0.0.1:8000/detect/${filename}`);
            console.log('检测结果:', response.data);

            if (response.data.error) {// 检查是否有错误
                alert(`检测失败: ${response.data.error}`);
                return;
            }

            const annotatedImagePath = `http://127.0.0.1:8000/${response.data.annotated_image_path}`;
            const uploadedImage = document.getElementById('uploadedImage');// 获取图片元素
            uploadedImage.src = annotatedImagePath;// 更新为标注图片
            uploadedImage.style.display = 'block';// 显示图片
            setTimeout(() => uploadedImage.classList.add('visible'), 10);

            if (response.data.heatmap_image_path) {// 如果有热力图
                const heatmapImagePath = `http://127.0.0.1:8000/${response.data.heatmap_image_path}`;// 构造热力图 URL
                const heatmapImage = document.getElementById('heatmapImage');
                heatmapImage.src = heatmapImagePath;
                heatmapImage.style.display = 'block';// 显示热力图
                setTimeout(() => heatmapImage.classList.add('visible'), 10);
            } else {
                document.getElementById('heatmapImage').style.display = 'none';
                alert('热力图生成失败，请检查图片格式或模型配置');
            }

            // 显示统计结果
            const classCounts = response.data.class_counts;// 获取类别统计数据
            let summaryText = '';
            if (Object.keys(classCounts).length > 0) {// 如果检测到目标
                summaryText = Object.entries(classCounts)
                    .map(([cls, count]) => `${cls === 'person' ? '人' : cls === 'car' ? '车' : cls}: ${count}`)
                    .join('，');
            } else {
                summaryText = '未检测到目标';// 无目标时的提示
            }
            document.getElementById('summaryText').textContent = summaryText;
            document.getElementById('detectionSummary').style.display = 'block';

            loading.style.display = 'none';
            progress.style.display = 'none';
            progressBar.style.width = '0%';
            this.disabled = false;
        });
    } catch (error) {
        console.error('检测失败:', error.response ? error.response.data : error.message);
        alert('检测失败，请重试！');
        loading.style.display = 'none';
        progress.style.display = 'none';
        progressBar.style.width = '0%';
        this.disabled = false;
    }
});