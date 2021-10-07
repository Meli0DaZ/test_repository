from selenium import webdriver

PATH = "msedgedriver.exe"
url = 'http://45.79.43.178/source_carts/wordpress/wp-admin'

driver = webdriver.Edge(PATH)

driver.get(url)