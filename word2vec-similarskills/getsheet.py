from data import skills_list
from itertools import chain
from gensim.models import Word2Vec
from sampledata import sample_skills
import random
from allskills import flat_skills_list

similar_skills_dict = {}
# flat_skills_list = list(chain.from_iterable(skills_list))
#
# random_skills = random.sample(flat_skills_list, 50)

model = Word2Vec.load('word2vec.model')

for skill in flat_skills_list:

    sim_skills = model.wv.most_similar(skill, topn=5)

    similar_skills = [skill+f'({_})' for skill, _ in sim_skills]

    similar_skills_dict[skill] = similar_skills

# print(similar_skills_dict)

