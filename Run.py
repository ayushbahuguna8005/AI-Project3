import Models
import operator
import math
import matplotlib.pyplot as plt


class WriterFile:

    @staticmethod
    def write_file_output(sentence_original, filename_number, EN_Un, FR_Un, GE_Un, EN_Bi, FR_Bi, GE_Bi, print_all):
        with open('out' + str(filename_number) + '.txt', 'w') as f:
            sentence = Models.LanguageModel.clean_sentence(sentence_original)
            log_prob_en = 0
            log_prob_ge = 0
            log_prob_fr = 0
            f.write(sentence_original + '\n\n')
            print(sentence_original)
            f.write('UNIGRAM MODEL:\n\n')
            print('UNIGRAM MODEL:')
            for c in sentence:
                prob_en_uni = EN_Un.probs_alpha['(' + c + ')']
                log_prob_en += math.log(prob_en_uni, 10)

                prob_fr_uni = FR_Un.probs_alpha['(' + c + ')']
                log_prob_fr += math.log(prob_fr_uni, 10)

                prob_ge_uni = GE_Un.probs_alpha['(' + c + ')']
                log_prob_ge += math.log(prob_ge_uni, 10)
                f.write('UNIGRAM MODEL:' + c + '\n')

                f.write('FRENCH: P(' + c + ') = ' + str(prob_fr_uni) + ' ==> log prob of sentence so far: ' + str(
                    log_prob_fr) + '\n')
                f.write(
                    'ENGLISH: P(' + c + ') = ' + str(prob_en_uni) + ' ==> log prob of sentence so far: ' + str(
                        log_prob_en) + '\n')
                f.write('GERMAN: P(' + c + ') = ' + str(prob_ge_uni) + ' ==> log prob of sentence so far: ' + str(
                    log_prob_ge) + '\n\n')
                if print_all:
                    print('UNIGRAM MODEL:' + c)
                    print('FRENCH: P(' + c + ') = ' + str(prob_fr_uni) + ' ==> log prob of sentence so far: ' + str(
                        log_prob_fr))
                    print('ENGLISH: P(' + c + ') = ' + str(prob_en_uni) + ' ==> log prob of sentence so far: ' + str(
                        log_prob_en))
                    print('GERMAN: P(' + c + ') = ' + str(prob_ge_uni) + ' ==> log prob of sentence so far: ' + str(
                        log_prob_ge))
            maximum = max(log_prob_en, log_prob_ge, log_prob_fr)
            if log_prob_en == maximum:
                f.write('According to the unigram model, the sentence is in English\n\n')
                print('According to the unigram model, the sentence is in English')
            elif log_prob_fr == maximum:
                f.write('According to the unigram model, the sentence is in French\n\n')
                print('According to the unigram model, the sentence is in French')
            elif log_prob_ge == maximum:
                f.write('According to the unigram model, the sentence is in German\n\n')
                print('According to the unigram model, the sentence is in German')
            f.write('----------------\n\n')
            print('----------------\n')
            log_prob_en = 0
            log_prob_ge = 0
            log_prob_fr = 0
            f.write('BIGRAM MODEL:\n\n')
            print('BIGRAM MODEL:')
            for c in range(0, len(sentence) - 1):
                index_i = sentence[c]
                index_j = sentence[c + 1]
                prob_en_bi = EN_Bi.cond_probs['(' + (index_i) + '|' + (index_j) + ')']
                prob_fr_bi = FR_Bi.cond_probs['(' + (index_i) + '|' + (index_j) + ')']
                prob_ge_bi = GE_Bi.cond_probs['(' + (index_i) + '|' + (index_j) + ')']
                log_prob_en += math.log(prob_en_bi, 10)
                log_prob_fr += math.log(prob_fr_bi, 10)
                log_prob_ge += math.log(prob_ge_bi, 10)
                f.write('BIGRAM MODEL: ' + sentence[c] + sentence[c + 1] + '\n')
                f.write('FRENCH: P(' + sentence[c + 1] + '|' + sentence[c] + ') = ' + str(
                    prob_fr_bi) + ' ==> log prob of sentence so far: ' + str(log_prob_fr) + '\n')
                f.write('ENGLISH: P(' + sentence[c + 1] + '|' + sentence[c] + ') = ' + str(
                    prob_en_bi) + ' ==> log prob of sentence so far: ' + str(log_prob_en) + '\n')
                f.write('GERMAN: P(' + sentence[c + 1] + '|' + sentence[c] + ') = ' + str(
                    prob_ge_bi) + ' ==> log prob of sentence so far: ' + str(log_prob_ge) + '\n\n')
                if print_all:
                    print('BIGRAM MODEL: ' + sentence[c] + sentence[c + 1])
                    print('FRENCH: P(' + sentence[c + 1] + '|' + sentence[c] + ') = ' + str(
                        prob_fr_bi) + ' ==> log prob of sentence so far: ' + str(log_prob_fr))
                    print('ENGLISH: P(' + sentence[c + 1] + '|' + sentence[c] + ') = ' + str(
                        prob_en_bi) + ' ==> log prob of sentence so far: ' + str(log_prob_en))
                    print('GERMAN: P(' + sentence[c + 1] + '|' + sentence[c] + ') = ' + str(
                        prob_ge_bi) + ' ==> log prob of sentence so far: ' + str(log_prob_ge))
            maximum = max(log_prob_en, log_prob_ge, log_prob_fr)
            if log_prob_en == maximum:
                f.write('According to the bigram model, the sentence is in English\n\n')
                print('According to the bigram model, the sentence is in English\n\n')
            elif log_prob_fr == maximum:
                f.write('According to the bigram model, the sentence is in French\n\n')
                print('According to the bigram model, the sentence is in French\n\n')
            elif log_prob_ge == maximum:
                f.write('According to the bigram model, the sentence is in German\n\n')
                print('According to the bigram model, the sentence is in German\n\n')


