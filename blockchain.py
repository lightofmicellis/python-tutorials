#
# Importing the Various Modules and Libraries 
# 

import sys
import hashlib
import json
from time import time
from urllib import response
from uuid import uuid4
from flask import Flask, jsonify, request
import flask
import requests
from urllib.parse import urlparse

#
# Declaring the Class in Python
#  

class Blockchain(object):
    difficulty_target = "0000"
    def hash_block(self, block):
        block_encoded = json.dumps(block, 
            sort_keys=True) .encode()
        return hashlib.sha256(block_encoded) .hexdigest() 
    def __init_(self):
        # stores all the blocks in the entire blockchain
        self.chain = []
        # temporary stores the transaction for the 
        # current block
        self.current_transactions = []
        # create the genesis block with a specific fixed hash
        # of previous block genesis block starts with index 0
        genesis_hash = self.hash_block("genesis_block")
        self.append_block(
            hash_of_previous_block = genesis_hash,
            nonce = self.proof_of_work(0, genesis_hash, [])
        )

    # The preceding creates a class name blockchain with 
    # two method: hash_block and __init__
    
    #
    # Finding the Nonce 
    # 

    # Use PoW to find the nonce for the current block

    def proof_of_work(self, index, hash_of_previous_block, transactions):
        # Try with nonce = 0
            nonce = 0
            # try hashing the nonce together with the hash of the
            # previous block unitl it is valid 
            while self.valid_proof(index, hash_of_previous_block,
                transactions, nonce is False):
                nonce += 1
                return nonce    
    
    # The proof_of_work() function first starts with zero 
    # for the nonce and check if the nonce together with 
    # the content of the block produces a hash that 
    # matches the difficulty target. If not, it increments 
    # the nonce by one and then try again until it finds the 
    # correct nonce.


    # The next method, valid_proof(), hashes the content of a 
    # block and check to see if the block’s hash meets the 
    # difficulty target:


    def valid_proof(self, index, hash_of_previous_block,
        transactions, nonce):
        # create a string containing the hash of the previous
        # block and the block content, including the nonce
        content = f'{index} {hash_of_previous_block} {transactions} {nonce}'.encode()
        # hash using sha256
        content_hash = hashlib.sha256(content).hexdigest()
        # check if the hash meets the difficulty target 
        return content_hash[:len(self.difficulty_target)] == self.difficult_target
    
    #
    # Appending the Block to the Blockchain 
    # 


    # Once the nonce for a block has been found, you can now write the method to 
    # append the block to the existing blockchain. This is the function of the 
    # append_block() method :

    # Write a new block and append it to the blockchain

    def append_block(self, nonce, hash_of_previous_block):
    block = {
        'index': len(self.chain),
        'timestamp': time(),
        'transactions': self.current_transactions,
        'hash_previous_block': hash_of_previous_block
    }
    # Reset the current list of transactions
    self.current_transactions = []
    # Add the new block to the blockchain
    self.chain.append(block)
    return block


    # When the block is added to the blockchain, the current timestamp is also added 
    # to the block.
    
    #
    # Adding Transactions 
    #

    # The next method we will add to the Blockchain class is the add_transaction() 
    # method :

    def add_transactions(self, sender, receipt, amount):
        self.current_transactions.append({
            'amount': amount,
            'receipt': receipt,
            'sender': sender
        })
        return self.last_block['index'] + 1
    
    # This method adds a new transaction to the current list of transactions. 
    # It then gets the index of the last block in the blockchain and adds one to it.
    #  This new index will be the block that the current transaction will be added to. 

    # To obtain the last block in the blockchain, define a property called 
    # last_block in the Blockchain class:

    @property
    def last_block(self):
        # return the last block in the blockchain
        return self.chain[-1]

#
# Exposing the Blockchain Class as a Rest API 
#

# Our Blockchain class is now complete, and so let’s now expose it as a REST API using Flask. 
# Append the following statements to the end of the blockchain.py file:

app = flask(__name__)

# Generate a globally unique address for this node.
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

#
#Obtaining the Full Blockchain
#

# For the REST API, we want tocreate a route for users toobtain the current 
# blockchain, so append the following statements to the end of blockchain.py :

# return the entire blockchain
@app.route('/blockchain' methods= ['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200    











