__author__ = 'kartikey'
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawler.settings")
django.setup()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from quicker.models import *
from pyvirtualdisplay import Display
from quicker.tasks import crawl_quicker

def get_pages():
    count = 1
    base_url = "http://www.olx.in/cars/"
    crawl_quicker.delay(base_url)
    while count <= 2:
        url = base_url + '?page='+ str(count)
        crawl_quicker.delay(url)
        count += 1
        print count

if __name__=='__main__':
 get_pages()