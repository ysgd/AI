import pyttsx3
import speech_recognition as sr
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def greetings():
	time = int(datetime.datetime.now().hour)
	if time>0 and time<12:
		speak("Good Morning!!")

	elif time>=12 and time<18:
		speak("Good Afternoon!!")

	else:
		speak("Good Evening!!")

	
	speak("How may I help you?")

def Command():
	r = sr.Recognizer()

	
	

	try:
		print("recognizing...")
		query = r.recognize_google(audio, language='en')
		print(query)

	except Exception as e:
		print("can't hear you..")
		
	return query




if __name__ == '__main__':
	greetings()
	Command()

