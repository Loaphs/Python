import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tkinter import *
from tkinter.ttk import *

s=Service(ChromeDriverManager().install())
driver = wd.Chrome(service=s)
driver.get('https://realpython.github.io/fake-jobs/')

results = []
content = driver.page_source
soup = bs(content, 'html.parser')

root = Tk()
root.title('JobSite')
root.geometry('900x600')

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

tabs_control = Notebook(root)
jobs_tab = Frame(tabs_control)
tabs_control.add(jobs_tab, text = 'Jobs Available')
tabs_control.pack(expand = 1, fill = "both")

for element in soup.findAll(attrs={'class': 'card'}):
    name = element.find('h2')
    if name not in results:
        results.append(name.text)
        item_label = Label(jobs_tab, font = 'calibri 15 bold', text = name.text)
        item_label.pack(anchor = 'n')


root.mainloop()