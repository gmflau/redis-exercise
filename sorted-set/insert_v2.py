import redis
import json

r = redis.StrictRedis(host="10.168.0.2",
        port="10001",
        charset="utf-8",
        decode_responses=True)

num_ss_key = "ss1"

for i in range(1, 101):
    r.zadd(num_ss_key, { i: i })

ss_list = r.zrevrange(num_ss_key, "0", "-1")

print("Printing the items from a sorted set using zrevrange()")
count = 0
for item in ss_list:
    count += 1
    print(item, end=",")

print()
print("Total number of items => " + str(count))
r.delete(num_ss_key)
