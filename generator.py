#!/usr/bin/env python3

import secrets
import json
import sys
from algosdk import account, mnemonic
from algosdk.v2client import algod

class Generator:
	def generateAccounts(self, numAccounts):
		ret = dict()

		for i in range(0, numAccounts):
			private_key, address = account.generate_account()
			ret[private_key] = address

		return ret

	def generator(self, file_name, numAccounts):
		algod_client = None

		# ALGOD_TOKEN and ALGOD_ADDRESS given to you by your access node
		with open(file_name, "r") as config:
			info = json.load(config)
			algod_client = algod.AlgodClient(info["ALGOD_TOKEN"],info["ALGOD_ADDRESS"])

		output_file_name = "accounts-{}.json".format(secrets.randbits(32)) 

		with open(output_file_name, "w") as output:
			final_object = self.generateAccounts(numAccounts)
			json.dump(final_object, output, indent=4)
		
if __name__ == '__main__':
	Generator().generator("config.json", int(sys.argv[1]))

