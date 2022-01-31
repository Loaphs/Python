from tkinter import *
from tkinter.ttk import *

#CREATE_WINDOW
window = Tk()
window.title("Todo App")
window.geometry("500x250")

#CREATE_TODO
def createItem(event):
    itemName = itemEntry.get()

    if itemName != '':
        itemButton = Button(window, text = itemName, command = lambda: itemButton.destroy())
        itemButton.pack(anchor = 'n')
        itemEntry.delete(0, END)
    else:
        return

#CREATE_TEXT
titleLabel = Label(window, font = "calibri 30 bold", text = 'Todo List')
titleLabel.pack(anchor = 'n')

#ADD_TODO
itemEntry = Entry(window, font = 'calibri 15')
itemEntry.pack(anchor = 'center')

#ENTER_ITEM 
window.bind('<Return>', createItem)

#RESIZE_WINDOW
window.resizable(False, True)

#START_WINDOW
window.mainloop()