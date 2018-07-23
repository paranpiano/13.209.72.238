from selenium import webdriver


#browser = webdriver.Chrome('../driver/chromedriver.exe')
print('test started')
browser = webdriver.Firefox(executable_path = '..\webDriver_FireFox\geckodriver.exe')
#driver = webdriver.Firefox()
browser.get('http://localhost:8000')


assert 'Django' in browser.title