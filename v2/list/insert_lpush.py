import redis
import json

r = redis.Redis(host="localhost",
        port="6379",
        charset="utf-8",
        decode_responses=True)

num_list_key = "list_1to100"

# O(N) for N number of items
for i in range(1, 101):
    r.lpush(num_list_key, i)

# O(S+N), O(N) for printing all the items
num_list = r.lrange(num_list_key, "0", "-1")

for item in num_list:
    print(item, end=",")

print()
r.delete(num_list_key)
