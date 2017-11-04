from glove import Glove
import pickle
import tensorflow as tf

with open('text8', 'r', encoding='utf-8') as f:
    corpus = f.readlines()

glove = pickle.load(open('glove.pkl', 'rb'))
#glove = Glove(verbose=1)
#glove.fit_corpus(corpus, 10, 1000)
#glove.save()
print("Training")
sess = tf.Session()
glove.train_tf(sess, 100, 0.05, 100, 0.75, 100)
#print(glove.most_similar(['were', 'are'], ['was'], topn=50))
print(glove.most_similar('he'))
