transaction1 = {
  'amount': '30',
  'sender': 'Alice',
  'receiver': 'Bob'}
transaction2 = { 
  'amount': '200',
  'sender': 'Bob',
  'receiver': 'Alice'}
transaction3 = { 
  'amount': '300',
  'sender': 'Alice',
  'receiver': 'Bob' }
transaction4 = { 
  'amount': '300',
  'sender': 'Bob',
  'receiver': 'Alice' }
transaction5 = { 
  'amount': '200',
  'sender': 'Alice',
  'receiver': 'Bob' }
transaction6 = { 
  'amount': '400',
  'sender': 'Bob',
  'receiver': 'Alice' }

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]

#1 add a new transaction
my_transaction = { 
  'amount': '100',
  'sender': 'Alice',
  'receiver': 'Bob' }

#2 add new transaction to the existing one
mempool.append(my_transaction)

#test print
#print(mempool)

#3 create a new list of addtional three new transactions

block_transactions = mempool[0:3]
print(block_transactions)







