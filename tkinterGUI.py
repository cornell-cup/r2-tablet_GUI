from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import threading
import time

class GUIapp():
    def __init__(self):
        self.i = 0
        root = Tk()
        root.geometry("750x450")
        self.note = ttk.Notebook(root)

        self.tab1 = ttk.Frame(self.note)
        self.tab2 = ttk.Frame(self.note)
        self.tab3 = ttk.Frame(self.note)
        self.tab4 = ttk.Frame(self.note)

        # tab 1 information : General Info
        text = Label(self.tab1, text="This is Cornell Cup.", width=50)
        text.pack(side=LEFT)

        # tab 2 information : Visual Img

        # tab 3 information : Data Streaming
        Facial_Recognition_Photo_path = "cropped.jpg"
        img = Image.open(Facial_Recognition_Photo_path)
        img = img.resize((180, 180), Image.ANTIALIAS)
        Facial_Recognition_Photo_img = ImageTk.PhotoImage(img)

        c1 = Label(self.tab3, text="Voice Recognition Text", font=("Helvetica", 19))
        c2 = Label(self.tab3, text="Sentiment Analysis Output", font=("Helvetica", 19))
        c3 = Label(self.tab3, text="Facial Recognition Photo", font=("Helvetica", 19))
        c4 = Label(self.tab3, text="Facial Recognition Result", font=("Helvetica", 19))
        c5 = Label(self.tab3, text="Object Detection Result", font=("Helvetica", 19))
        self.data1 = Label(self.tab3, text="", font=("Courier", 19))
        self.data2 = Label(self.tab3, text="", font=("Courier", 19))
        self.data3 = Label(self.tab3, image=Facial_Recognition_Photo_img)
        self.data4 = Label(self.tab3, text="", font=("Courier", 19))
        self.data5 = Label(self.tab3, text="", font=("Courier", 19))

        c1.grid(row=0, column=0, padx=5, pady=5)
        c2.grid(row=0, column=1, padx=5, pady=5)
        c3.grid(row=2, column=0, padx=5, pady=5)
        c4.grid(row=2, column=1, padx=5, pady=5)
        c5.grid(row=4, column=0, padx=5, pady=5, rowspan=1)
        self.data1.grid(row=1, column=0, padx=5, pady=5)
        self.data2.grid(row=1, column=1, padx=5, pady=5)
        self.data3.grid(row=3, column=0, padx=5, pady=5)
        self.data4.grid(row=3, column=1, padx=5, pady=5)
        self.data5.grid(row=5, column=0, padx=5, pady=5, rowspan=1)

        # tab 4 information : Sign up





        self.note.add(self.tab1, text="General Info")
        self.note.add(self.tab2, text="Visual Img")
        self.note.add(self.tab3, text="Data Streaming")
        self.note.add(self.tab4, text="Sign up")
        self.note.pack()

        # create a thread to constantly update the text in the streaming tab
        thread1 = threading.Thread(target=self.update_stream_text)
        thread1.start()

        root.mainloop()

    # update the text in the streaming tab once a second
    def update_stream_text(self):
        while 1:
            FacialRecognitionResult = open('FacialRecognitionResult.txt', 'r').read()
            VoiceRecognitionText = open('VoiceRecognitionText.txt', 'r').read()
            SentimentAnalysisOutput = open('SentimentAnalysisOutput.txt', 'r').read()
            ObjectDetectionResult = open('ObjectDetectionResult.txt', 'r').read()
            self.data1['text'] = FacialRecognitionResult
            self.data2['text'] = VoiceRecognitionText
            self.data4['text'] = SentimentAnalysisOutput
            self.data5['text'] = ObjectDetectionResult
            self.tab3.update()
            # make the system sleep for 1 second
            time.sleep(1)


GUIapp()
