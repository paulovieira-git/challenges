# pip install openai, scipy, sounddevice, audiofile, gtts, pyttsx3, keyboard
import openai
import sounddevice as sd
import audiofile as af
from scipy.io.wavfile import write
from gtts import gTTS
import pandas as pd
import multiprocessing
import pyttsx3
import keyboard
slow_talk = True
openai.api_key = "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"
input_audio_filename = 'input.wav'
output_audio_filename = 'chatgpt_response.wav'
log_filename = './conversation.txt'

chat = [{"role": "system", "content": "You are a helpful, happy, carefull and patient assistant made to help elder people and if the AI does not know the answer to a question, it truthfully says it does not know."}]

# Voice Record
def speech(text):
    p = multiprocessing.Process(target=pyttsx3.speak, args=(text,))
    p.start()
    while p.is_alive():
        if keyboard.is_pressed('enter'):
            p.terminate()
        else:
            continue
    p.join()

# Get audio with time
# def get_audio_time(filename, sec, sr = 44100):
#     audio = sd.rec(int(sec * sr), samplerate=sr, channels=2, blocking=False)
#     sd.wait()
#     write(filename, sr, audio)

# Get audio with enter
def get_audio_manual(filename, sr = 44100):
    input("  == Press enter to start talk. Say \'Thank you\' to Exit and generate log ==")
    audio = sd.rec(int(10 * sr), samplerate=sr, channels=2)
    input("  == Press enter when you finish ==")
    sd.stop()
    write(filename, sr, audio)

# Play audio
def play_audio(filename):
    signal, sr = af.read(filename)
    sd.play(signal, sr)

# Audio to txt
def audio_to_txt(filename):
    audio_file= open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    audio_file.close()
    return transcript

# Roseta stone
def roseta_stone(filename):
    audio_file= open(filename, "rb")
    translation = openai.Audio.translate("whisper-1", audio_file)
    audio_file.close()
    return translation

# text to audio generator
def save_text_as_audio(text, audio_filename):
    conversion = gTTS(text=text, lang='en', slow=slow_talk)
    conversion.save(audio_filename)

# save log
def save_log(conversation):
    data = pd.DataFrame(conversation)
    data.to_csv(log_filename, index=False)
    print('== Log Created ==')
    print('Thank you')


def main():
    while True:
        get_audio_manual(input_audio_filename)
        transcription = audio_to_txt(
            input_audio_filename)  # if we want to speak in another language  we would use 'translate_audio' function
        if transcription['text'].lower() == 'thank you.':
            save_log(chat)
            break
        chat.append({"role": "user", "content": transcription['text']})
        print(f"\nUser: {transcription['text']}")

        bot = openai.ChatCompletion.create(model="gpt-3.5-turbo", temperature=0.1, messages=chat)

        response = bot.choices[0].message.content
        chat.append({"role": "assistant", "content": response})
        print(f"Assistant: {response}")
        print("\n=== Press enter to stop the answer and start a new question ===\n")
        speech(response)


if __name__ == '__main__':
    main()