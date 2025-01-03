import math
from collections import Counter
from utils import cosine_similarity


def main(sentences):
    # get tf score
    global_counter = Counter()
    for sentence in sentences:
        words = sentence.lower().split()
        global_counter.update(words)

    word2idx = {word: i for i, word in enumerate(global_counter.keys())}
    document_frequency = {word: 0 for word in global_counter.keys()}
    vector_per_doc = {}

    # get tf score of each sentence
    for sentence in sentences:
        words = sentence.lower().split()
        vector_per_doc[sentence] = [0] * len(word2idx)
        for word in words:
            vector_per_doc[sentence][word2idx[word]] += 1
        for word in set(words):
            document_frequency[word] += 1

    for sentence in sentences:
        for word, idx in word2idx.items():
            tf = vector_per_doc[sentence][idx]
            if document_frequency[word] == 0:
                tf_idf = 0
            else:
                tf_idf = tf * math.log(len(sentences) / document_frequency[word])
            vector_per_doc[sentence][idx] = tf_idf

    first_sentence = vector_per_doc[sentences[0]]

    for sentence in sentences[1:]:
        second_sentence = vector_per_doc[sentence]
        similarity = cosine_similarity(first_sentence, second_sentence)
        print(f"Similarity between `{sentences[0]}` and `{sentence}`: {similarity:.4f}")


if __name__ == "__main__":
    sentences = [
        "I'd like an apple.",
        "An apple a day keeps the doctor away.",
        "Never compare an apple to an orange.",
        "I prefer scikit-learn to orange.",
    ]

    main(sentences)
