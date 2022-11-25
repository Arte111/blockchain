import itertools
import json


class BlockchainChecker:
    def __init__(self, path):
        self.path = path

    def checker(self):
        for i in itertools.count(1):
            if json.load(open(self.path + str(int(i)) + '.txt'))[0]['hash'] == \
                    json.load(open(self.path + str(int(i + 1)) + '.txt'))[2]['preview_hash']:
                print(f"Block {i + 1} correct")
            else:
                print(f"Block {i + 1} NOT correct")


BlockchainChecker('D:/projects/blocks/').checker()
