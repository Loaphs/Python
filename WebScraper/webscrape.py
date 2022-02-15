from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tkinter import *
from tkinter.ttk import *

import webbrowser

s=Service(ChromeDriverManager().install())
driver = wd.Chrome(service=s)
driver.get('https://realpython.github.io/fake-jobs/')

content = driver.page_source        
soup = bs(content, 'html.parser')

root = Tk()
root.title('JobSite')
root.geometry('900x600')

tabs_control = Notebook(root)
jobs_tab = Frame(tabs_control)
tabs_control.add(jobs_tab, text = 'Jobs Available')
tabs_control.pack(expand = 1, fill = "both")

scroll_bar = Scrollbar(jobs_tab)
scroll_bar.pack(side = RIGHT, fill = Y)

results = []
resultlinks = []

results_box = Listbox(jobs_tab, yscrollcommand = scroll_bar.set)

for element in soup.findAll(attrs={'class': 'card'}):
    name = element.find('h2')
    link = element.find('a', string = 'Apply')
    if name not in results:
        results.append(name.text)
        results_box.insert(END, name.text)
    if link not in resultlinks:
        resultlinks.append(link['href'])

def item_selected(event):
    selected_job = results_box.curselection()

    index = results_box.index(selected_job)

    webbrowser.open(resultlinks[index])

results_box.bind('<<ListboxSelect>>', item_selected)

results_box.pack(side = LEFT, expand = TRUE, fill = BOTH)

scroll_bar.config(command = results_box.yview)


root.mainloop()