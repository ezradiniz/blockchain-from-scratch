from block import Block

class Blockchain(object):

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        block = Block.mine_block(self.chain[len(self.chain) - 1], data)
        self.chain.append(block)
        return block

    def is_valid_chain(self, chain):
        genesis = f'{Block.genesis()}'
        block_init = f'{chain[0]}'

        if genesis != block_init:
            return False

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i - 1]
            if block.last_hash != last_block.cur_hash or block.cur_hash != Block.block_hash(block):
                return False

        return True

    def replace_chain(self, new_chain):
        if len(new_chain) <= len(self.chain):
            print('Received chain is not longer than the current chain.')
            return
        if not self.is_valid_chain(new_chain):
            print('Received chain is not valid.')
            return

        print('Replacing blockchain with the new chain.')
        self.chain = new_chain
