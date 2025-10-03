from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
from pydantic import BaseModel
import random
import os

app = FastAPI(title="LinkSafe URL Scanner")

# Dummy URL scanning logic
def scan_url(url: str):
    labels = ["Safe", "Suspicious", "Malicious"]
    label = random.choice(labels)
    score = round(random.uniform(0.6, 0.99), 2)
    
    explanation = [
        "The URL uses HTTPS." if "https" in url else "The URL does not use HTTPS.",
        "The domain is recognized." if "example" in url else "The domain is unknown or new.",
        "No suspicious keywords found." if "login" not in url else "Suspicious keywords detected."
    ]
    
    advice = "Avoid clicking on unknown links." if label != "Safe" else "Link looks safe."
    
    return {
        "url": url,
        "label": label,
        "score": score,
        "explanation": explanation,
        "advice": advice
    }

# Request model
class URLRequest(BaseModel):
    url: str

# Endpoint for scanning URL
@app.post("/predict")
async def predict(request_data: URLRequest):
    result = scan_url(request_data.url)
    return JSONResponse(content=result)

# Serve index.html
@app.get("/", response_class=HTMLResponse)
async def index():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>index.html not found</h1>")

