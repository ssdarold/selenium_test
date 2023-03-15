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
import requests
import json
import datetime  
from datetime import datetime


url = 'https://dli.3wp.ru/'

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=r'C:\\Users\\1395266\\Documents\\ChromeDriver\\chromedriver.exe')




# =========================  One Way ========================= 



driver.get(url)

# Рандомный индекс для дат
random_index_date = random.randrange(len(date_list.date_list))

# Рандомный индекс для Pickup
random_index_pickup = random.randrange(len(pickup_list.pickup_list))

# Рандомный индекс для dropoff
random_index_dropoff = random.randrange(len(dropoff_list.dropoff_list))

# Заполняем данные
driver.find_element_by_name('tab_1_pickup').send_keys(pickup_list.pickup_list[random_index_pickup])
driver.find_element_by_name('tab_1_dropoff').send_keys(dropoff_list.dropoff_list[random_index_dropoff])
date = driver.find_element_by_name('tab_1_datetime')
inputDate = date_list.date_list[random_index_date]
driver.execute_script(f"arguments[0].setAttribute('value', '{inputDate}')", date)
driver.find_element_by_name('submit_1').click()

# step-2
preDistance = driver.find_element_by_xpath("/html/body/div[3]/main/div/div/div/div[2]/div/p[2]/span")
distance = preDistance.text.split(" ")[0]

# Задаем параметры
firstName = "Test First Name"
lastName = "Test Last Name"
umail = "test@test.com"
tel = '9999999999'
newDate = datetime.strptime(inputDate, "%Y-%m-%dT%H:%M")
finDate = newDate.strftime('%d.%m.%Y %H:%M')


driver.find_element_by_name('first_name').send_keys(firstName)
driver.find_element_by_name('last_name').send_keys(lastName)
driver.find_element_by_name('umail').send_keys(umail)
driver.find_element_by_name('tel').send_keys(tel)
driver.find_element_by_name('step-button-new').click()

# Запрашиваем данные созданного лида
hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
text = json.loads(hookData.text)

if text['entity_status'] != "lead" or text['first_name'] != firstName or text['last_name'] != lastName or text['umail'] != umail or text['tel'] != tel or text['initial_km'] != distance or text['pickup'] != pickup_list.pickup_list[random_index_pickup] or text['dropoff'] != dropoff_list.dropoff_list[random_index_dropoff] or text['ride_date'] != finDate:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write('Неверные данные пришли на вебхук при создании лида. Step-2. Тип трансфера - One Way')

# step-3

# Сначала проверяем цены

# Цена для eclass
eclassPrice = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/div[3]/form/div[2]/div[3]/p')
itogPriceE = eclassPrice.text.split(" ")[0]

response = requests.get(f'https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/getRemotePrice.php?type=oneway&class=eclass&distance={distance}&inputDate={inputDate}')
# print(f'Eclass site price: {response.text} || Eclass calc price: {itogPriceE}')

if response.text != itogPriceE:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Цены для Eclass не совпадают. Цена на сайте: {itogPriceE}, правильная цена: {response.text}. Дата: {inputDate}, дистанция: {distance}. Тип трансфера - One Way')

# Цена для vclass
vclassPrice = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/div[4]/form/div[2]/div[3]/p')
itogPriceV = vclassPrice.text.split(" ")[0]

response = requests.get(f'https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/getRemotePrice.php?type=oneway&class=vclass&distance={distance}&inputDate={inputDate}')
# print(f'Vclass site price: {response.text} || Vclass calc price: {itogPriceV}')

if response.text != itogPriceV:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Цены для Vclass не совпадают. Цена на сайте: {itogPriceV}, правильная цена: {response.text}. Дата: {inputDate}, дистанция: {distance}. Тип трансфера - One Way')

# Цена для Sprinter
sprinterPrice = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/div[5]/form/div[2]/div[3]/p')
itogPriceSprinter = sprinterPrice.text.split(" ")[0]

response = requests.get(f'https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/getRemotePrice.php?type=oneway&class=sprinter&distance={distance}&inputDate={inputDate}')
print(f'Sprinter site price: {response.text} || Sprinter calc price: {itogPriceSprinter}')

