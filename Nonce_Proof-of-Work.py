new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

#Import the sha256 hash function from the Python hashlib library
from hashlib import sha256 

# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
# default nonce from 0
nonce = 0
# creating the proof 
proof = sha256((str(nonce)+str(new_transactions)).encode()).hexdigest()

# printing proof
print(proof)

# finding a proof that has 2 leading zeros

while (proof[:2] != '0'*difficulty):
  nonce += 1
  proof = sha256((str(nonce)+str(new_transactions)).encode()).hexdigest()

# printing final proof that was found
final_proof = proof
print(final_proof)
