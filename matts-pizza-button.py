from webbrowser import open as webopen
import tkinter
from random import randint
from threading import Thread
import speech_recognition as sr
from time import sleep
from plyer import notification

def pizzaMe():
    if randint(0, 9) == 0:
        webopen('https://www.amazon.com/treadmill-home-treadmill/b?ie=UTF8&node=3407831')
    else:
        webopen('https://www.dominos.com/en/pages/order/menu#!/menu/category/viewall/')

def sendReminder(remTitle, remMessage):
    notification.notify(
                title = remTitle,
                message = remMessage,
                app_icon = 'images/icon.ico',
                timeout = 20,
            )

def pizzaReminder():
    while True:
        if randint(0, 9) == 0:
            sendReminder('Pizza Reminder', 'Eat Pizza')
        sleep(20)

def pizzaJokeReminder():
    pizzaJokes = [["What do you call a pizza that doesn't share?", "Selfish"], ["How did the pizza get in shape?", "Lots of crunches"], ["Why was the pizza late to work?", "It overslept"], ["Why was the pizza embarrassed?", "It had a little SAUSAGE showing!"], ["How do you fix a broken pizza?", "With tomato paste"], ["What did the pizza say to the spatula?", "You're flipping me out!"], ["What did the green pepper say to the pizza?", "You're looking hot tonight!"], ["Why did the customer send the pizza back?", "It wasn't DELI-VERING what she wanted! "], ["What do you call a pizza who is a master of martial arts?", "A ninja turtles pizza"], ["What do you call a sleeping pizza?", "Pizza ZZZ"], ["Why was the pizza so exhausted?", "It was filled with energy and ready for a NAP-olitan."], ["Why did the pizza cross the road?", "To get to the other side!"],["How did the pizza win the spelling bee?", "It knew the right ingredients."], ["What did one pizza say to the other?", "You look so cheesy today."], ["How does an Italian chef know the pizza is ready?", "Timer is up and the cheese is melted." ], ["What do you call a pizza that makes you laugh?", "Lolzzarella!"], ["How do pizzas travel?", "On their bikes - the pizza cycle"], ["What do you call a pizza that makes you laugh?", "LOLzzarella!"], ["Why couldn't the pizza pay her rent?", "She was short on dough."], ["What did the green pepper say to the pizza?", "Hey, you're looking hot!"], ["Why don't eggs tell pizza jokes?", "They'd crack each other up."], ["What's a pizza's favorite karate move?", "Pizza punch!"], ["Why did Patsy decline a second piece of pizza?", "She was already full!"], ["How did the Italian baker improve his pizza recipe?", "He refined the dough."], ["What happens when two pizza slices get into an argument?", "They exchange heated words!"], ["How do you keep a pizza warm?", "Bake it a jacket."], ["Why was the pizza shy?", "It lacked self-con-feta-dence!"], ["What did the pizza say when it was denied dessert?", "No pie for me?!" ], ["How does a pizza introduce itself?", "Slice to meet you!"], ["Why couldn't the pizza cross the road?", "It wasn't DELI-VERABLE!"], ["What did one topping say to the other?", "There's not mushroom on this pizza!"], ["Why do pizzas make great detectives?", "They know how to follow the clues-tons."], ["How did the pizza win the superbowl?", "It passed the final proof!"], ["Why did the customer send her pizza back to the kitchen?", "It wasn't what she oregano-ly ordered."], ["Why are pizzas so popular?", "They have a lot of fans!"], ["What do you call a pizza that plays guitar?", "Axi Rose special"], ["Why did the pizza roll?", "It wanted a spin."]]
    while True:
        if randint(0, 14) == 0:
            jokePick = randint(0, len(pizzaJokes) - 1)
            sendReminder(pizzaJokes[jokePick][0], pizzaJokes[jokePick][1])
            time.sleep(time.sleep(20))

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
root.iconbitmap("images/icon.ico")

root.resizable(height=0, width=0)
tkinter.Button(root, text="PIZZA\n", font=("Courier", 57), height=4, command=pizzaMe, bg='brown4', overrelief='groove', borderwidth=0, activebackground='brown4').grid()

listenThread = Thread(target=listenForPizza)
listenThread.start()

reminderThread = Thread(target=pizzaReminder)
reminderThread.start()

jokesThread = Thread(target=pizzaJokeReminder)
jokesThread.start()

# Send greeting message
sendReminder("Matt's Pizza Button", 'Press the button or say "pizza" for pizza.')

root.mainloop()
