from block import Block
from blockchain import Blockchain

def main():
    bc = Blockchain()

    bc.add_block('foo')
    bc.add_block('bar')
    bc.add_block('baz')
    bc.add_block('qux')

    for block in bc.chain:
        print(block)

if __name__ == '__main__':
    main()
