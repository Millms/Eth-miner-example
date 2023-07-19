import hashlib

def mine(block_number, transactions, previous_hash, prefix_zeros):
    # Define the prefix with required number of zeros
    prefix_str = '0' * prefix_zeros

    # Initialize a nonce (a value that will be changed until a valid hash is found)
    nonce = 0

    while True:
        # Create the candidate block data by combining relevant information
        data = str(block_number) + transactions + previous_hash + str(nonce)

        # Hash the candidate block data using SHA256
        hash_result = hashlib.sha256(data.encode()).hexdigest()

        # Check if the hash meets the required prefix criteria
        if hash_result.startswith(prefix_str):
            print(f"Successfully mined a block with Nonce: {nonce}")
            return hash_result

        # Increment the nonce for the next iteration
        nonce += 1

if __name__ == "__main__":
    # Example data for mining a block
    block_number = 1
    transactions = "example_transactions_data"
    previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"
    prefix_zeros = 4  # The higher the value, the more difficult it is to mine the block

    mined_hash = mine(block_number, transactions, previous_hash, prefix_zeros)
    print("Mined Hash:", mined_hash)
