from blockchain import Blockchain

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Alice", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Bob", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Alice", "amount":"25"}

local_blockchain = Blockchain()
#creates a Genesis Block
#local_blockchain.print_blocks()
# print each transaction
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()

#Modify the second block
#local_blockchain.add_block(fake_transactions)
local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()
