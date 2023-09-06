from gensim.models import Word2Vec


model = Word2Vec.load('word2vec.model')

sim_skills = model.wv.most_similar('python', topn=10)

similar_skills = [skill for skill, _ in sim_skills]

print(similar_skills)
