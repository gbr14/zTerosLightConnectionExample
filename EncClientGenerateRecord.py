import requests
import argparse

parser = argparse.ArgumentParser(description='Generate a new Record in zTeros Light.')
parser.add_argument('--Address', help='Address of zTeros Instance in the format ip address:port (e.g. 172.0.0.1:8080) or FQDN:port (your-url.com:8080)', action = 'store')

args = parser.parse_args()

# Sends a post request to your instance e.g. http://<your-url.com>:8080/EncryptionService/records/
resp = requests.post('http://{}/EncryptionService/records/'.format(args.Address))
if resp.status_code != 200:
    # This means something went wrong.
    print('POST /records/ {}'.format(resp.status_code))
# Should return a response in the format record {"RecordUID":"12345678abcde"} make a note of this UID for future calls.
print(resp.text)
