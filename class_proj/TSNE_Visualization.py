#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Expended_X from CSC2515 Final Project Source Code
expanded_X, group_idxs, target = expand_data(kid_data)
X = expanded_X.to_numpy(np.float64)


from sklearn.manifold import TSNE
X_embedded = TSNE(n_components=3, learning_rate='auto',
                  init='random', perplexity=3).fit_transform(X)


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt

new_labels = ['Graduated','Dropout','Extended Length Degree']
ax = sns.scatterplot(x= X_embedded[:,0], y = X_embedded[:,1],  hue=y, palette="deep")
L = plt.legend() #fontsize='6'
L.get_texts()[0].set_text('Graduated')
L.get_texts()[1].set_text('Dropout')
L.get_texts()[2].set_text('Extended Length Degree')
sns.move_legend(ax,"upper left", bbox_to_anchor=(1, 1))
plt.show()

