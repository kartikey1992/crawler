__author__ = 'kartikey'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from quicker.models import *
from pyvirtualdisplay import Display
from .views import get_company_location,save_data
from celery.task import task


@task(ignore_result=True)
def crawl_quicker(url):
    driver = webdriver.Firefox()
    driver.get(url)
    car_hover_elements = driver.find_elements_by_css_selector('table.fixed.breakword')
    for element in car_hover_elements:
        a_element = element.find_element_by_css_selector('a.marginright5.link.linkWithHash.detailsLink')
        car_link = a_element.get_attribute("href")
        car_description = a_element.find_element_by_tag_name("span").get_attribute("innerHTML").replace(' ','')
        car_company = element.find_element_by_css_selector("p.color-9.lheight14.margintop3").find_element_by_tag_name("small").get_attribute("innerHTML")
        car_company,car_location = get_company_location(car_company)
        car_price = element.find_element_by_css_selector("p.price.x-large.margintop10").find_element_by_tag_name("strong").get_attribute("innerHTML").replace(' ','')
        save_data(car_link,car_description,car_company,car_price,car_location)
    driver.close()



