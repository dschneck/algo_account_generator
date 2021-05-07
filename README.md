# Algorand Account Generator
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

### Example
	**Input:**

	$ python3.8 generator.py 2
	
	**Output:**

```
{
	"hj65k423k34l2": "3214jkl234jl1234",
	"l45536j7kl43d": "7jk4l35j43kl56j3"
}

```
