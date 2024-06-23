from pathlib import Path
from openai import OpenAI
client = OpenAI()

input_file='output.txt'
input_text=''
with open(input_file, 'r') as file:
    input_text = file.read()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=input_text
  )

response.stream_to_file(speech_file_path)