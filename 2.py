import random
from datetime import datetime,timedelta
a=random.randrange(0,6)
print("Generate a random integer number 0 and 6 :")
print(a)
b=random.randrange(5,10)
print("Generate a random integer number 5 and 10 , excluding 10 :")
print(b)
c=random.randrange(0,10,3)
print("Generate a random integer number 0 and 10 with a step of 3 :")
print(c)
my_list=[]
date1=datetime.now()
one_day=timedelta(days=1)
date2=date1+one_day
my_list.append(datetime.strftime(date1,"%Y-%m-%d"))
my_list.append(datetime.strftime(date2,"%Y-%m-%d"))
print("Random date between two dates:")
print(random.choice(my_list))
