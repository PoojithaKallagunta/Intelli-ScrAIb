# Intelli-ScrAIb

## 1. Project Overview 

### **Project Name:** *Intelli-ScrAIb – AI-Powered Content Generator*  
### **Description:**  
Intelli-ScrAIb is an AI-driven article generation and query answering platform that simplifies content creation using natural language prompts. Users can generate articles based on topic, tone, audience, and length. The system integrates LangChain with Google’s Gemini-Flash LLM for smart content generation and contextual Q&A, built with a responsive Flask web interface.

---

## 2. Prerequisites

- **Python Version:** 3.11  
- **Flask**  
- **LangChain**  
- **Gemini-Flash Model**  
- **HTML / Tailwind CSS**  
- **JavaScript (for UI interaction + Speech recognition)**  
- **VS Code or equivalent IDE**  
- **Browser (Chrome preferred)**  
- **dotenv**  

---

## 3. Project Setup

### Clone the Repository:
git clone https://github.com/YourUsername/Intelli-ScrAIb.git

---

## 4. Configuration

**Environment File:**
- Create a `secret.env` file with the following variable:
GOOGLE_API_KEY=your_gemini_api_key_here

**Port:**
- `main.py`: 5000 (Flask app runs on this port)

---

## 5. Directory Structure

Intelli-ScrAIb/
│
├── static/
│ └── css/
│ └── output.css # Tailwind compiled CSS
│
├── templates/
│ ├── index.html # Main UI interface
│ ├── about.html # About the platform
│ ├── contact.html # Contact information
│ ├── prompts.html # List of AI writing prompt categories
│
├── main.py # Flask backend and API logic
├── secret.env # Environment file for Gemini API key
├── README.md # Project documentation


---

## 6. Project Structure Description

- **`static/`**  
  Contains the Tailwind CSS styles used for styling the UI.

- **`templates/`**  
  All HTML UI pages rendered by Flask. Includes pages for article generation, about, prompts, and contact.

- **`index.html`**  
  Main landing page where the user provides prompt inputs and interacts with the AI.

- **`about.html`**  
  Provides a short description about the project, its purpose, and its vision.

- **`contact.html`**  
  Displays email and mobile number to reach the development team.

- **`prompts.html`**  
  Lists suggested categories and prompt formats for article generation.

- **`main.py`**  
  Backend logic to serve HTML, handle article generation via Gemini model, and answer queries using context-aware LangChain prompts.

- **`secret.env`**  
  Stores the Google Gemini API key securely for backend access.

---

## 7. API Endpoints

The Flask backend exposes the following endpoints:

- `GET /` – Main UI page (index)
- `POST /generate` – Accepts user preferences and returns generated article
- `POST /ask_query` – Accepts a question and article content, returns AI-generated answer
- `GET /about` – About page
- `GET /contact` – Contact information page
- `GET /prompts` – Prompt category page
- `GET /test` – Testing endpoint for Flask server status

---

## 8. Steps to Run the Application

Open a terminal in VS Code and execute:

python main.py

Once running, visit `http://127.0.0.1:5000/` in your browser.  
From there:

1. Enter a topic, select tone, audience, and length.
2. Click **Generate Article** to get AI-written content.
3. Use **🎤 Prompt** to input topic using voice.
4. Ask contextual follow-up questions via **Ask** button under “Ask Questions”.
5. View responses, or clear the chat with **Clear Chat**.

---
