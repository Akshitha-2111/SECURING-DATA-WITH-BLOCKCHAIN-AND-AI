Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import json
... import time
... from hashlib import sha256
... 
... class Block:
...     def __init__(self, index, transactions, timestamp, previous_hash):
...         self.index = index
...         self.transactions = transactions
...         self.timestamp = timestamp
...         self.previous_hash = previous_hash
...         self.nonce = 0
... 
...     def compute_hash(self):
...         block_string = json.dumps(self.__dict__, sort_keys=True)
...         return sha256(block_string.encode()).hexdigest()
... 
... 
... class Blockchain:
...     difficulty = 2
... 
...     def __init__(self):
...         self.unconfirmed_transactions = []
...         self.chain = []
...         self.create_genesis_block()
... 
...     def create_genesis_block(self):
...         genesis_block = Block(0, [], time.time(), "0")
...         genesis_block.hash = genesis_block.compute_hash()
...         self.chain.append(genesis_block)
... 
...     @property
...     def last_block(self):
...         return self.chain[-1]
... 
...     def proof_of_work(self, block):
...         block.nonce = 0
...         computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block
        new_block = Block(
            index=last_block.index + 1,
            transactions=self.unconfirmed_transactions,
            timestamp=time.time(),
            previous_hash=last_block.hash
        )

        proof = self.proof_of_work(new_block)
        new_block.hash = proof
        self.chain.append(new_block)
        self.unconfirmed_transactions = []
