import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('JobSite')
root.geometry('500x250')

tabs_control = Notebook(root)
jobs_tab = Frame(tabs_control)
tabs_control.add(jobs_tab, text = 'Jobs Available')

driver = wd.Chrome(executable_path = 'C:\\Users\\Levi\\Documents\\ChromeDriver\\chromedriver.exe')
driver.get('https://realpython.github.io/fake-jobs/')

results = []
content = driver.page_source
soup = bs(content)

for element in soup.findAll(attrs={'class': 'card'}):
    name = element.find('h2')
    if name not in results:
        results.append(name.text)
        item_label = Label(jobs_tab, font = 'calibri 15 bold', text = name.text)
        item_label.pack(anchor = 'n')


root.mainloop