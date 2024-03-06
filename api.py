print("Start api read application")

import requests

paginaresults = requests.get("https://catfact.ninja/facts")
