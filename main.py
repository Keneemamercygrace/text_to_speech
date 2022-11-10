from gtts import gTTS
import os
import PyPDF2

pdf_file = open("02. World War One at Home author BBC.pdf", 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
count = pdf_reader.numPages
textList = []

for i in range(count):
    try:
        page = pdf_reader.getPage(i)
        textList.append(page.extractText())

    except:
        pass

textString = " ".join(textList)
language = 'en'

myobj = gTTS(text=textString, lang=language, slow=False)

myobj.save('world_war.mp3')
os.system("mpg321 welcome.mp3")
