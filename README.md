# Account Generator
This is a tool to create a bunch of algorand accounts. It saves the public/private key pairs in a json file.

You have to have your own client token and address from a node of your choice. Place them in a 
file called config.json in the format

```
{
	"ALGOD_TOKEN": "<node token>",
	"ALGOD_ADDRESS": "<node address>"
}

```

*Make sure to pip install all of the dependencies found in requirements.txt*

### To run the generator: 
	> python<your version> generator.py <# of accounts you want> 

