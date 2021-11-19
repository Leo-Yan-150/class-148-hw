from tkinter import *
import random

root=Tk()

root.title("Random Lists Generator")
root.geometry("600x400")
root.configure(background = 'snow')

items = Label(root, text = 'Cheese, Sandwhich, Water, Juice, Chocolate, Fruits, Snacks, Ham, Veggies, Ketchup')
random_number_list=Label(root)
itemlist = Label(root)

def randomlist():
    itemslist = ['Cheese', 'Sandwhich', 'Water', 'Juice', 'Chocolate', 'Fruits', 'Snacks', 'Ham', 'Veggies', 'Ketchup']
    randn = random.randint(0,9)
    random_number_list['text'] = "Put " + itemslist[randn] + " inside the bag"
    
btn = Button(root, text='Choose what to put in', command=randomlist)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

random_number_list.place(relx = 0.5, rely = 0.4, anchor = CENTER)
items.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()
