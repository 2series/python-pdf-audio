import os
import pyttsx3

# Set the path to the PDF file
pdf_path = "path/to/your/pdf/file.pdf"

# Set the path to the output audio file
audio_path = "path/to/your/audio/file.mp3"

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Open the PDF file and read its contents
with open(pdf_path, "r") as f:
    text = f.read()

# Set the audio file format
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)
engine.setProperty("voice", "english")

# Save the audio file
engine.save_to_file(text, audio_path)
engine.runAndWait()

print("PDF converted to audio successfully!")
