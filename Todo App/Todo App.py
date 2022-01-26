from tkinter import *
from tkinter.ttk import *

#CREATE_WINDOW
window = Tk()
window.title("Todo App")
window.geometry("500x250")

#CREATE_TODO
def createItem():
    itemName = itemEntry.get()
    def destroyItem():
        return

    if itemName != '':
        itemButton = Button(window, command = destroyItem)
        itemButton.pack(setside = LEFT)
        itemLabel = Label(window, font = 'calibri 15', text = itemName)
        itemLabel.pack(setside = LEFT)
        itemEntry.delete(0, END)
    else:
        return

#CREATE_TEXT
titleLabel = Label(window, font = "calibra 30 bold", text = 'Todo List')
titleLabel.pack(anchor = 'n')

#ADD_TODO
itemEntry = Entry(window, font = 'calibri 15')
itemEntry.pack(anchor = 'center')
entryButton = Button(window, text = 'Create Item', command = createItem)
entryButton.pack(anchor = 'center')


window.mainloop()