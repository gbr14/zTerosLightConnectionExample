import requests
import argparse
import base64

parser = argparse.ArgumentParser(description='Retrieve a Record from zTeros Light.')
parser.add_argument('--UID', help='UID of the record you wish to retrieve', action = 'store')
parser.add_argument('--File', help='The full path to the file you wish to save to', action = 'store')
parser.add_argument('--Address', help='Address of zTeros Instance', action = 'store')

args = parser.parse_args()


# Sends a get request to your instance e.g. http://<your-url.com>:8080/EncryptionService/records/12345678abcde
resp = requests.get('http://{}/EncryptionService/records/{}'.format(args.Address, args.UID))

if resp.status_code != 200:
    # This means something went wrong.
    print('POST /records/ {}'.format(resp.status_code))
    print(resp.text)
    quit()

f = open(args.File, "w")

# As we encoded to base64 in the upload we need to decode it now.
f.write(base64.b64decode(resp.json()['Data'].encode('ascii')).decode('ascii'))
f.close()

# We don't print the full response here as it contains the output.
# But it would be in the format { "Completed": "True", "RecordUID": "12345678abcde", "Data": "My Data"} 
