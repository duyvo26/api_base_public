import subprocess

# Chạy ứng dụng FastAPI
if __name__ == "__main__":
    subprocess.Popen(["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "60074", "--workers", "2"])
