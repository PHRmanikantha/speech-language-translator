from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr

mainwindow = Tk()
mainwindow.title("Speech-To-Text Converter")
mainwindow.geometry('500x500')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='orange')

def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="en-IN")
            except:
                text = "Error recognizing speech"
            return text

def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech-to-Text Converter')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='blue')

    Label(speechtotextwindow, text='Speech-to-Text Converter', font=("Comic Sans MS", 15), bg='black').place(x=50)
    text_box = Text(speechtotextwindow, font=12, height=3, width=30)
    text_box.place(x=7, y=100)
    record_button = Button(speechtotextwindow, text='Record', bg='Sienna', command=lambda: text_box.insert(END, recordvoice()))
    record_button.place(x=140, y=50)

Label(mainwindow, text='Speech-To-Text Converter', font=('Times New Roman', 16), bg='blue', wrap=True, wraplength=450).place(x=25, y=0)
speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='Purple', command=SpeechToText)
speechtotextbutton.place(x=100, y=250)

mainwindow.update()
mainwindow.mainloop()
