
#pip.exe install openai sounddevice audiofile scipy gtts pandas multiprocessing pyttsx3 bard
import sounddevice as sd
import audiofile as af
from scipy.io.wavfile import write
from gtts import gTTS
import pandas as pd
import pyttsx3
import keyboard
import openai

# Set the OpenAI API key
openai.api_key = "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"

input_audio_filename = 'input.wav'
output_audio_filename = 'response.wav'
log_filename = 'conversation_bard.txt'

chat = [{"role": "system", "content": "You are a helpful, careful, and patient assistant made to help older people. If you do not know the answer to a question, you truthfully say you do not know."}]

# Voice Record
def record_audio(filename, duration_sec=10, sr=44100):
    input("  == Press enter to start talking. Say 'Thank you' to exit and generate a log ==")
    audio = sd.rec(int(duration_sec * sr), samplerate=sr, channels=2)
    input("  == Press enter when you finish ==")
    sd.stop()
    write(filename, sr, audio)

# Play audio
def play_audio(filename):
    signal, sr = af.read(filename)
    sd.play(signal, sr)

# Audio to txt
def audio_to_txt(filename):
    with open(filename, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript

# Text to audio generator
def save_text_as_audio(text, audio_filename, slow_talk=True):
    conversion = gTTS(text=text, lang='en', slow=slow_talk)
    conversion.save(audio_filename)

# GPT-3 response generator
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Replace with the engine of your choice
        prompt=prompt,
        max_tokens=100,  # Adjust the max_tokens as needed for the desired response length
    )
    return response['choices'][0]['text'].strip()

# Save log
def save_log(conversation):
    data = pd.DataFrame(conversation)
    data.to_csv(log_filename, index=False)
    print('== Log Created ==')
    print('Thank you')

def main():
    while True:
        record_audio(input_audio_filename)
        transcription = audio_to_txt(input_audio_filename)

        if transcription['text'].lower() == 'thank you.':
            save_log(chat)
            break

        chat.append({"role": "user", "content": transcription['text']})
        print(f"\nUser: {transcription['text']}")

        question = transcription['text']
        response = generate_response(question)
        chat.append({"role": "assistant", "content": response})
        print(f"Assistant: {response}")
        print("\n=== Press enter to stop the answer and start a new question ===\n")
        pyttsx3.speak(response)

if __name__ == '__main__':
    main()