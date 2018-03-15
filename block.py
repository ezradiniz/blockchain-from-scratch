from hashlib import sha256

class Block(object):

    def __init__(self, timestamp, lastHash, curHash, data, nonce, difficulty):
        self.timestamp = timestamp
        self.lastHash = lastHash
        self.curHash = curHash
        self.data = data
        self.nonce = nonce
        self.difficulty = difficulty

    @staticmethod
    def genesis():
        '''Return genesis block'''
        return Block('Genesis time', '----', 'ezra-hash', [], 0, 1)

    @staticmethod
    def mineBlock(lastBlock, data):
        ''' Mine block '''
        pass

    def __str__(self):
        return f'''
            Timestamp: {self.timestamp}
            Last Hash: {self.lastHash[:10]}
            Hash: {self.curHash[:10]}
            Difficulty: {self.difficulty}
            Nonce: {self.nonce}
            Data: {self.data}
        '''
