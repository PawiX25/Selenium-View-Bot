from selenium import webdriver
import time

driver = webdriver.Firefox()
url = input('URL: ')

x = 1

for x in range(int(input('Number of visits: '))):
    driver.get(url)