from blockchain import Blockchain
from block import Block

blockchain = Blockchain()

blockchain.add_block(Block("Transaction 1"))
blockchain.add_block(Block("Transaction 2"))

print("\nBlockchain validity:", blockchain.is_chain_valid())

# Tampering Example
blockchain.chain[1].data = "Hacked Transaction"
print("After tampering:", blockchain.is_chain_valid())