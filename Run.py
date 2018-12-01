import Models
files_en = ['en-moby-dick.txt', 'en-the-little-prince.txt']
files_fr = ['fr-le-petit-prince.txt', 'fr-vingt-mille-lieues-sous-les-mers.txt']
model_EN = Models.Unigram(files_en)
# model_EN = Models.Unigram('en-the-little-prince.txt')
# model_FR = Models.Unigram(files_fr)
print(model_EN.probabilities_alpha())
# sen2 = "What will the Japanese economy be like next year?"
# sen3 = "She asked him if he was a student at this school."
# sen4 = "I'm OK."
# sen5 = "Birds build nests."
# sen6 = "I hate AI."
# sen7 = "L’oiseau vole."
# sen8 = "Woody Allen parle."
# sen9 = "Est-ce que l’arbitre est la?"
# sen0 = "Cette phrase est en anglais."
# sen = "J’aime l’IA."
#
# print(sen, "Prob in eng: ", model_EN.calc_prob_unigram(sen), "Prob in fre: ", model_FR.calc_prob_unigram(sen))
# print(sen2, "Prob in eng: ", model_EN.calc_prob_unigram(sen2), "Prob in fre: ", model_FR.calc_prob_unigram(sen2))
# print(sen3, "Prob in eng: ", model_EN.calc_prob_unigram(sen3), "Prob in fre: ", model_FR.calc_prob_unigram(sen3))
# print(sen4, "Prob in eng: ", model_EN.calc_prob_unigram(sen4), "Prob in fre: ", model_FR.calc_prob_unigram(sen4))
# print(sen5, "Prob in eng: ", model_EN.calc_prob_unigram(sen5), "Prob in fre: ", model_FR.calc_prob_unigram(sen5))
# print(sen6, "Prob in eng: ", model_EN.calc_prob_unigram(sen6), "Prob in fre: ", model_FR.calc_prob_unigram(sen6))
# print(sen7, "Prob in eng: ", model_EN.calc_prob_unigram(sen7), "Prob in fre: ", model_FR.calc_prob_unigram(sen7))
# print(sen8, "Prob in eng: ", model_EN.calc_prob_unigram(sen8), "Prob in fre: ", model_FR.calc_prob_unigram(sen8))
# print(sen9, "Prob in eng: ", model_EN.calc_prob_unigram(sen9), "Prob in fre: ", model_FR.calc_prob_unigram(sen9))
# print(sen0, "Prob in eng: ", model_EN.calc_prob_unigram(sen0), "Prob in fre: ", model_FR.calc_prob_unigram(sen0))

# model_EN = Models.Bigram('en-moby-dick.txt', 'en-the-little-prince.txt')
# model_FR = Models.Bigram('fr-le-petit-prince.txt', 'fr-vingt-mille-lieues-sous-les-mers.txt')
# print(model_EN.conditional_prob())
#
# sen2 = "What will the Japanese economy be like next year?"
# sen3 = "She asked him if he was a student at this school."
# sen4 = "I'm OK."
# sen5 = "Birds build nests."
# sen6 = "I hate AI."
# sen7 = "L’oiseau vole."
# sen8 = "Woody Allen parle."
# sen9 = "Est-ce que l’arbitre est la?"
# sen0 = "Cette phrase est en anglais."
# sen = "J’aime l’IA."
#
# print(sen, "Prob in eng: ", model_EN.calc_prob_bigram(sen), "Prob in fre: ", model_FR.calc_prob_bigram(sen))
# print(sen2, "Prob in eng: ", model_EN.calc_prob_bigram(sen2), "Prob in fre: ", model_FR.calc_prob_bigram(sen2))
# print(sen3, "Prob in eng: ", model_EN.calc_prob_bigram(sen3), "Prob in fre: ", model_FR.calc_prob_bigram(sen3))
# print(sen4, "Prob in eng: ", model_EN.calc_prob_bigram(sen4), "Prob in fre: ", model_FR.calc_prob_bigram(sen4))
# print(sen5, "Prob in eng: ", model_EN.calc_prob_bigram(sen5), "Prob in fre: ", model_FR.calc_prob_bigram(sen5))
# print(sen6, "Prob in eng: ", model_EN.calc_prob_bigram(sen6), "Prob in fre: ", model_FR.calc_prob_bigram(sen6))
# print(sen7, "Prob in eng: ", model_EN.calc_prob_bigram(sen7), "Prob in fre: ", model_FR.calc_prob_bigram(sen7))
# print(sen8, "Prob in eng: ", model_EN.calc_prob_bigram(sen8), "Prob in fre: ", model_FR.calc_prob_bigram(sen8))
# print(sen9, "Prob in eng: ", model_EN.calc_prob_bigram(sen9), "Prob in fre: ", model_FR.calc_prob_bigram(sen9))
# print(sen0, "Prob in eng: ", model_EN.calc_prob_bigram(sen0), "Prob in fre: ", model_FR.calc_prob_bigram(sen0))

