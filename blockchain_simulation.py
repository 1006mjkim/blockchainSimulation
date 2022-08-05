from hashlib import sha256
#SHA-256 = Secure Hashing Algorithm, 256 0s and 1s
import json
import random, datetime

#Block class
class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=random.randint(0,9)):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        #convert the attributes of the object to strings
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


#Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = []

    def check_proof_of_work(self, block, rand):
        if block.nonce == rand:
            return 1
        else:
            return 0
        
    def mine(self):
        length = len(self.chain)
        block = self.chain[length-1]
        rand = random.randint(0,9);
        while self.check_proof_of_work(block, rand) != 1:
            rand = random.randint(0,9)
        self.chain.append(Block(length+1, [], str(datetime.datetime.now()), self.chain[length-1].compute_hash()))

blocks = Blockchain()
blocks.chain.append(Block(1, [], str(datetime.datetime.now()), 0))
print(blocks.chain[0].compute_hash())

blocks.mine()
print(blocks.chain[len(blocks.chain)-1].compute_hash())
print(vars(blocks.chain[len(blocks.chain)-1]))
