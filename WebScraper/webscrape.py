import pandas as pd
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

results_box = Listbox(jobs_tab, yscrollcommand = scroll_bar.set)

for element in soup.findAll(attrs={'class': 'card'}):
    name = element.find('h2')
    link = element.find('a')
    print(link)
    if name not in results:
        results_box.insert(END, name.text)
    for item in link:
        if link.text == 'Apply':
                results.append(link.href)

def item_selected(event):
    selected_job = results_box.curselection()

    index = results_box.index(selected_job)

    print(results)
    #webbrowser.open(results[index])

results_box.bind('<<ListboxSelect>>', item_selected)

df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index = FALSE, encoding = 'utf-8')

results_box.pack(side = LEFT, expand = TRUE, fill = BOTH)

scroll_bar.config(command = results_box.yview)


root.mainloop()