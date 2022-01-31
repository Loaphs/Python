import requests
from tkinter import *
from tkinter.ttk import *

class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        scrollbar = Scrollbar(self, orient = 'vertical', command = canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox('all')))

        canvas.create_window((0, 0), window = self.scrollable_frame, anchor = 'nw')

        canvas.configure(yscrollcommand = scrollbar.set)

        canvas.pack(side = 'left', fill = 'both', expand = True)
        scrollbar.pack(side = 'right', fill = 'y')

root = Tk()
root.title('Web Scraper')
root.geometry('600x300')

frame = ScrollableFrame(root)

url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)

htmlRead = Label(frame.scrollable_frame, font = 'calibri 9', text = page.text)
htmlRead.pack()

print(page.text)

frame.pack()
root.mainloop()