if response.text != itogPriceSprinter:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Цены для Sprinter не совпадают. Цена на сайте: {itogPriceSprinter}, правильная цена: {response.text}. Дата: {inputDate}, дистанция: {distance}. Тип трансфера - One Way')

# Цена для sclass
sclassPrice = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/div[6]/form/div[2]/div[3]/p')
itogPriceS = sclassPrice.text.split(" ")[0]

response = requests.get(f'https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/getRemotePrice.php?type=oneway&class=sclass&distance={distance}&inputDate={inputDate}')
print(f'Sclass site price: {response.text} || Sclass calc price: {itogPriceS}')

if response.text != itogPriceS:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Цены для Sclass не совпадают. Цена на сайте: {itogPriceS}, правильная цена: {response.text}. Дата: {inputDate}, дистанция: {distance}. Тип трансфера - One Way')

# Цена для glsclass
glsclassPrice = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/div[7]/form/div[2]/div[3]/p')
itogPriceGLS = glsclassPrice.text.split(" ")[0]

response = requests.get(f'https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/getRemotePrice.php?type=oneway&class=glsclass&distance={distance}&inputDate={inputDate}')
print(f'GLSclass site price: {response.text} || GLSclass calc price: {itogPriceGLS}')

if response.text != itogPriceGLS:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Цены для GLSclass не совпадают. Цена на сайте: {itogPriceGLS}, правильная цена: {response.text}. Дата: {inputDate}, дистанция: {distance}. Тип трансфера - One Way')

# Цена для sprinter Long
sprinterLongPrice = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/div[8]/form/div[2]/div[3]/p')
itogPriceSLong = sprinterLongPrice.text.split(" ")[0]

response = requests.get(f'https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/getRemotePrice.php?type=oneway&class=slong&distance={distance}&inputDate={inputDate}')
print(f'Sprinter Long site price: {response.text} || Sprinter Long calc price: {itogPriceSLong}')

if response.text != itogPriceSLong:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Цены для Sprinter Long не совпадают. Цена на сайте: {itogPriceSLong}, правильная цена: {response.text}. Дата: {inputDate}, дистанция: {distance}. Тип трансфера - One Way')

# Выбираем рандомно машину
random_index_class = random.randrange(len(class_list))
choosenClass = class_list[random_index_class]
step3Button = driver.find_element_by_id(f'{choosenClass}-button')
driver.execute_script("arguments[0].click();", step3Button)

# Запрашиваем данные сделки, созданной на основе лида
hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
text = json.loads(hookData.text)

if text['entity_status'] != "deal":
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write('Лид не стал сделкой. Step-3. Тип трансфера - One Way')

if text['car_type'] != full_class_name_list[random_index_class]:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Машина не корректно передалась (или вообще не передалась) на вебхук. Ожидалась машина "{full_class_name_list[random_index_class]}", а на вебхук пришло "{text["car_type"]}". Step-3. Тип трансфера - One Way')




# payments
time.sleep(3)

driver.back()

# Получение случайного индекса, отличного от предыдущего
while True:
    second_index = random.randrange(len(class_list))
    if second_index != random_index_class:
        break

secondChoosenClass = class_list[second_index]
secondStep3Button = driver.find_element_by_id(f'{secondChoosenClass}-button')
driver.execute_script("arguments[0].click();", secondStep3Button)

# =========================  Hourly ========================= 

driver.get(url)

driver.find_element_by_class_name('active-hourly').click()

# Заполняем данные
driver.find_element_by_name('tab_2_pickup').send_keys(pickup_list.pickup_list[random_index_pickup])
# duration = Select(driver.find_element_by_name('tab_2_duration'))
# duration.select_by_value("8 hours")
date = driver.find_element_by_name('tab_2_datetime')
inputDate = date_list.date_list[random_index_date]
driver.execute_script(f"arguments[0].setAttribute('value', '{inputDate}')", date)
driver.find_element_by_name('submit_2').click()

duration = "2 hours"

