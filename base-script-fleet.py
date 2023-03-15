from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import date_list
import pickup_list
import dropoff_list
from class_list import full_class_name_list, class_list
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import requests
import json
import datetime  
from datetime import datetime


url = 'https://dli.3wp.ru/fleet'

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=r'C:\\Users\\1395266\\Documents\\ChromeDriver\\chromedriver.exe')




# =========================  One Way ========================= 



driver.get(url)

# находим все кнопки на странице
buttons = driver.find_elements(By.NAME, "car_type")

# выбираем произвольную кнопку и кликаем на нее
random_button = random.choice(buttons)
driver.execute_script("arguments[0].click();", random_button)

# Рандомный индекс для дат
random_index_date = random.randrange(len(date_list.date_list))

# Рандомный индекс для Pickup
random_index_pickup = random.randrange(len(pickup_list.pickup_list))

# Рандомный индекс для dropoff
random_index_dropoff = random.randrange(len(dropoff_list.dropoff_list))

# # Заполняем данные
# driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/div[2]/div/input[2]').send_keys(pickup_list.pickup_list[random_index_pickup])
# driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/div[2]/div/input[3]').send_keys(dropoff_list.dropoff_list[random_index_dropoff])
date = driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/div[2]/div/input[4]')
inputDate = date_list.date_list[random_index_date]
# driver.execute_script(f"arguments[0].setAttribute('value', '{inputDate}')", date)
# oneWayButton = driver.find_element_by_name('submit_1_fleet')
# driver.execute_script("arguments[0].click();", oneWayButton)

# # step-2
# preDistance = driver.find_element_by_xpath("/html/body/div[3]/main/div/div/div/div[2]/div/p[2]/span")
# distance = preDistance.text.split(" ")[0]

# Задаем параметры
firstName = "Test First Name"
lastName = "Test Last Name"
umail = "test@test.com"
tel = '9999999999'
newDate = datetime.strptime(inputDate, "%Y-%m-%dT%H:%M")
finDate = newDate.strftime('%d.%m.%Y %H:%M')


# driver.find_element_by_name('first_name').send_keys(firstName)
# driver.find_element_by_name('last_name').send_keys(lastName)
# driver.find_element_by_name('umail').send_keys(umail)
# driver.find_element_by_name('tel').send_keys(tel)
# driver.find_element_by_name('step-button-new').click()

# # Запрашиваем данные созданного лида
# hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
# text = json.loads(hookData.text)

# if text['entity_status'] != "lead" or text['first_name'] != firstName or text['last_name'] != lastName or text['umail'] != umail or text['tel'] != tel or text['initial_km'] != distance or text['pickup'] != pickup_list.pickup_list[random_index_pickup] or text['dropoff'] != dropoff_list.dropoff_list[random_index_dropoff] or text['ride_date'] != finDate:
#     with open('errorLog.txt', 'a', encoding='utf-8') as err:
#         err.write('Неверные данные пришли на вебхук при создании лида. Step-2. Тип трансфера - One Way Fleet')





# # payments
# time.sleep(6)
# # Переключаемся на iframe
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

# # Заполняем данные
# driver.find_element_by_id('Field-numberInput').send_keys("4242424242424242")
# driver.find_element_by_id('Field-expiryInput').send_keys("01/33")
# driver.find_element_by_id('Field-cvcInput').send_keys("123")

# # Переключаемся обратно на основной контент
# driver.switch_to.default_content()


# payButton = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div[3]/div[2]/form/button')
# driver.execute_script("arguments[0].click();", payButton)

# time.sleep(3)

# # Проверяем, пришел ли Payment code в сделку
# hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
# text = json.loads(hookData.text)

# if text['payment_code'] == "0":
#     with open('errorLog.txt', 'a', encoding='utf-8') as err:
#         err.write('На вебхук не пришел Payment code. Success. Тип трансфера - One Way Fleet')



# =========================  Hourly ========================= 

# driver.get(url)

# # находим все кнопки на странице
# buttons = driver.find_elements(By.NAME, "car_type")

# # выбираем произвольную кнопку и кликаем на нее
# random_button = random.choice(buttons)
# driver.execute_script("arguments[0].click();", random_button)

# # Кликаем на вкладку Hourly
# driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/div[1]/div[2]').click()

# # Заполняем данные
# driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/div[3]/div/input[2]').send_keys(pickup_list.pickup_list[random_index_pickup])
# # duration = Select(driver.find_element_by_name('tab_2_duration'))
# # duration.select_by_value("8 hours")
# date = driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/div[3]/div/input[3]')
# inputDate = date_list.date_list[random_index_date]
# driver.execute_script(f"arguments[0].setAttribute('value', '{inputDate}')", date)
# driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/div[3]/div/button').click()

# duration = "2 hours"

# driver.find_element_by_name('first_name').send_keys(firstName)
# driver.find_element_by_name('last_name').send_keys(lastName)
# driver.find_element_by_name('umail').send_keys(umail)
# driver.find_element_by_name('tel').send_keys(tel)
# driver.find_element_by_name('step-button-new').click()

