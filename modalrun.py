import modal
import subprocess
app = modal.App("playdoai")
@app.function(gpu="H100")
def run():
    subprocess.run(["git", "clone", ""])
    subprocess.run(["python", "inference.py"])