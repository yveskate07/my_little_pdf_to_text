from PyPDF2 import PdfReader
from gtts import gTTS

# Extraire le texte du PDF
file_name = input('Please type the path of the pdf file !\n')
reader = PdfReader(file_name)
text = ""
for page in reader.pages:
    text += page.extract_text()

# Transformer en audio
tts = gTTS(text, lang='fr')
tts.save("document_audio.mp3")
