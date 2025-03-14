# Name Capitalizer Web App

This is a simple web application built with **FastAPI**, **Jinja2 templates**, and **n8n** to demonstrate GET and POST requests. Users can submit a name via a form, and the app capitalizes it and displays the result on the webpage. The capitalization logic is handled by an n8n workflow, included as a JSON file for easy setup.

## Features
- Submit a name via a form (POST request).
- Display the capitalized name on the webpage (GET request).
- Uses FastAPI for the web server and Jinja2 for templating.
- Integrates with n8n for processing (workflow provided).

## Project Structure
```
name_app/
├── main.py                     # FastAPI application
├── templates/                  # Jinja2 templates
│   └── index.html             # HTML form and result page
├── capitalize_name_workflow.json  # n8n workflow file
├── requirements.txt           # Python dependencies
├── README.md                  # This file
```

## Prerequisites
- **Python 3.8+**: For running FastAPI.
- **n8n**: Workflow automation tool (installed globally or locally).
- **Git**: To clone the repository.

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/your-username/name-capitalizer-web-app.git
cd name-capitalizer-web-app


### 2. Install Python Dependencies
```
Create a virtual environment and install the required packages:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up n8n
- Install n8n globally (if not already installed):
  ```bash
  npm install -g n8n
  ```
- Start n8n in a terminal (keep it running):
  ```bash
  n8n
  ```
- Open n8n in your browser at `http://localhost:5678`.

### 4. Import the n8n Workflow
- In the n8n interface:
  1. Click the **"Import Workflow"** button (or drag-and-drop).
  2. Select the `capitalize_name_workflow.json` file from the project folder.
  3. Save the workflow.
  4. Activate it by toggling the "Active" switch (top-right) to ON (green).
- The workflow will listen at `http://localhost:5678/webhook/capitalize-name`.

### 5. Run the FastAPI App
```bash
uvicorn main:app --reload
```
- Open your browser at `http://localhost:8000` to use the app.

## How It Works
1. **User Input**: Enter a name in the form and submit (POST request to `/`).
2. **FastAPI**: Sends the name to n8n via a POST request to `http://localhost:5678/webhook/capitalize-name`.
3. **n8n**: Capitalizes the name and returns the result.
4. **FastAPI**: Renders the `index.html` template with the capitalized name (GET request).

## Example
- Input: `talha`
- Output: `Result: Talha`

## Notes
- The response time is ~2-3 seconds due to the HTTP round-trip to n8n. For a faster alternative, you could modify `main.py` to capitalize the name directly in FastAPI (see comments in the code).
- Ensure n8n is running and the workflow is active for the app to work.

## Troubleshooting
- **"Error contacting n8n"**: Verify n8n is running (`n8n start`) and the workflow is active.
- **404 Webhook Error**: Ensure the workflow is imported and active, and the URL in `main.py` matches (`http://localhost:5678/webhook/capitalize-name`).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (optional: add a LICENSE file if desired).

## Acknowledgments
- Built with [FastAPI](https://fastapi.tiangolo.com/), [n8n](https://n8n.io/), and [Jinja2](https://jinja.palletsprojects.com/).
- Thanks to the open-source community!
```