def plot_model_matrix(matrix, model_name):
    plt.imshow(matrix)
    xy = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
          't',
          'u', 'v', 'w', 'x', 'y', 'z']
    plt.title(model_name)
    plt.xticks(range(len(xy)), xy, fontsize=16)
    plt.yticks(range(len(xy)), xy, fontsize=16)
    plt.colorbar()
    plt.show()


def plot_uni_model(uni_dict, name):
    lists = sorted(uni_dict.items())
    x, y = zip(*lists)
    plt.bar(x, y)
    plt.title(name)
    plt.show()


files_en = ['en-moby-dick.txt', 'en-the-little-prince.txt']
model_EN_Un = Models.Unigram(files_en)
model_EN_Un.write_file_lang_model(model_EN_Un.probs_alpha, 'unigramEN.txt')

files_fr = ['fr-le-petit-prince.txt', 'fr-vingt-mille-lieues-sous-les-mers.txt']
model_FR_Un = Models.Unigram(files_fr)
model_FR_Un.write_file_lang_model(model_FR_Un.probs_alpha, 'unigramFR.txt')

files_ge = ['German1.txt', 'German2.txt']
model_GE_Un = Models.Unigram(files_ge)
model_GE_Un.write_file_lang_model(model_GE_Un.probs_alpha, 'unigramOT.txt')


# with open('input.txt', 'r') as f:
#     lines = f.readlines()
# sentences = [x.strip() for x in lines]

sentences = ["Kate sang."]
# for sentence in sentences:
#     print(sentence)

model_EN_Bi = Models.Bigram(files_en)
model_EN_Bi.write_file_lang_model(model_EN_Bi.cond_probs, 'bigramEn.txt')
model_FR_Bi = Models.Bigram(files_fr)
model_FR_Bi.write_file_lang_model(model_FR_Bi.cond_probs, 'bigramFR.txt')
model_GE_Bi = Models.Bigram(files_ge)
model_GE_Bi.write_file_lang_model(model_GE_Bi.cond_probs, 'bigramGE.txt')

for i in range(0, len(sentences)):
    WriterFile.write_file_output(sentences[i], (i + 1), model_EN_Un, model_FR_Un, model_GE_Un,
                                 model_EN_Bi, model_FR_Bi, model_GE_Bi, False)
    # prob_en = model_EN_Un.calc_prob_unigram(sentences[i])
    # prob_fr = model_FR_Un.calc_prob_unigram(sentences[i])
    # prob_ge = model_GE_Un.calc_prob_unigram(sentences[i])
    # prob_map = {'EN': prob_en, 'FR': prob_fr, 'GE': prob_ge}
    # sorted_list = sorted(prob_map.items(), key=operator.itemgetter(1), reverse=True)
    # sorted_map = dict(sorted_list)
    # print(sentence, sorted_map[list(sorted_map.keys())[0]])
    # print(sentences[i], next(iter(sorted_map)))
    # print(sorted_map)

# EN_matrix_tp = [[row[i] for row in model_EN_Bi.bigram_matrix] for i in range(len(model_EN_Bi.bigram_matrix[0]))]
# FR_matrix_tp = [[row[i] for row in model_FR_Bi.bigram_matrix] for i in range(len(model_FR_Bi.bigram_matrix[0]))]
# GE_matrix_tp = [[row[i] for row in model_GE_Bi.bigram_matrix] for i in range(len(model_GE_Bi.bigram_matrix[0]))]
#
# plot_model_matrix(EN_matrix_tp, 'English Bigram Model')
# plot_model_matrix(FR_matrix_tp, 'French Bigram Model')
# plot_model_matrix(GE_matrix_tp, 'German Bigram Model')
#
# plot_uni_model(model_EN_Un.probs_alpha, 'English Unigram Model')
# plot_uni_model(model_FR_Un.probs_alpha, 'French Unigram Model')
# plot_uni_model(model_GE_Un.probs_alpha, 'German Unigram Model')

