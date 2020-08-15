import requests
import argparse
import base64

parser = argparse.ArgumentParser(description='Upload a record to zTeros Light.')
parser.add_argument('--UID', help='UID of the record you wish to update', action = 'store')
parser.add_argument('--File', help='The full path to the file you wish to upload', action = 'store')
parser.add_argument('--Address', help='Address of zTeros Instance', action = 'store')

args = parser.parse_args()

# For simplicity we are uploading a text file containing JSON data, this could be anything.
f = open(args.File, "r")

# We are encoding the file in base64, this helps more if it was a binary format.
payload = base64.b64encode(f.read().encode('ascii')).decode('ascii')
f.close()

# Sends a put request to your instance e.g. http://<your-url.com>:8080/EncryptionService/records/12345678abcde
resp = requests.put('http://{}/EncryptionService/records/{}'.format(args.Address, args.UID), payload)

if resp.status_code != 200:
    # This means something went wrong.
    print('POST /records/ {}'.format(resp.status_code))

# The response should be in the format {"RecordUID": "12345678abcde", "Completed": "True"} for now we will just print it.
print(resp.text)
