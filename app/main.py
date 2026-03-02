from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>K8s Microservice</title>
            <style>
                body {
                    font-family: Arial;
                    text-align: center;
                    background-color: #0f172a;
                    color: white;
                    padding-top: 100px;
                }
                .card {
                    background: #1e293b;
                    padding: 30px;
                    border-radius: 10px;
                    display: inline-block;
                    box-shadow: 0 0 20px rgba(0,0,0,0.5);
                }
                h1 {
                    color: #38bdf8;
                }
                .status {
                    color: #22c55e;
                    font-size: 24px;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🚀 K8s Microservice</h1>
                <p class="status">STATUS: RUNNING ✅</p>
                <p>Deployed on AWS + Kubernetes</p>
            </div>
        </body>
    </html>
    """
