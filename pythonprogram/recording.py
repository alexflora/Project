#Listening audio from microphone
"""import speech_recognition as sr

recognizer = sr.Recognizer()

# Open the microphone and capture audio
with sr.Microphone() as source:
    print("Please speak something...")
    audio = recognizer.listen(source, timeout=10)  # Adjust the timeout as needed

# Recognize the speech
try:
    text = recognizer.recognize_google(audio)
    print(f"Transcription: {text}")
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print(f"Error with the speech recognition service: {e}") """


#Get the audio from our local system

"""import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load your audio file
audio_file = "C:\pythonprogram\Recordwav2.wav"  # Replace with the path to your audio file

# Recognize the speech from the audio file
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)  # Read the entire audio file

# Perform speech recognition
try:
    text = recognizer.recognize_google(audio_data)
    print(f"Transcription: {text}")
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Error with the speech recognition service: {e}")"""

#Useing recognizer sphinx method

"""import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load your audio file
audio_file = "C:\pythonprogram\Recordwav2.wav"   # Replace with the path to your audio file

# Recognize the speech from the audio file using Sphinx
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)  # Read the entire audio file

# Perform speech recognition using Sphinx
try:
    text = recognizer.recognize_sphinx(audio_data)
    print(f"Transcription: {text}")
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Error with the speech recognition service: {e}")"""

#convert tamil to english

"""from googletrans import Translator

# Initialize the translator
translator = Translator()

# Text to translate
text_to_translate = "வணக்கம், எப்படி இருக்கின்றது?"

# Detect the source language (optional)
detected_language = translator.detect(text_to_translate).lang
print(f"Detected Language: {detected_language}")

# Translate to English
translated_text = translator.translate(text_to_translate, src=detected_language, dest='en')

# Print the translation
print(f"Translation to English: {translated_text.text}")"""

# Using Speach recognition to convert tamil to english

"""import speech_recognition as sr
from googletrans import Translator

# Initialize the recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

# Function to transcribe and translate audio
def transcribe_and_translate(audio_file):
    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file

    # Perform speech recognition
    try:
        detected_language = recognizer.recognize_google(audio_data, language="ta-IN")
        print(f"Detected Language: {detected_language}")

        # Translate to English
        translation = translator.translate(detected_language, src="ta", dest="fr")
        print(f"Translation to English: {translation.text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")

# Path to your Tamil audio file
audio_file =r"C:\pythonprogram\tamilrec2.wav"  # Replace with the path to your audio file

# Perform transcription and translation
transcribe_and_translate(audio_file)"""

#Merge two audio File 

"""# import required libraries
from pydub import AudioSegment
from pydub.playback import play
 
wav_file_1 = AudioSegment.from_file("C:\pythonprogram\Recordwav1.wav")
wav_file_2 = AudioSegment.from_file("C:\pythonprogram\Recordwav2.wav")
 
# Combine the two audio files
wav_file_3 = wav_file_1 + wav_file_2
  
# play the sound
play(wav_file_3)"""

#Increasing/Decreasing volume of the file: By using ‘+’ and ‘-‘ operator.

"""# import required library
import pydub
from pydub.playback import play
 
wav_file =  pydub.AudioSegment.from_file(file = "C:\pythonprogram\tamilrec2.wav",
                                         format = "wav")
# Increase the volume by 10 dB
new_wav_file = wav_file + 10
 
# Reducing volume by 5
silent_wav_file = wav_file - 5
 
#  Playing silent file
play(silent_wav_file)
 
#  Playing original file
play(wav_file)
 
#  Playing louder file
play(new_wav_file)"""


# Import the required modules
import speech_recognition as sr
from pydub import AudioFile

# Create a Recognizer instance
r = sr.Recognizer()

# Define a function to convert voice to text
def voice_to_text(filename):
    
# Load the audio file
    audio = AudioFile(filename)
# Convert the audio file to a compatible format
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
# Create an AudioData instance from the audio file
    data = sr.AudioData(audio.raw_data, audio.frame_rate, audio.sample_width)
# Recognize the speech using Google's Speech Recognition API
    try:
# Return the transcribed text
        return r.recognize_google(data)
    except sr.UnknownValueError:
# Return an error message if speech is not recognized
        return "Speech could not be recognized"
    except sr.RequestError as e:
#Return an error message if there is a problem with the API request
        return f"Could not request results from Google Speech Recognition service; {e}"

filename="C:\pythonprogram\Recordwav2.wav"
voice_to_text(filename)
 



