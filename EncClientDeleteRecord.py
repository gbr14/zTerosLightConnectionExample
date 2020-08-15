import requests
import argparse
import base64

parser = argparse.ArgumentParser(description='Deletes a record from zTeros Light.')
parser.add_argument('--UID', help='UID of the record you wish to delete', action = 'store')
parser.add_argument('--Address', help='Address of zTeros Instance', action = 'store')

args = parser.parse_args()


# Sends a delete request to your instance e.g. http://<your-url.com>:8080/EncryptionService/records/12345678abcde
resp = requests.delete('http://{}/EncryptionService/records/{}'.format(args.Address, args.UID))

if resp.status_code != 200:
    # This means something went wrong.
    print('DELETE /records/ {}'.format(resp.status_code))

# Response should be in the format {"Completed": "True", RecordUID":"12345678abcde "}
print(resp.text)
