"""
This is the final code structure for the R2D2 project
Cornell Cup Robotics, Spring 2019
File Created by Yanchen Zhan '22 (yz366)
"""

### import respective packages
import sys
#import speech_recognition as sr
#import pyaudio
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sid
#from random import *
import simpleaudio as sa
import piimages_final
import client
import socket
import json
import time
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions, SentimentOptions
import retinasdk
#apiKey = "69ba0c10-5e17-11e9-8f72-af685da1b20e"
#apiKey = "f09d0fe0-3223-11e9-bb65-69ed2d3c7927" #FOR DEMO DAY ONLY
apiKey = "f8512d60-67b2-11e9-8f72-af685da1b20e"
liteClient = retinasdk.LiteClient(apiKey)

import threading
from threading import Lock, Thread
lock = Lock()
lock2 = Lock()

naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
version='2018-11-16',
iam_apikey='_wxBEgRMBJ_WzXRWYzlTLYrNp3A0mmYEjKp-UQsdhvap')

setup_bool = False
confirmation_final = 1000
no_clue_final = 999
wakeup_final = 998
sleep_final = 997
move_final = 996
attendance_final = 995
sentiment_value = 0
		
"""
listen to user statement in mic
returns spoken words from user OR 
returns empty string if source not detected
"""
def listen(r, mic):
	with mic as source:
		r.adjust_for_ambient_noise(source)
		print("\n\n\nYou may begin talking:\n\n\n") #testing
		audio = r.listen(source)

	try:
		return r.recognize_google(audio)

	except sr.UnknownValueError:
		print ("What are you saying?") #testing
		return ""


"""
plays respective sound from speakers
based on sentiment analysis value
"""
def react_with_sound (sentiment_value):
	
	print ("about to play sound...")
	
	lead_folder = "/home/pi/Desktop/r2-tablet_GUI/R2FinalSounds/"
	#lead_folder = "/home/yanchen-zhan/Documents/Cornell-Cup/r2-voice_recognition/Final/R2FinalSounds/"
	#lead_folder = "C:\PythonProjects\\r2-voice_recognition\Final\R2FinalSounds\\"
	sounds = {"confirmation":"R2OK.wav" , "wake up":"R2Awake.wav" , "angry":"R2Angry.wav" , "good":"R2Good.wav" , \
	"happy":"R2Happy.wav" , "neutral":"R2Neutral.wav" , "sad":"R2Sad.wav" , \
	"sleep":"R2Sleep.wav", "no clue":"R2Confused.wav" , "move":"R2Move.wav" , \
	"attendance":"R2Attendance.wav"}
	
	if (sentiment_value == confirmation_final):
		play_sound(lead_folder + sounds["confirmation"])
	elif (sentiment_value == no_clue_final):
		play_sound(lead_folder + sounds["no clue"])
	elif (sentiment_value == wakeup_final):
		play_sound(lead_folder + sounds["wake up"])
	elif (sentiment_value == sleep_final):
		play_sound(lead_folder + sounds["sleep"])
	elif (sentiment_value == move_final):
		play_sound(lead_folder + sounds["move"])
	elif (sentiment_value == attendance_final):
		play_sound(lead_folder + sounds["attendance"])
	elif (sentiment_value < -0.5):
		play_sound(lead_folder + sounds["angry"])
	elif (sentiment_value < 0):
		play_sound(lead_folder + sounds["sad"])
	elif (sentiment_value == 0):
		play_sound(lead_folder + sounds["neutral"])
	elif (sentiment_value > 0.5):
		play_sound(lead_folder + sounds["happy"])
	else:
		play_sound(lead_folder + sounds["good"])

### play sound from speakers
def play_sound(file_name):
	wave_obj = sa.WaveObject.from_wave_file(file_name)
	play_obj = wave_obj.play()
	play_obj.wait_done()

