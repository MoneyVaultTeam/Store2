from web3 import Web3

# Connect to your Ethereum node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/142343463eb54932a7091eb52a5507cc'))  # Replace with your Infura project ID

# Replace with the contract address and ABI of the token
contract_address = "0x1ec9f8d4b77aa4243d90d5dc61a57c95241af7a9"
contract_abi = [...]  # Insert the ABI of the token contract

# Create a contract object
token_contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Replace with the name of the method that returns the token price
price_method_name = "getPrice"  # Replace with the actual method name

# Get the current price of the token
def get_token_price():
    try:
        price = token_contract.functions[price_method_name]().call()
        return price
    except Exception as e:
        print("Error:", e)
        return None

# Main function
def main():
    token_price = get_token_price()
    if token_price is not None:
        print("Current Token Price:", token_price)
    else:
        print("Failed to retrieve token price.")

if __name__ == "__main__":
    main()

