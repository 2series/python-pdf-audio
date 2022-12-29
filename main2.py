import pyttsx3,PyPDF2

# Insert the name of your PDF file
pdf_file = 'book.pdf'

# Initialize the PDF reader and text-to-speech engine
pdfreader = PyPDF2.PdfFileReader(open(pdf_file, 'rb'))
speaker = pyttsx3.init()

# Loop through the pages of the PDF and read the text
for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

# Name the MP3 file whatever you would like
mp3_file = 'story.mp3'

# Save the audio file and play it
speaker.save_to_file(clean_text, mp3_file)
speaker.runAndWait()

# Stop the text-to-speech engine
speaker.stop()
