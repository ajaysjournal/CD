import re
import numpy as np

stop_words = ({'a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren',
              'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can',
              'couldn', 'd', 'did', 'didn', 'do', 'does', 'doesn', 'doing', 'don', 'down', 'during', 'each', 'few',
              'for', 'from', 'further', 'had', 'hadn', 'has', 'hasn', 'have', 'haven', 'having', 'he', 'her', 'here',
              'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'isn', 'it', 'its',
              'itself', 'just', 'll', 'm', 'ma', 'me', 'mightn', 'more', 'most', 'mustn', 'my', 'myself', 'needn', 'no',
              'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves',
              'out', 'over', 'own', 're', 's', 'same', 'shan', 'she', 'should', 'shouldn', 'so', 'some', 'such', 't',
              'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this',
              'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was', 'wasn', 'we', 'were',
              'weren', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', 'wouldn',
              'y', 'you', 'your', 'yours', 'yourself', 'yourselves'})


class word:
    def __init__(self, w_id, text, is_keyword):
        self.w_id = w_id
        self.text = text
        self.is_keyword = is_keyword

    def __str__(self):
        return f"id : {self.w_id} \ntext : {self.text}  \nis_keyword : {self.is_keyword}"




def make_word_fragments(text):
    words = []
    text = re.sub(' +', ' ', text).split(' ')
    for i in range(len(text)):
        words.append(word(str(i), text[i], not is_keyword(text[i])))
    return words


def is_keyword(text):
    # todo to improve the User expierence
    # r = np.random.randint(100) < 50
    # we have to refine this.
    return text in stop_words