driver.find_element_by_name('first_name').send_keys(firstName)
driver.find_element_by_name('last_name').send_keys(lastName)
driver.find_element_by_name('umail').send_keys(umail)
driver.find_element_by_name('tel').send_keys(tel)
driver.find_element_by_name('step-button-new').click()

# Запрашиваем данные созданного лида
hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
text = json.loads(hookData.text)

if text['entity_status'] != "lead" or text['first_name'] != firstName or text['last_name'] != lastName or text['umail'] != umail or text['tel'] != tel or text['pickup'] != pickup_list.pickup_list[random_index_pickup] or text['duration'] != "2 hours" or text['ride_date'] != finDate:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write('Неверные данные пришли на вебхук при создании лида. Step-2. Тип трансфера - Hourly')

# step-3

# Сначала проверяем цены

# Цена для eclass
eclassPrice = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/div[4]/form/div[2]/div[3]/p')
itogPriceE = eclassPrice.text.split(" ")[0]

response = requests.get(f'https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/getRemotePrice.php?type=hourly&class=eclass&distance={distance}&inputDate={inputDate}')
# print(f'Eclass site price: {response.text} || Eclass calc price: {itogPriceE}')

if response.text != itogPriceE:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Цены для Eclass не совпадают. Цена на сайте: {itogPriceE}, правильная цена: {response.text}. Дата: {inputDate}, продолжительность: {duration}. Тип трансфера - Hourly')

# Цена для vclass
vclassPrice = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/div[4]/form/div[2]/div[3]/p')
itogPriceV = vclassPrice.text.split(" ")[0]

response = requests.get(f'https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/getRemotePrice.php?type=hourly&class=vclass&distance={distance}&inputDate={inputDate}')
# print(f'Vclass site price: {response.text} || Vclass calc price: {itogPriceV}')

if response.text != itogPriceV:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Цены для Vclass не совпадают. Цена на сайте: {itogPriceV}, правильная цена: {response.text}. Дата: {inputDate}, продолжительность: {duration}. Тип трансфера - Hourly')

# Цена для Sprinter
sprinterPrice = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/div[5]/form/div[2]/div[3]/p')
itogPriceSprinter = sprinterPrice.text.split(" ")[0]

response = requests.get(f'https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/getRemotePrice.php?type=hourly&class=sprinter&distance={distance}&inputDate={inputDate}')
print(f'Sprinter site price: {response.text} || Sprinter calc price: {itogPriceSprinter}')

if response.text != itogPriceSprinter:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Цены для Sprinter не совпадают. Цена на сайте: {itogPriceSprinter}, правильная цена: {response.text}. Дата: {inputDate}, продолжительность: {duration}. Тип трансфера - Hourly')

# Цена для sclass
sclassPrice = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/div[6]/form/div[2]/div[3]/p')
itogPriceS = sclassPrice.text.split(" ")[0]

response = requests.get(f'https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/getRemotePrice.php?type=hourly&class=sclass&distance={distance}&inputDate={inputDate}')
print(f'Sclass site price: {response.text} || Sclass calc price: {itogPriceS}')

if response.text != itogPriceS:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Цены для Sclass не совпадают. Цена на сайте: {itogPriceS}, правильная цена: {response.text}. Дата: {inputDate}, продолжительность: {duration}. Тип трансфера - Hourly')

# Цена для glsclass
glsclassPrice = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/div[7]/form/div[2]/div[3]/p')
itogPriceGLS = glsclassPrice.text.split(" ")[0]

response = requests.get(f'https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/getRemotePrice.php?type=hourly&class=glsclass&distance={distance}&inputDate={inputDate}')
print(f'GLSclass site price: {response.text} || GLSclass calc price: {itogPriceGLS}')

if response.text != itogPriceGLS:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Цены для GLSclass не совпадают. Цена на сайте: {itogPriceGLS}, правильная цена: {response.text}. Дата: {inputDate}, продолжительность: {duration}. Тип трансфера - Hourly')

# Цена для sprinter Long
sprinterLongPrice = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/div[8]/form/div[2]/div[3]/p')
itogPriceSLong = sprinterLongPrice.text.split(" ")[0]

