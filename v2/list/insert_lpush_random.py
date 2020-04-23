import redis
import random

r = redis.Redis(host="localhost",
        port="6379",
        charset="utf-8",
        decode_responses=True)

num_list_key = "list_1to100"

print("Insert 100 random values into a list")
count = 0
for i in range(1, 101):
    rand_num = random.randint(1,100)    
    r.lpush(num_list_key, rand_num)

num_list = r.lrange(num_list_key, "0", "-1")
for item in num_list:
    count += 1
    print(item, end=",")
print()
print("Total number inserted into the list (before sorting) => " + str(count))


print("Let's sort our number in the list")
r.sort(num_list_key, desc=True, store=num_list_key)

num_list = r.lrange(num_list_key, "0", "-1")
count = 0
for item in num_list:
    count += 1
    print(item, end=",")
print()
print("Total number in the list (after sorting) => " + str(count))


r.delete(num_list_key)
