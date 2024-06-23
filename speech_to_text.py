from openai import OpenAI
client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )



audio_file= open("/Users/liangshenghao/Projects/hackthalon/openAI/VOXTAB_Medical_audio.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
# print(type(transcription.text))

file_path = "output.txt"
with open(file_path, 'w') as file:
    # Write the string to the file
    file.write(transcription.text)
# print(completion.choices[0].message)