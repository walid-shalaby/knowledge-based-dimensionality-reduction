
# coding: utf-8

## 20ng global definitions

# In[ ]:

from sets import Set
max_labels = 1 # use only top 1 probabilities labels as maximum labels per doc is 1
min_df = 1
max_df = 1.0
min_tf = 1
#test_set_size = 0.20
#max_chi_square_terms = 10000
db_path = '../../../data/ng20/ng20.db'
train_or_test_values = Set(['train','test','both'])
vocabulary_src_values = Set(['all','title','body'])
