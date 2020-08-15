# A simple script to check the actual size of a payload being sent to a zTeros Light when it is encoded in base64

from sys import getsizeof
import base64
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--File', metavar='-F', help='The full path to the file you wish to upload', action = 'store')

args = parser.parse_args()

f = open(args.File, "r")

payload = base64.b64encode(f.read().encode('ascii')).decode('ascii')
f.close()

print(getsizeof(payload))
