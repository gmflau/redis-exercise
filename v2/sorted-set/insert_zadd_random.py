import redis
import random

r = redis.StrictRedis(host="localhost",
        port="6379",
        charset="utf-8",
        decode_responses=True)

num_ss_key = "ss1"

#
# O(N*log(N)) for zadd-ing N items 
#
# A new random value may collide with an existing one.
# In that case, repeated valuer will not be stored twice.
# Meaning only one copy of the value will remain in the 
# sorted set.
#
for i in range(1, 101):
    rand_num = random.randint(1,100)
    r.zadd(num_ss_key, { rand_num: rand_num })

ss_list = r.zrevrange(num_ss_key, "0", "-1")

#
# O(log(N)+M), O(log(N)+N) for printing the entire sorted set
#
print("Printing the items from a sorted set using zrevrange()")
count = 0
for item in ss_list:
    count += 1
    print(item, end=",")

print()
print("Total number of items => " + str(count))

r.delete(num_ss_key)
