from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Home page with form (GET request)
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, result: str = None):
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

# Handle form submission (POST request)
@app.post("/", response_class=HTMLResponse)
async def process_name(request: Request, name: str = Form(...)):
    # Send the name to n8n Webhook
    # n8n_webhook_url = "http://localhost:5678/webhook-test/capitalize-name"
    n8n_webhook_url = "http://localhost:5678/webhook/capitalize-name"
    payload = {"name": name}
    response = requests.post(n8n_webhook_url, json=payload)
    
    if response.status_code == 200:
        # Get the capitalized name from n8n
        capitalized_name = response.json().get("capitalized_name", "Error")
        return templates.TemplateResponse("index.html", {"request": request, "result": capitalized_name})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "result": "Error contacting n8n"})

# Run the app with: uvicorn main:app --reload