response = requests.get(f'https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/getRemotePrice.php?type=hourly&class=slong&distance={distance}&inputDate={inputDate}')
print(f'Sprinter Long site price: {response.text} || Sprinter Long calc price: {itogPriceSLong}')

if response.text != itogPriceSLong:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Цены для Sprinter Long не совпадают. Цена на сайте: {itogPriceSLong}, правильная цена: {response.text}. Дата: {inputDate}, продолжительность: {duration}. Тип трансфера - Hourly')


# Выбираем рандомно машину
random_index_class = random.randrange(len(class_list))
choosenClass = class_list[random_index_class]
step3Button = driver.find_element_by_id(f'{choosenClass}-button')
driver.execute_script("arguments[0].click();", step3Button)

# Запрашиваем данные сделки, созданной на основе лида
hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
text = json.loads(hookData.text)

if text['entity_status'] != "deal":
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write('Лид не стал сделкой. Step-3. Тип трансфера - Hourly')

if text['car_type'] != full_class_name_list[random_index_class]:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Машина не корректно передалась (или вообще не передалась) на вебхук. Ожидалась машина "{full_class_name_list[random_index_class]}", а на вебхук пришло "{text["car_type"]}". Step-3. Тип трансфера - Hourly')




# payments
time.sleep(6)

driver.back()

# Получение случайного индекса, отличного от предыдущего
while True:
    second_index = random.randrange(len(class_list))
    if second_index != random_index_class:
        break

secondChoosenClass = class_list[second_index]
secondStep3Button = driver.find_element_by_id(f'{secondChoosenClass}-button')
driver.execute_script("arguments[0].click();", secondStep3Button)


# =========================  Tours  ========================= 


driver.get(url)

driver.find_element_by_class_name('active-tours').click()

# Заполняем данные
driver.find_element_by_name('tab_3_pickup').send_keys(pickup_list.pickup_list[random_index_pickup])
driver.find_element_by_name('tab_3_requirements').send_keys("Test")
date = driver.find_element_by_name('tab_3_datetime')
inputDate = date_list.date_list[random_index_date]
driver.execute_script(f"arguments[0].setAttribute('value', '{inputDate}')", date)
driver.find_element_by_name('submit_3').click()

# step-2


# Выбираем рандомно машину
random_index_class = random.randrange(len(class_list))
choosenClass = class_list[random_index_class]
step3Button = driver.find_element_by_id(f'{choosenClass}-button')
driver.execute_script("arguments[0].click();", step3Button)

# Запрашиваем данные сделки, созданной на основе лида
hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
text = json.loads(hookData.text)

if text['entity_status'] != "deal":
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write('Лид не стал сделкой. Step-3. Тип трансфера - Tours')

if text['car_type'] != full_class_name_list[random_index_class]:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write(f'Машина не корректно передалась (или вообще не передалась) на вебхук. Ожидалась машина "{full_class_name_list[random_index_class]}", а на вебхук пришло "{text["car_type"]}". Step-3. Тип трансфера - Tours')



# Запрашиваем данные созданного лида
hookData = requests.get('https://dli.3wp.ru/wp-content/plugins/step-form-backend/core/checkZoho.php')
text = json.loads(hookData.text)

if text['entity_status'] != "lead" or text['first_name'] != firstName or text['last_name'] != lastName or text['umail'] != umail or text['tel'] != tel or text['pickup'] != pickup_list.pickup_list[random_index_pickup] or text['ride_date'] != finDate:
    with open('errorLog.txt', 'a', encoding='utf-8') as err:
        err.write('Неверные данные пришли на вебхук при создании лида. Step-2. Тип трансфера - Tours')


driver.back()

# Получение случайного индекса, отличного от предыдущего
while True:
    second_index = random.randrange(len(class_list))
    if second_index != random_index_class:
        break

secondChoosenClass = class_list[second_index]
secondStep3Button = driver.find_element_by_id(f'{secondChoosenClass}-button')
driver.execute_script("arguments[0].click();", secondStep3Button)

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


driver.quit()
