import math
import datetime
import random       
from math import sqrt,pi
sqrt_2 = math.sqrt(4)
print(sqrt_2)
number = random.randint(1,10000)
print(number)
choice = random.choice(['apple', 'banana', 'carrot'])
print(choice)
number

today = datetime.date.today()
print(today)
now = datetime.now()
print(now.date())
print(now.time())
datetime.utcnow()
now.strftime("%Y-%m-%d %H:%M:%S")


from zoneinfo import ZoneInfo

ist = ZoneInfo("Asia/Kolkata")
now_ist = datetime.now(ist)

print("Current IST:", now_ist)


# import os 
import os 
current_dir = os.getcwd()
print(current_dir)


#import json data
import json
data = {'name':'alice', 'age':30}
json_string=json.dumps(data)