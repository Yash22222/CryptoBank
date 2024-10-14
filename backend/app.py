from flask import Flask, jsonify, request
import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', nonce=100)  # Create the genesis block

    def new_block(self, nonce, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'nonce': nonce,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset the list of current transactions
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1  # Return the index of the block that will hold this transaction

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def validate_chain(self):
        # Check if the blockchain is valid
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            previous_block = self.chain[i - 1]

            if block['previous_hash'] != self.hash(previous_block):
                return False
            if block['index'] != previous_block['index'] + 1:
                return False
        return True

app = Flask(__name__)

# Create a blockchain instance
blockchain = Blockchain()

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Crypto Bank!"})

@app.route('/mine', methods=['GET'])
def mine():
    # Simulate mining
    last_block = blockchain.last_block
    nonce = 100  # In a real application, you'd compute this dynamically
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(nonce, previous_hash)
    response = {
        'message': 'New block mined!',
        'index': block['index'],
        'transactions': block['transactions'],
        'nonce': block['nonce'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transaction', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']

    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/validate', methods=['GET'])
def validate():
    is_valid = blockchain.validate_chain()
    if is_valid:
        response = {'message': 'Blockchain is valid.'}
    else:
        response = {'message': 'Blockchain is not valid.'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)