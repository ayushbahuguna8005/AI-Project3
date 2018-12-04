import re
import math
import collections


class LanguageModel:

    def __init__(self, filenames):
        self.text = ''
        for filename in filenames:
            self.text += LanguageModel.read_file(filename)
        self.alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't',
                          'u', 'v', 'w', 'x', 'y', 'z']

    @staticmethod
    def write_file_lang_model(map, filename):
        with open(filename, 'w') as f:
            for key in map:
                f.write(key + ' = ' + str(map[key]) + '\n')

    @staticmethod
    def clean_sentence(sentence):
        # new_sen = sentence.replace(" ", "").lower()
        new_sen = re.sub('[^a-zA-Z\n]', '', sentence).lower()
        # print("Clean sentence ", sentence, new_sen)
        return new_sen

    @staticmethod
    def read_file(fileName):
        with open(fileName, "r") as f:
            for line in f:
                string_txt = f.read().replace("\n", "")
        string_txt = re.sub('[^a-zA-Z\n]', '', string_txt).lower()
        # with open('test.txt', "w") as wr:
        #     wr.write(string_txt)
        return string_txt


class Unigram(LanguageModel):
    def __init__(self, filenames):
        super().__init__(filenames)
        self.alphabets_map = {}
        self.probs_alpha = {}
        for c in self.text:
            if c in self.alphabets_map:
                self.alphabets_map[c] += 1
            else:
                self.alphabets_map[c] = 1
        self.generate_probabilities()

    def print_dict(self):
        for key in self.alphabets_map:
            print(key, self.alphabets_map[key])
        # print(len(self.alphabets_map))

    def generate_probabilities(self):
        temp_map = {}
        for key in self.alphabets_map:
            key2 = '(' + key + ')'
            temp_map[key2] = (self.alphabets_map[key] + 0.5) / (len(self.text) + 26 * 0.5)
        self.probs_alpha = collections.OrderedDict(sorted(temp_map.items()))


class Bigram(LanguageModel):

    def __init__(self, filenames):
        super().__init__(filenames)
        self.map_size = 26
        self.cond_probs = {}
        self.bigram_map = [0] * self.map_size
        for i in range(self.map_size):
            self.bigram_map[i] = [0] * self.map_size
        for i in range(0, len(self.text) - 1):
            index_i = self.char_hash(self.text[i])
            index_j = self.char_hash(self.text[i + 1])
            self.bigram_map[index_i][index_j] += 1
        self.count_char = [sum(i) for i in self.bigram_map]
        self.generate_conditional_prob()

    def char_hash(self, character):
        return self.alphabets.index(character)

    def get_char(self, index):
        return self.alphabets[index]

    def print_map(self):
        for i in range(self.map_size):
            print(self.bigram_map[i])

    def generate_conditional_prob(self):
        for i in range(self.map_size):
            for j in range(self.map_size):
                char_i = self.get_char(i)
                char_j = self.get_char(j)
                x = (self.bigram_map[i][j] + 0.5) / (self.count_char[i] + 26 * 0.5)
                key = '(' + char_i + '|' + char_j + ')'
                self.cond_probs[key] = x
