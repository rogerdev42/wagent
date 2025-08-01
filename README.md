# Weather AI Agent

🌤️ **Weather AI Agent** is an AI-powered chatbot that provides real-time weather information in response to user questions in natural language.  
It combines OpenAI GPT, LangChain, FastAPI, Streamlit, and the OpenWeather API.

---

## 🚀 Features

- Natural language interface (Streamlit)
- AI agent with memory (LangChain + OpenAI)
- Real-time weather from OpenWeather API
- FastAPI backend with a clean `/ask` endpoint
- Docker + Docker Compose support

---

## 🛠️ Technologies

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI API](https://platform.openai.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [OpenWeather API](https://openweathermap.org/api)
- Docker & Docker Compose

---

## 📦 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rogerdev42/wagent.git
cd wagent
```
### 2. Configure environment variables

Create two .env files based on the provided examples:

- api/.env
- ui/.env

You can copy them from the .env.example files:
```bash
cp api/.env.example api/.env
cp ui/.env.example ui/.env
```
### 3. Start the application using Docker

```bash
docker-compose up --build
```
- FastAPI backend will run at: http://localhost:8000

- Streamlit UI will be available at: http://localhost:8501

## 💬 Example Prompt

    What's the weather in Tokyo?

## 📁 Project Structure

    wagent/
    ├── api/                  # FastAPI backend
    │   ├── main.py
    │   ├── config.py
    │   ├── requirements.txt
    │   └── .env.example
    ├── ui/                   # Streamlit frontend
    │   ├── app.py
    │   ├── requirements.txt
    │   └── .env.example
    ├── docker-compose.yml
    ├── README.md

## 📝 License

This project is licensed under the MIT License © 2025.