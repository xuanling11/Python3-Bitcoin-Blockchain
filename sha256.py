# import sha256
from hashlib import sha256

# text to hash
text = "I am excited to learn about blockchain"
text1 = "I am excited to learn about blockchain!"

# encode the text
hash_result = sha256(text.encode())
hash_result1 = sha256(text1.encode())

# print result
print(hash_result.hexdigest())
print(hash_result1.hexdigest())
