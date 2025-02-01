import librosa
import openai

openai.api_key = "your-api-key-here"

def analyze_music(file_path):
    y, sr = librosa.load(file_path, sr=None)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return f"Темп музики: {tempo:.2f} BPM"

def generate_poem(tempo):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Напиши вірш, що відповідає темпу {tempo} BPM",
        max_tokens=100
    )
    return response["choices"][0]["text"].strip()

file_path = "music.mp3"
tempo = analyze_music(file_path)
poem = generate_poem(tempo)
print(f"Згенерований вірш:
{poem}")
