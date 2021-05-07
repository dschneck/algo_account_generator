import secrets
import json
import sys
from algosdk import account, mnemonic
from algosdk.v2client import algod

def generateAccounts(N):
	ret = dict()

	for i in range(0, N):
		private_key, address = account.generate_account()
		ret[private_key] = address

	return ret

algod_client = None

# You need to make your own config.json with your 
# ALGOD_TOKEN and ALGOD_ADDRESS given to you by your access nodeo
with open("config.json", "r") as config:
	info = json.load(config)
	algod_client = algod.AlgodClient(info["ALGOD_TOKEN"],info["ALGOD_ADDRESS"])

file_name = "accounts-{}.json".format(secrets.randbits(32)) 

with open(file_name, "w") as output:
	n = int(sys.argv[1])
	final_object = generateAccounts(n)
	json.dump(final_object, output, indent=4)
	




