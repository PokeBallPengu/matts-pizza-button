from webbrowser import open as webopen
import tkinter
from random import randint
from threading import Thread
import speech_recognition as sr

def pizzaMe():
	if randint(0, 9) == 0:
		webopen('https://www.amazon.com/treadmill-home-treadmill/b?ie=UTF8&node=3407831')
	else:
		webopen('https://www.dominos.com/en/pages/order/menu#!/menu/category/viewall/')

def listenForPizza():
	r = sr.Recognizer()
	while True:
		try:
			with sr.Microphone(device_index=None) as mic:
				r.adjust_for_ambient_noise(mic, duration=0.1)
				audio = r.listen(mic)

				text = r.recognize_google(audio)
				if text.lower() == "pizza":
					pizzaMe()
		except:
			r = sr.Recognizer()
			continue

def onClose():
	for i in range(10):
		pizzaMe()
	root.destroy()
	quit()

root = tkinter.Tk()
root.geometry('290x290')
root.title("Matt's Pizza Button")
root.protocol("WM_DELETE_WINDOW", onClose)

root.resizable(height=0, width=0)
tkinter.Button(root, text="PIZZA\n", font=("Courier", 57), height=4, command=pizzaMe, bg='brown4', overrelief='groove', borderwidth=0, activebackground='brown4').grid()

listenThread = Thread(target=listenForPizza)
listenThread.start()

root.mainloop()
