# 🌞 Morning Brief Voice Assistant

A voice-based assistant that fetches your unread Outlook emails and calendar events every morning, summarizes them using PydanticAI/MCP, converts to speech, and sends them to you via Telegram.

---

## 🚀 Features

- 📬 Fetches Outlook unread emails and events via **Microsoft Graph API**
- 🧠 Summarizes them using **PydanticAI / MCP schema agent**
- 🔊 Converts the summary to voice using **OpenAI TTS** or `gTTS`
- 📤 Sends both voice and text to **Telegram**
- 🔁 Automate via **webhooks** or **n8n** workflows

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/yourusername/morning-brief.git
cd morning-brief



### 2. Install dependencies

pip install -r requirements.txt


### 3. Azure AD App Registration

To access Outlook data:

- Go to Azure Portal

- Register an App:

 - Redirect URI: http://localhost

 - Grant these API permissions:

   - Mail.Read

   - Calendars.Read

- Note the following:

 - CLIENT_ID

 - TENANT_ID

 - CLIENT_SECRET (if using confidential flow)


## 🔐 Environment Variables

CLIENT_ID=your-client-id
TENANT_ID=your-tenant-id
CLIENT_SECRET=your-secret (if needed)
BOT_TOKEN=your-telegram-bot-token
CHAT_ID=your-chat-id
OPENAI_API_KEY=your-openai-api-key

## 📃 Example CLI Commands

python main.py

python utils/tts.py

docker build -t morning_brief_docker .

morning-brief/
│
├── .env
├── requirements.txt
├── utils/
│   ├── tts.py
│   ├── stt.py
│   └── _ _init__.py
├── agents/
│   └── morning_brief.py
├── data_source/
│   ├── microsoft_graph_api.py
|   ├── voice_input.py
├── out_voice/
│   └── telegram_voice.py
├── Dockerfile
├── docker-compose.yml
├── README.md


