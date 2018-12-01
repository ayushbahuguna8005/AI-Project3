import re
import math


class LanguageModel:

    def __init__(self, filename):
        self.text = LanguageModel.read_file(filename)
        self.alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't',
                          'u', 'v', 'w', 'x', 'y', 'z']

    def __init__(self, filename, filename2):
        self.book1 = LanguageModel.read_file(filename)
        self.book2 = LanguageModel.read_file(filename2)
        self.text = self.book1 + self.book2
        self.alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't',
                          'u', 'v', 'w', 'x', 'y', 'z']

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
    def __init__(self, filename, filename2):
        super().__init__(filename, filename2)
        self.alphabets_map = {}
        for c in self.text:
            if c in self.alphabets_map:
                self.alphabets_map[c] += 1
            else:
                self.alphabets_map[c] = 1

    def calc_prob_unigram(self, sentence):
        # sentence = sentence.replace(" ", "").lower()
        sentence_new = LanguageModel.clean_sentence(sentence)
        # print(sentence_new)
        prob = 0;
        for c in sentence_new:
            # print('char : ', c)
            if c in self.alphabets_map:
                x = (self.alphabets_map[c] + 0.5) / (len(self.text) + 26 * 0.5)
                prob += math.log(x)
            else:
                x = 0.5 / len(self.text)
                prob += math.log(x)
        return prob

    def print_dict(self):
        for key in self.alphabets_map:
            print(key, self.alphabets_map[key])
        # print(len(self.alphabets_map))

    def probabilities(self):
        probs_alpha = {}
        for key in self.alphabets_map:
            probs_alpha[key] = self.alphabets_map[key] / len(self.text)
        return probs_alpha

class Bigram(LanguageModel):
    def __init__(self, filename, filename2):
        super().__init__(filename, filename2)
        self.map_size = 26
        self.bigram_map = [0] * self.map_size
        for i in range(self.map_size):
            self.bigram_map[i] = [0] * self.map_size
        self.bigram_map[1][1] = 1
        for i in range(0, len(self.text) - 1):
            index_i = self.char_hash(self.text[i])
            index_j = self.char_hash(self.text[i + 1])
            self.bigram_map[index_i][index_j] += 1
        self.count_char = [sum(i) for i in self.bigram_map]

    def char_hash(self, character):
        return self.alphabets.index(character)

    def get_char(self, index):
        return self.alphabets[index]

    def print_map(self):
        for i in range(self.map_size):
            print(self.bigram_map[i])

    def calc_prob_bigram(self, sentence):
        sentence_new = LanguageModel.clean_sentence(sentence)
        # print("Clean sentence", sentence_new)
        prob = 0
        for i in range(len(sentence_new) - 1):
            index_i = self.char_hash(self.text[i])
            index_j = self.char_hash(self.text[i + 1])
            x = (self.bigram_map[index_i][index_j] + 0.5) / (self.count_char[index_i] + 26 * 0.5)
            prob += math.log(x)
        return prob


