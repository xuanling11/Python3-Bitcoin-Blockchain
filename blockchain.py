#imports the Block class from block.py
from block import Block

class Blockchain:
    def __init__(self):
      self.chain = []
      self.all_transactions = []
      self.genesis_block() #start with genesis block

    #initiate with genesis block
    def genesis_block(self):
      Block(self.all_transactions, previous_hash = 0)
      self.chain.append(Block)


