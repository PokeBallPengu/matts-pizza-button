from webbrowser import open as webopen
import tkinter
from random import randint

def pizzaMe():
	if randint(0, 9) == 0:
		webopen('https://www.amazon.com/treadmill-home-treadmill/b?ie=UTF8&node=3407831')
	else:
		webopen('https://www.dominos.com/en/pages/order/menu#!/menu/category/viewall/')

root = tkinter.Tk()
root.geometry('255x255')
root.title("Matt's Pizza Button")

root.resizable(height=0, width=0)
tkinter.Button(root, text="PIZZA\n", font=("Courier", 57), height=4, command=pizzaMe, bg='brown4', overrelief='groove', borderwidth=0, activebackground='brown4').grid()

root.mainloop()