def stop():
	print ("emergency invoked")
	
	#start exit procedure here
	## begin by creating threads to send poweroff commands to each arduino asynchronously (if feasible)
	#t0 = threading.thread(target = shutdown, args = ("",))
	#t0.start()
	
	#t0.join()
	react_with_sound(sleep_final)
	sys.exit()
		
def wave(methodcnt): # NOTE - INSTANTIATE WITH SPECIAL CASE
	"""global setup_bool
	# initial bootup
	if (setup_bool == False or methodcnt == False):
		setup_bool = True
	else:"""
	print ("waving")
	#	react_with_sound(confirmation_final)
	return 0
	
def greet(methodcnt):
	"""global setup_bool
	if (setup_bool == False or methodcnt == False):
		setup_bool = True
	else:"""
	print ("greeting, don't forget to wave")
	wave(methodcnt)
	#	react_with_sound(confirmation_final)
	return 1

# have R2 take attendance
def take_attendance(methodcnt):
	"""global setup_bool
	if (setup_bool == False or methodcnt == False):
		print ("in if statement")
		setup_bool = True
	else:"""
	print ("checking in - F.R.")
	react_with_sound(attendance_final)
	client.CheckIn()	
	return 2

def make_friends(name):
    friend = name[len("my name is ")+1:] #index where the first name appears
    client.MakeFriends(friend)
    return 9

def grab_item(item, methodcnt):
	"""global setup_bool
	if (setup_bool == False or methodcnt == False):
		setup_bool = True"""
	if (item == "periscope"):
		open_periscope()
	elif (item == "nerf" or "gun" in item):
		show_guns()
	else:
		print ("grabbing " + item)
	#	react_with_sound (confirmation_final)
	return 3
	
def spit_info():
	print ("info spit")
	#react_with_sound (confirmation_final)
	return 4

def open_periscope():
	print ("opening periscope")
	#react_with_sound (confirmation_final)
	return 5
	
def show_guns():
	print ("showing off dem guns...")
	#react_with_sound (confirmation_final)
	return 6
	
#implement threading in here
#locks implemented to prevent any conflict in data retrieval
def writeToVoice(input):
	lock.acquire()
	file=open('VoiceRecognitionText.txt','w+')
	file.write(input + "\r\n")
	file.close()	
	lock.release()

def writeToSentiment(score):
	lock2.acquire()
	score1 = str(score)
	file=open('SentimentAnalysisOutput.txt','w+')
	file.write(score1 + "\r\n")
	file.close()	
	lock2.release()

def sentiment(input):
	try:				
		response = naturalLanguageUnderstanding.analyze(
		text=input,
		features=Features(
		sentiment=SentimentOptions(document=None, targets=None))).get_result()

		parsed_json = json.loads(json.dumps(response, indent=2))
		sentiment = parsed_json['sentiment']
		document = sentiment['document']
		score = document['score']
		sentiment_value = float(score)
			
	except:
		sentiment_value = sid().polarity_scores(input)['compound']
			
	print(sentiment_value)	
	react_with_sound(sentiment_value)
	return 7

def object_detection():
	piimages_final.main()
	return 8

