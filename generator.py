#!/usr/bin/env python3

import secrets
import json
import sys
from algosdk import account, mnemonic

class Generator:
	def generateAccounts(self, numAccounts):
		ret = dict()

		for i in range(0, numAccounts):
			private_key, address = account.generate_account()
			ret[i] = mnemonic.from_private_key(private_key)

		return ret

	def generator(self, file_name, numAccounts):

		output_file_name = "accounts-{}.json".format(secrets.randbits(32)) 

		with open(output_file_name, "w") as output:
			final_object = self.generateAccounts(numAccounts)
			json.dump(final_object, output, indent=4)
		
if __name__ == '__main__':
	Generator().generator("algo-config.json", int(sys.argv[1]))

