# python-pdf-audio

## main.py
This script uses the pyttsx3 library, which is a Python wrapper for text-to-speech engines 
It reads the contents of the PDF file and converts it to an audio file using the text-to-speech engine 
We adjust the rate, volume, and voice properties to customize the audio output

To use this script, you will need to have Python and the pyttsx3 library installed on your system. 
You will also need to specify the paths to the PDF file and the output audio file in the pdf_path and audio_path variables, respectively


## main2.py
This code reads the contents of a PDF file and converts it to an audio file using the text-to-speech engine 
It reads each page of the PDF and cleans up the text by stripping leading and trailing whitespace and replacing newline characters with spaces 
It then saves the audio file and plays it using the save_to_file and runAndWait methods of the text-to-speech engine
Finally, it stops the engine when it is done

To use this code, you will need to have Python and the pyttsx3 and PyPDF2 libraries installed on your system
You will also need to specify the name of your PDF file in the pdf_file variable, and the name of the output audio file in the mp3_file variable
