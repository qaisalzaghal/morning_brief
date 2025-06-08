import os
from gtts import gTTS
import subprocess
import ffmpeg
from agents.morning_brief import summarize_brief

"""
def voice_output():
    # Step 1: Generate voice as MP3
    tts = gTTS(text="You don't have any events scheduled for today.", lang='en')
    tts.save("summary.mp3")
    return "summary.mp3"

def convert_mp3_to_ogg(mp3_path, ogg_path):
    # Step 2: Convert MP3 to OGG (Opus codec) using ffmpeg
    subprocess.run([
        "ffmpeg", "-y", "-i", mp3_path,
        "-c:a", "libopus", "-b:a", "64k", "-vbr", "on",
        ogg_path
    ])
    return "summary.ogg"




mp3_file = voice_output()
ogg_file = "summary.ogg"
convert_mp3_to_ogg(mp3_file, ogg_file)

"""
def voice_output():
    from pydantic import BaseModel
    from pydantic_ai import Agent

    class VoiceInput(BaseModel):
        text: str

    class VoiceOutput(BaseModel):
        mp3_file: bytes

    config = Agent(
        model="openai:tts-1",
        system_prompt="Convert this text to a voice MP3.",
        input_model=VoiceInput,
        output_model=VoiceOutput
    )

    agent = Agent(config=config)

    result = agent.run_sync(VoiceInput(text=summarize_brief()))
    with open("summary.mp3", "wb") as f:
        f.write(result.mp3_file)

    return result    

