from datetime import datetime
import random
import time

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]

for i in range(5):
    current_minute =datetime.today().minute
    if current_minute in odds:
        print("current minute is odd ")
    else :
        print("current minute is not odd ")
    wait_time = random.randint(1,10)    
    time.sleep(wait_time)
