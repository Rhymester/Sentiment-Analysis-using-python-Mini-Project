import string
from collections import Counter
import matplotlib.pyplot as plt

text_init = open("read.txt", encoding = 'utf-8').read()
lc = text_init.lower()
cleaned_text = lc.translate(str.maketrans('','',string.punctuation))
tokens = cleaned_text.split()
print(tokens)
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

cleaned_lst=[]
for i in tokens:
    if i not in stop_words:
        cleaned_lst.append(i)

print(cleaned_lst)

emotion_list=[]
with open('emotions.txt', 'r') as file:
    for ln in file:
        cleared_line = ln.replace("\n", "").replace(",","").replace("'","").strip()
        word, emotion = cleared_line.split(':')
        if word in cleaned_lst:
            emotion_list.append(emotion)

print(emotion_list)
cnt = Counter(emotion_list)
print(cnt)


fig, ax1 = plt.subplots()
ax1.bar(cnt.keys(), cnt.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()