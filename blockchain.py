#imports the Block class from block.py
from block import Block

class Blockchain:
  def __init__(self):
    self.chain = []
    self.all_transactions = []
    self.genesis_block()

  def genesis_block(self):
    transactions = {}
    genesis_block = Block(transactions, "0")
    self.chain.append(genesis_block)
    return self.chain

  # prints contents of blockchain
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()    
  
  # add block to blockchain `chain`
  def add_block(self, transactions):
    previous_block_hash = self.chain[len(self.chain)-1].hash
    new_block = Block(transactions, previous_block_hash)
    # perform PoW of the new block
    proof = self.proof_of_work(new_block)
    self.chain.append(new_block)
    return proof, new_block

  def validate_chain(self):
    # loop starts with 1
    for i in range(1, len(self.chain)):
      # validator guess hash value
      current = self.chain[i]
      previous = self.chain[i-1]
      # check if the validate hash is matching generate hash from the blockchain
      if (current.hash != current.generate_hash()):
        return False
      elif (previous.hash != previous.generate_hash()):
        return False
        #only and if only both hash generate from the validator matches the blockchain generated hash, the block is valid and can be posted on the blockchain
      else:
        return True
      
   def proof_of_work(self, block, difficulty=2):
    #Proof of Work
    proof = block.generate_hash()
    # finding the correct hash
    while (proof[:difficulty] != '0'*difficulty):
      block.nonce += 1
      proof = block.generate_hash()
    #reset nonce to 0
    block.nonce = 0
    return proof
