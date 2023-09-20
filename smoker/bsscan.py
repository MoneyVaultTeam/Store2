from web3 import Web3

# Connect to your Ethereum node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/142343463eb54932a7091eb52a5507cc'))    # Replace with your Infura project ID

# Replace with the contract address
contract_address = "0x1ec9f8d4b77aa4243d90d5dc61a57c95241af7a9"


def get_contract_abi(contract_address):
    try:
        # Get the transaction receipt of the contract creation
        tx_receipt = w3.eth.getTransactionReceipt(contract_address)
        print(tx_receipt)
        if tx_receipt is not None and tx_receipt["contractAddress"] == contract_address:
            # The contract address matches the receipt, so extract the ABI
            contract_abi = w3.eth.get_code(contract_address).hex()[10:]
            return contract_abi
        else:
            print("Transaction receipt not found or contract address mismatch.")
            return None
    except Exception as e:
        print("Error:", e)
        return None

# Main function
def main():
    contract_abi = get_contract_abi(contract_address)
    if contract_abi:
        print("Contract ABI:", contract_abi)
    else:
        print("Failed to retrieve contract ABI.")

if __name__ == "__main__":
    main()