def main():
	
	methodcnt = False
	
	#method dispatcher to connect to functions
	dispatcher = {'wave1':wave, 'greet1':greet, 'take_attendance1':take_attendance, 'grab_item1':grab_item}
	# https://www.reddit.com/r/Python/comments/7udbs1/using_python_dict_to_call_functions_based_on_user/
	
	#test run to see if all r2 functionality working as expected
	fndictGreetingsKeys = {"wave", "hello", "hi", "hey", "check", "attendance"}
	fndictGetItemsKeys = {"water", "bottle", "stickers", "periscope", "nerf", "guns", "gun"} # NEED TO CHECK SPELLING OF PERISCOPE FOR VOICE RECOGNITION
	
	#in formation of dictionaries, all functions being called
	fndictGreetings = {"wave":dispatcher['wave1'], "hello":dispatcher['greet1'], "hi":dispatcher['greet1'], "hey":dispatcher['greet1'], "check":dispatcher['take_attendance1'], "attendance":dispatcher['take_attendance1']}
	fndictGetItems = {"water":dispatcher['grab_item1'], "bottle":dispatcher['grab_item1'], "stickers":dispatcher['grab_item1'], "periscope":dispatcher['grab_item1'], "nerf":dispatcher['grab_item1'], "guns":dispatcher['grab_item1'], "gun":dispatcher['grab_item1']}
	methodcnt = True
	setup_bool = True
	
	### opens microphone instance that takes speech from human to convert to text
	#r = sr.Recognizer()
	#mic = sr.Microphone(2)

	# tells R2 to wake up
	while (True):
		spoken_text = input("enter 'hey r2' to start: ")
		#spoken_text = listen(r, mic)
		#spoken_text = spoken_text.lower()
		print("The following startup phrase was said:\n" + spoken_text + "\n")
		
		# R2 unsure of input
		if (spoken_text == ""):
			print ("What?")
			react_with_sound(no_clue_final)
		
		elif ("r2 stop" in spoken_text):
			#write(spoken_text)
			stop()
		
		elif ("hey r2" in spoken_text):
			print ("awake")
			react_with_sound(wakeup_final)
			break			
	
	# R2 waits to hear what user wants - CHANGE PROMPTS HERE
	while (True):
		
		spoken = input("enter command or sentence: ")
		#spoken = simplify_text(listen (r, mic))
		#spoken = spoken.lower()
		print("The following text was said:\n" + spoken + "\n")
		
		if ("r2 stop" in spoken):
			#write(spoken_text)
			stop()
		
		# R2 unsure of input
		elif (spoken == ""):
			print ("What?")
			react_with_sound(no_clue_final)
		
		elif ("what do you see" in spoken):
			object_detection()
		
		else: 
			#use NLTK to determine part of speech of first word spoken
			tokens = nltk.word_tokenize (spoken)
			tagged = nltk.pos_tag(tokens)
			print (tagged[0])
			
			keywords = liteClient.getKeywords(spoken)
					
			#if question desired about Cornell Cup
			if ("cup" in keywords and "cornell" in keywords or "competition" in keywords):
				spit_info()
				
			#run through commands first
			elif ("wave" in spoken or "high five" in spoken or "VB" in tagged[0] or "JJ" in tagged[0]):
				
				if ("high five" in spoken):
					keywords.append("high five")
					
				else:
					for x in range(0, len(keywords)):
							
						word = keywords[x]
						print (word)
							
						react_with_sound (confirmation_final)
								
						if (word in fndictGreetingsKeys):	
							print(fndictGreetings[word](methodcnt))
							print ("in fndictGreetingKeys")
							break
						
						elif (word in fndictGetItemsKeys):
							print(fndictGetItems[word](word, methodcnt))
							print ("in fndictGetItemsKey")
							break
			
			else:				
				#sentiment analysis
				try:				
					global sentiment_value
					response = naturalLanguageUnderstanding.analyze(
					text=spoken,
					features=Features(
					sentiment=SentimentOptions(document=None, targets=None))).get_result()

					parsed_json = json.loads(json.dumps(response, indent=2))
					sentiment = parsed_json['sentiment']
					document = sentiment['document']
					score = document['score']
					sentiment_value = float(score)
					
				except:
					sentiment_value = sid().polarity_scores(spoken)['compound']
				
					
				print(sentiment_value)	
				react_with_sound(sentiment_value)
		
		t1 = threading.Thread(target = writeToVoice, args=(spoken,))
		t2 = threading.Thread(target = writeToSentiment, args=(sentiment_value,))
		t1.start()
		t2.start()
		t1.join()
		t2.join()
			
main()

#multithreading plan: add locks to prevent GUI program from accessing text file data too quickly while the text file is writing
#create a new thread for this process
