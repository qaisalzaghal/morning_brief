import requests
from utils import voice_output
from agents.morning_brief import summarize_brief

def send_voice_to_telegram(ogg_path, bot_token, chat_id):

    url = f"https://api.telegram.org/bot{bot_token}/sendVoice"
    with open(ogg_path, 'rb') as voice:
        response = requests.post(
            url,
            data={'chat_id': chat_id},
            files={'voice': voice}
        )
    print("Voice response:", response.json())


def send_text_to_telegram(message, bot_token, chat_id):

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    response = requests.post(
        url,
        data={'chat_id': chat_id, 'text': message}
    )
    print("Text response:", response.json())


BOT_TOKEN = "8115131625:AAGUS-xNoSBWNG527_cssWAMVdO6yAzgxZo"
CHAT_ID = "1535217669"

ogg_file = voice_output()

text_summary = summarize_brief()  

send_text_to_telegram(text_summary, BOT_TOKEN, CHAT_ID)
send_voice_to_telegram(ogg_file, BOT_TOKEN, CHAT_ID)
