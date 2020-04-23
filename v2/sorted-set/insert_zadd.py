import redis
import json

r = redis.StrictRedis(host="localhost",
        port="6379",
        charset="utf-8",
        decode_responses=True)

num_ss_key = "ss1"

# O(N*log(N)) for zadd-ing N items
for i in range(1, 101):
    r.zadd(num_ss_key, { i: i })

ss_list = r.zrevrange(num_ss_key, "0", "-1")

# O(log(N)+M), O(log(N)+N) for printing the entire sorted set
print("Printing the items from a sorted set using zrevrange()")
count = 0
for item in ss_list:
    count += 1
    print(item, end=",")

print()
print("Total number of items => " + str(count))

r.delete(num_ss_key)
