from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

my_blockchain = Blockchain()
#add the new block
#my_blockchain.add_block(new_transactions)
#to print the block
#my_blockchain.print_blocks()

#try to fake a transaction
my_blockchain.add_block("fake_transactions")
my_blockchain.print_blocks()
my_blockchain.validate_chain()


