import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


import requests
import secrets
import string

url = "http://127.0.0.1:8000/play/createRoom/"
loginUrl = "http://127.0.0.1:8000/login/"

isBugFree = False

for i in range(20):
    N = 20
    res = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(N))

    """PARAMETERS = {
        'username': "{}".format(res),
        'email': "user@{}.com".format(res),
        'password': "Jayash@403",
        'password2': "Jayash@403"
    }"""

    PARAMETERS = {
        "roomId": res
    }


    r = requests.post(url, PARAMETERS, headers={'Authorization': "Token ec5e0e255e66fe1a9378325c7edc3c02a3ed4709"})

    print(r.text)

#     LOGINPARAMETERS = {
#         'username': "pLO2RLKc$f7b",
#         'password': "pLO2RLKc$f7b"
#     }

#     # r = requests.post(loginUrl, PARAMETERS)


#     # if not str(r.text).startswith('{"token"'):
#     #     isBugFree = True
#     #     print(r.text)

# if isBugFree:
#     print("Passed All Test Cases!")