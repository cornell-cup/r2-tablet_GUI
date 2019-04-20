from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
from tkinter import font
import threading
import time


class GUIapp():

    def save_info(self):
        m = self.entry1.get()
        print(m)
        with open('txt.txt', 'a') as the_file:
            the_file.write(m + '\n')
        self.clear_text()

    def clear_text(self):
        self.entry1.delete(0, 'end')

    def __init__(self):
        self.i = 0
        root = Tk()
        root.geometry("750x450")
        root.attributes('-fullscreen', True)
        self.note = ttk.Notebook(root)

        self.tab1 = ttk.Frame(self.note)
        self.tab2 = ttk.Frame(self.note)
        self.tab3 = ttk.Frame(self.note)
        self.tab4 = ttk.Frame(self.note)
        self.quitButton = ttk.Button(self.note, text="Quit the program", command=quit)

        # tab 1 information : General Info
        info = "The original R2D2 Project focused upon creating a semi-autonomous \n " \
               "lab assistant that could navigate and map out its surrounding \n" \
               "environment. Since last year, the team has expanded upon R2’s ability \n " \
               "to interact with its surroundings enabling the droid to complete tasks \n" \
               " such as getting food from a fridge, opening a door, recognizing and \n " \
               "greeting individual people, and even firing a nerf dart at a target. \n" \
               "To generate excitement and interest in robotics and engineering, \n" \
               "the team aims to advertise the R2 project and \n" \
               "generate interest in its design process through a Kickstarter campaign. \n" \
               "This hopefully will work toward the long-term goal of \n" \
               "having our R2 robot appear in a Star Wars movie."
        text = Label(self.tab1, text=info, width=60)
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

        # create a thread to constantly update the text in the streaming tab
        thread1 = threading.Thread(target=self.update_stream_text)
        thread1.start()

        # tab 4 information : Sign up
        self.text = Label(self.tab4, text="Enter your Email here", font=("Courier", 20))
        self.text.pack(side=LEFT)
        self.entry1 = Entry(self.tab4)
        self.text.grid(row=0, sticky=W)
        self.entry1.grid(row=0, column=1)
        b = Button(self.tab4, text="OK", command=self.save_info, height = 5, width = 5)
        b.grid(row=3, sticky=S)

        self.note.add(self.tab1, text="General Info")
        self.note.add(self.tab2, text="Visual Img")
        self.note.add(self.tab3, text="Data Streaming")
        self.note.add(self.tab4, text="Sign up")
        self.note.add(self.quitButton, text="For Staff Only")
        self.note.pack()

        root.mainloop()

    # update the text in the streaming tab once a second
    def update_stream_text(self):
        while 1:
            # update the text
            VoiceRecognitionText = open('VoiceRecognitionText.txt', 'r').read()
            SentimentAnalysisOutput = open('SentimentAnalysisOutput.txt', 'r').read()
            FacialRecognitionResult = open('FacialRecognitionResult.txt', 'r').read()
            ObjectDetectionResult = open('ObjectDetectionResult.txt', 'r').read()
            self.data1['text'] = VoiceRecognitionText
            self.data2['text'] = SentimentAnalysisOutput
            self.data4['text'] = FacialRecognitionResult
            self.data5['text'] = ObjectDetectionResult

            Facial_Recognition_Photo_path = "cropped.jpg"
            img = Image.open(Facial_Recognition_Photo_path)
            img = img.resize((180, 180), Image.ANTIALIAS)
            Facial_Recognition_Photo_img = ImageTk.PhotoImage(img)
            # update the photo
            self.data3['image'] = Facial_Recognition_Photo_img
            self.tab3.update()
            # make the system sleep for 1 second
            time.sleep(1)


GUIapp()