# # Запрашиваем данные созданного лида
# hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
# text = json.loads(hookData.text)

# if text['entity_status'] != "lead" or text['first_name'] != firstName or text['last_name'] != lastName or text['umail'] != umail or text['tel'] != tel or text['pickup'] != pickup_list.pickup_list[random_index_pickup] or text['duration'] != "2 hours" or text['ride_date'] != finDate:
#     with open('errorLog.txt', 'a', encoding='utf-8') as err:
#         err.write('Неверные данные пришли на вебхук при создании лида. Step-2. Тип трансфера - Hourly')


# # Запрашиваем данные сделки, созданной на основе лида
# hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
# text = json.loads(hookData.text)

# if text['entity_status'] != "deal":
#     with open('errorLog.txt', 'a', encoding='utf-8') as err:
#         err.write('Лид не стал сделкой. Step-3. Тип трансфера - Hourly')

# if text['car_type'] != full_class_name_list[random_index_class]:
#     with open('errorLog.txt', 'a', encoding='utf-8') as err:
#         err.write(f'Машина не корректно передалась (или вообще не передалась) на вебхук. Ожидалась машина "{full_class_name_list[random_index_class]}", а на вебхук пришло "{text["car_type"]}". Step-3. Тип трансфера - Hourly')




# # payments
# time.sleep(6)
# # Переключаемся на iframe
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

# # Заполняем данные
# driver.find_element_by_id('Field-numberInput').send_keys("4242424242424242")
# driver.find_element_by_id('Field-expiryInput').send_keys("01/33")
# driver.find_element_by_id('Field-cvcInput').send_keys("123")

# # Переключаемся обратно на основной контент
# driver.switch_to.default_content()


# payButton = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div[3]/div[2]/form/button')
# driver.execute_script("arguments[0].click();", payButton)

# time.sleep(3)

# # Проверяем, пришел ли Payment code в сделку
# hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
# text = json.loads(hookData.text)

# if text['payment_code'] == "0":
#     with open('errorLog.txt', 'a', encoding='utf-8') as err:
#         err.write('На вебхук не пришел Payment code. Success. Тип трансфера - Hourly')


# =========================  Tours  ========================= 


driver.get(url)

# находим все кнопки на странице
buttons = driver.find_elements(By.NAME, "car_type")

# выбираем произвольную кнопку и кликаем на нее
random_button = random.choice(buttons)
driver.execute_script("arguments[0].click();", random_button)

# Кликаем на вкладку Tours
driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/div[1]/div[3]').click()

# Заполняем данные
driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/div[4]/div/input[2]').send_keys(pickup_list.pickup_list[random_index_pickup])
driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/div[4]/div/textarea').send_keys("Test")
date = driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/div[4]/div/input[3]')
inputDate = date_list.date_list[random_index_date]
driver.execute_script(f"arguments[0].setAttribute('value', '{inputDate}')", date)
driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/div[4]/div/button').click()

# step-2


# Запрашиваем данные сделки, созданной на основе лида
hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
text = json.loads(hookData.text)

if text['entity_status'] != "deal":
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write('Лид не стал сделкой. Step-3. Тип трансфера - Tours Fleet')

if text['car_type'] != full_class_name_list[random_index_class]:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Машина не корректно передалась (или вообще не передалась) на вебхук. Ожидалась машина "{full_class_name_list[random_index_class]}", а на вебхук пришло "{text["car_type"]}". Step-3. Тип трансфера - Tours Fleet')



# Запрашиваем данные созданного лида
hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
text = json.loads(hookData.text)

if text['entity_status'] != "lead" or text['first_name'] != firstName or text['last_name'] != lastName or text['umail'] != umail or text['tel'] != tel or text['pickup'] != pickup_list.pickup_list[random_index_pickup] or text['ride_date'] != finDate:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write('Неверные данные пришли на вебхук при создании лида. Step-2. Тип трансфера - Tours')

# step-3

driver.find_element_by_name('first_name').send_keys(firstName)
driver.find_element_by_name('last_name').send_keys(lastName)
driver.find_element_by_name('umail').send_keys(umail)
driver.find_element_by_name('tel').send_keys(tel)
driver.find_element_by_name('step-button-new').click()


# payments
time.sleep(6)
# Переключаемся на iframe
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

# Заполняем данные
driver.find_element_by_id('Field-numberInput').send_keys("4242424242424242")
driver.find_element_by_id('Field-expiryInput').send_keys("01/33")
driver.find_element_by_id('Field-cvcInput').send_keys("123")

# Переключаемся обратно на основной контент
driver.switch_to.default_content()


payButton = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div[3]/div[2]/form/button')
driver.execute_script("arguments[0].click();", payButton)

time.sleep(3)

# Проверяем, пришел ли Payment code в сделку
hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
text = json.loads(hookData.text)

if text['payment_code'] == "0":
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write('На вебхук не пришел Payment code. Success. Тип трансфера - Tours')


# driver.quit()
