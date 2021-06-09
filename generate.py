import requests
import sys

if len(sys.argv) < 3:
    print("Usage: generate.py <key> <email> <password>")

headers = {
    'Content-Type': 'application/json',
}

args = (sys.argv)

params = (
    ('key', args[1]),
)

data =  {'email':args[2],
        'password':args[3],
        'returnSecureToken':'true'}

response = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword', headers=headers, params=params, data=str(data))

print(response.text)
