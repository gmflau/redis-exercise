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

for item in ss_list:
    print(item)

r.delete(num_ss_key)
