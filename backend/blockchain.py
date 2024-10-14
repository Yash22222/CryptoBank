import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        # Create the genesis block
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash,
            'transactions': self.pending_transactions
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.get_last_block()['index'] + 1

    def proof_of_work(self, last_proof):
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    def valid_proof(self, last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            previous_block = self.chain[i - 1]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            if not self.valid_proof(previous_block['proof'], block['proof']):
                return False
        return True