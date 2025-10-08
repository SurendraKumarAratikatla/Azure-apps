from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello from Surendra's Flask App on Azure Web App! happy see comments 2 if possible !!!"

@app.route("/status")
def status():
    return {"status": "running", "app": "Flask on Azure"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
