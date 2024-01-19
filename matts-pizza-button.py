from webbrowser import open as webopen
import tkinter
from random import randint

def pizzaMe():
	if randint(0, 9) == 0:
		webopen('dominoes.com')
	else:
		webopen('dominoes.com')

root = tkinter.Tk()
root.geometry('255x255')
root.title("Matt's Pizza Button")

root.resizable(height=0, width=0)
tkinter.Button(root, text="PIZZA\n", font=("Courier", 57), height=4, command=pizzaMe, bg='brown4', overrelief='groove', borderwidth=0, activebackground='brown4').grid()

root.mainloop()