from gensim.models import Word2Vec
from data import skills_list
print('getting data from skills list')
# Prepare your tokenized corpus
tokenized_corpus = skills_list
print('model is training.....')
# Initialize and train the Word2Vec model with different parameters
model = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=150, window=5, min_count=5, workers=4, epochs=100, sg=0
)

# Save the third round of fine-tuned model
model.save("word2vec.model")


