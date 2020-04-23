import redis
import random

r = redis.StrictRedis(host="localhost",
        port="6379",
        charset="utf-8",
        decode_responses=True)

num_ss_key = "ss1"

for i in range(1, 101):
    rand_num = random.randint(1,100)
    r.zadd(num_ss_key, { rand_num: rand_num })

ss_list = r.zrevrange(num_ss_key, "0", "-1")

print("Printing the items from a sorted set using zrevrange()")
count = 0
for item in ss_list:
    count += 1
    print(item, end=",")

print()
print("Total number of items => " + str(count))

r.delete(num_ss_key)
