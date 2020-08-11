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
  'receiver': 'Timothy' }
transaction4 = { 
  'amount': '300',
  'sender': 'Rodrigo',
  'receiver': 'Thomas' }
transaction5 = { 
  'amount': '200',
  'sender': 'Timothy',
  'receiver': 'Thomas' }
transaction6 = { 
  'amount': '400',
  'sender': 'Tiffany',
  'receiver': 'Xavier' }

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]


my_transaction = {'amount':0, 'sender':0, 'receiver':0}

mempool.append(my_transaction)

block_transactions = []

my_transaction1 = {'amount':1, 'sender':0, 'receiver':1}
my_transaction2 = {'amount':2, 'sender':1, 'receiver':2}
my_transaction3 = {'amount':3, 'sender':2, 'receiver':3}

block_transactions.append(my_transaction1)
block_transactions.append(my_transaction2)
block_transactions.append(my_transaction3)

jojolapin = 55
print(jojolapin)

# Creation de block

# import de la bibliothèque datetime 
from datetime import datetime 
# affiche le date actuel
print(datetime.now())

class Block:
# Ceci est la classe Block 
  def __init__(self, timestamp, transactions, previous_hash,  nonce=0):
    self.transactions=0
    self.previous_hash=0
    self.nonce=0
    self.timestamp=datetime.now()
    
    
    pass
# -*- coding: utf-8 -*-
"""
Créée à partir d'un tuto CodeAcademy, le 11/09/2020
@author: PierreDaguier
"""

#importe la classe blocj depuis block.py
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

  # imprime le contenu de la blockchain
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()    
  
  # ajoute un block à la blockchain
  def add_block(self, transactions):
    previous_block_hash = self.chain[len(self.chain)-1].hash
    new_block = Block(transactions, previous_block_hash)
    # modify this method
    proof = self.proof_of_work(new_block, difficulty = 2)
    self.chain.append(new_block)
    return proof, new_block
    

  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      if(current.hash != current.generate_hash()):
        print("Le hash actuel du block n'est pas égal au hash généré par la fonction de génération de hash")
        return False
      if(current.previous_hash != previous.generate_hash()):
        print("Le hash du block précédent n'est pas égal au hash tel qu'il aurait dû être généré par la fonction de génération de hash")
        return False
    return True
  
  def proof_of_work(self,block, difficulty=2):
    proof = block.generate_hash()
    while proof[:difficulty] != '0'*difficulty:
      block.nonce += 1
      proof = block.generate_hash()
    block.nonce = 0
    return proof