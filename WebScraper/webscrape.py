import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd

driver = wd.Chrome(executable_path = 'D:\Loaphs\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://https://realpython.github.io/fake-jobs/')

results = []