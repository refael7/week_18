import json
from dotenv import dotenv_values
from redis_connection import conn
from priority_logic import priority as p

config = dotenv_values(".env")

ALERTS_FILE = r"data\border_alerts.json"

QUEUE_URGENT = "urgent_queue"
QUEUE_NORMAL = "normal_queue"


def load_alerts(file_path):

    with open(file_path, "r") as f:
        return json.load(f)




def main():
    alerts = load_alerts(ALERTS_FILE)
    print(f"loaded {len(alerts)} alerts")

    urgent_count = 0
    normal_count = 0

    for alert in alerts:
        priority = p(alert)
        alert["priority"] = priority

        alert_r = json.dumps(alert)

        if priority == "URGENT":
            conn.rpush(QUEUE_URGENT, alert_r)
            urgent_count += 1
        else:
            conn.rpush(QUEUE_NORMAL, alert_r)
            normal_count += 1

    print(f" urgent: {urgent_count}, normal: {normal_count}")


main()