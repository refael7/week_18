
import json
import time
from datetime import datetime, timezone
from redis_connection import conn_redis
from mongo_connection import conn_mongo

QUEUE_URGENT = "queue_urgent"
QUEUE_NORMAL = "queue_normal"

collection = conn_mongo.collection("alerts")


def main():

    while True:
        message = conn_redis.lpop(QUEUE_URGENT)

        if message is None:
            message = conn_redis.lpop(QUEUE_NORMAL)


        if message is None:
            time.sleep(5.0)
            continue

        alert = json.loads(message)


        alert["insertion_time"] = datetime.now(timezone.utc).isoformat()


        collection.insert_one(alert)


main()
