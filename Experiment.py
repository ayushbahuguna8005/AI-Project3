from collections import defaultdict
import Models
import math


def generate_trigram_model(text):
    model = defaultdict(lambda: defaultdict(lambda: 0))
    for i in range(0, len(text) - 2):
        w1 = text[i]
        w2 = text[i + 1]
        w3 = text[i + 2]
        model[(w1, w2)][w3] += 1
    for w1_w2 in model:
        total_count = float(sum(model[w1_w2].values()))
        for w3 in model[w1_w2]:
            model[w1_w2][w3] = (model[w1_w2][w3]) / total_count

    return model


def predict_Language(sentence_test):
    sentence = Models.LanguageModel.clean_sentence(sentence_test)
    sentence = " ".join(sentence)
    prob_en = 0
    prob_fr = 0
    prob_ge = 0
    for w in range(0, len(sentence) - 2):
        w1 = sentence[w]
        w2 = sentence[w + 1]
        w3 = sentence[w + 2]
        prob_en += math.log(trigram_En[w1, w2][w3], 10)
        prob_fr += math.log(trigram_Fr[w1, w2][w3], 10)
        prob_ge += math.log(trigram_Ge[w1, w2][w3], 10)
    maximum = max(prob_en, prob_ge, prob_fr)
    # print(maximum)
    # print(prob_en)
    # print(prob_fr)
    # print(prob_ge)
    if maximum == prob_en:
        print('Trigam model:', sentence_test, 'English')
    elif maximum == prob_fr:
        print('Trigam model:', sentence_test, 'French')
    elif maximum == prob_en:
        print('Trigam model:', sentence_test, 'German')


files_en = ['en-moby-dick.txt', 'en-the-little-prince.txt']
model_En = Models.LanguageModel(files_en)
space_separated_en_text = " ".join(model_En.text)
trigram_En = generate_trigram_model(space_separated_en_text)

files_fr = ['fr-le-petit-prince.txt', 'fr-vingt-mille-lieues-sous-les-mers.txt']
model_Fr = Models.LanguageModel(files_fr)
space_separated_fr_text = " ".join(model_Fr.text)
trigram_Fr = generate_trigram_model(space_separated_fr_text)

files_ge = ['German1.txt', 'German2.txt']
model_Ge = Models.LanguageModel(files_ge)
space_separated_ge_text = " ".join(model_Ge.text)
trigram_Ge = generate_trigram_model(space_separated_ge_text)

sentences = ["What will the Japanese economy be like next year?", "She asked him if he was a student at this school.",
             "I'm OK.", "Birds build nests.", "I hate AI.", "L’oiseau vole.", "Woody Allen parle.",
             "Est-ce que l’arbitre est la?",
             "Cette phrase est en anglais.", "J’aime l’IA."]

for sentence in sentences:
    predict_Language(sentence)
