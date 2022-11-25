import hashlib
import json
import os


class Hash:
    def __init__(self, data, diff=4):
        self.data = data
        self.diff = diff

    def get_hash(self):
        h = hashlib.sha256(str(self.data).encode()).hexdigest()
        '''for h in range(self.diff - 1):
            h = hashlib.sha256(str(h).encode()).hexdigest()'''
        return h


class Block:
    def __init__(self, name, amount, to_whom_name, path='D:/projects/blocks/'):
        self.name = name
        self.amount = amount
        self.to_whom_name = to_whom_name
        self.path = path

    def get_last_block(self):
        files = os.listdir(self.path)
        files_2 = []
        for file in files:
            files_2.append(int(file.split('.')[0]))

        last_file = max(files_2)
        return last_file

    def get_last_block_hash(self):
        last_file_data = json.load(open(self.path + str(int(self.get_last_block())) + '.txt'))
        return last_file_data[0]['hash']

    def data_creator(self, preview_hash='0'):
        return [
            {'hash': Hash(self.name + str(self.amount) + self.to_whom_name + preview_hash).get_hash()},
            {'from': self.name, 'amount': self.amount, 'to_whom': self.to_whom_name},
            {'preview_hash': preview_hash}]

    def create_block(self):
        try:
            filename = self.get_last_block() + 1
            dump_data = self.data_creator(self.get_last_block_hash())
        except ValueError:
            filename = 1
            dump_data = self.data_creator()

        with open(self.path + str(filename) + '.txt', 'w') as fp:
            json.dump(dump_data, fp, indent=4, ensure_ascii=False)


Block('Json', 1000, 'skama.net').create_block()
Block('Arab', 666, 'Masha').create_block()
Block('Lena', 3, 'Alisa').create_block()
Block('Anna', 7323, 'Ivan').create_block()
Block('Arab', 32, 'Masha').create_block()
Block('Lena', 85515, 'Alisa').create_block()

