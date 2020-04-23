import redis
import random

r = redis.Redis(host="10.168.0.2",
        port="10001",
        charset="utf-8",
        decode_responses=True)

num_list_key = "list_1to100"

for i in range(1, 101):
    r.lpush(num_list_key, i)

num_list = r.lrange(num_list_key, "0", "-1")

count = 0
for item in num_list:
    count += 1
    print(item, end=",")

print()
print("Total number of items inserted = " + str(count))


print("Now insert additional 100 random values using lpush()")
print("The items in data structure before sorting")
for j in range(0, 100):
    rand_num = random.randint(1,100)
    r.lpush(num_list_key, rand_num)

num_list = r.lrange(num_list_key, "0", "-1")

for item in num_list:
    print(item, end=",")


print()
print("The items in data structure after sorting")
r.sort(num_list_key, desc=True, store=num_list_key)

num_list = r.lrange(num_list_key, "0", "-1")
count = 0
for item in num_list:
    count += 1
    print(item, end=",")


print()
print("Final total number of items = " + str(count))
print("Time complexity for this is O(N+M*log(M))")

r.delete(num_list_key)
