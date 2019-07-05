import requests
from concurrent.futures import ThreadPoolExecutor


def req():
    print(" req  start")
    r = requests.get("http://localhost:5000/api/lip/?file_path=/root&speechtext=4211")
    print(r.text)


with ThreadPoolExecutor(8) as executor:
        for _ in range(8):
            print(' submit req ')
            executor.submit(req)
