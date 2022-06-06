# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# s = Service('E:\Alex\Downloads\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
#
# driver.get("https://www.python.org/")
#
# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
#
# events_calendar = {}
#
# for n in range(len(event_times)):
#     events_calendar[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }
#
# print(events_calendar)
#
#
