import tkinterGUI
import voiceRecognition
import threading

class main_program():

	def __init__(self):
		voice_thread = threading.Thread(target = voiceRecognition.main, args = "")
		gui_thread = threading.Thread(target = tkinterGUI.GUIapp, args = "")
		
		print ("stahting")
		voice_thread.start()
		print ("between statements")
		gui_thread.start()
		
		print ("in between")
		
		#voice_thread.join()
		#print ("ending statements")
		#gui_thread.join()
		

main_program()
