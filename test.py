import datetime  
from datetime import datetime
import date_list
import random

random_index_date = random.randrange(len(date_list.date_list))

inputDate = date_list.date_list[random_index_date]
newDate = datetime.strptime(inputDate, "%Y-%m-%dT%H:%M")
finDate = newDate.strftime('%d.%m.%Y %H:%M')
print(finDate)
