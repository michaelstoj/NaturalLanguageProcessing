# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:28:55 2023

@author: mikes
"""

import nltk
from nltk.tokenize import word_tokenize

# Define the two articles to compare
article1 = "Fresh Tracks Therapeutics Announces Positive Topline Results from Single and Multiple Ascending Dose Parts of Phase 1 Study of Oral DYRK1A Inhibitor FRTX-02"
article2 = "Avenue Therapeutics Provides Regulatory Update on IV Tramadol and Other Corporate Updates"

# Tokenize the articles into sets of words
set1 = set(word_tokenize(article1.lower()))
set2 = set(word_tokenize(article2.lower()))

# Calculate the Jaccard similarity between the sets
jaccard_similarity = len(set1.intersection(set2)) / len(set1.union(set2))

# Print the Jaccard similarity
print("Jaccard similarity between the two articles: ", jaccard_similarity)
