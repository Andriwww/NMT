from monitor import check_hosts
import time
import json

with open("config.json") as f:
    config = json.load(f)

HOSTS = config["hosts"]
INTERVAL = config["interval"]

while True:
    check_hosts(HOSTS)
    print("-" * 60)
    time.sleep(INTERVAL)
