import json
from hashlib import sha256
from time import time

class Block(object):
    ''' Block is a part from blockchain '''

    def __init__(self, timestamp, last_hash, cur_hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.cur_hash = cur_hash
        self.data = data

    @staticmethod
    def genesis():
        '''Return genesis block'''
        return Block('Genesis time', '----', 'ezra-hash', [])

    @staticmethod
    def mine_block(last_block, data):
        ''' Mine block '''
        timestamp = int(round(time() * 1000))
        last_hash = last_block.cur_hash
        cur_hash = Block.hash(timestamp, last_hash, data)
        return Block(timestamp, last_hash, cur_hash, data)

    @staticmethod
    def hash(timestamp, last_hash, data):
        return sha256(f'{timestamp}{last_hash}{data}'.encode()).hexdigest()

    @staticmethod
    def block_hash(block):
        return Block.hash(block.timestamp, block.last_hash, block.data)

    def __str__(self):
        return f'''
            Data: {self.data}
            Hash: {self.cur_hash[:10]}
            Last Hash: {self.last_hash[:10]}
            Timestamp: {self.timestamp}
        '''
