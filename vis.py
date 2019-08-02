In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
# print(tweetData)
# Continue your program below!

# Get TextBlob
ls = [[], []]
for each in tweetData:
    tweet = each["text"]
    tb = TextBlob(tweet)
    ls[0].append(tb.polarity)
    ls[1].append(tb.subjectivity)

# Diagrams
def diagram(ls):
    f = plt.figure(1)
    plt.hist(ls[0], bins = 20)
    plt.xlabel("Polarity")
    plt.ylabel("Frequency")
    plt.title("Tweet polarity")
    f.show()
    f.savefig("tweet_polarity.png")

    g = plt.figure(2)
    plt.hist(ls[1], bins = 20)
    plt.xlabel("Subjectivity")
    plt.ylabel("Frequency")
    plt.title("Tweet subjectivity")
    g.show()
    f.savefig("tweet_subjectivity.png")

    h = plt.figure(3)
    plt.scatter(ls[0], ls[1])
    plt.xlabel("Polarity")
    plt.ylabel("Subjectivity")
    plt.title("polarity vs. subjectivity")
    h.show()
    h.savefig("polarity vs. subjectivity.png")

    input()

# Word Cloud by Frequency
def word_cloud_freq(tweetData):
    all_text = ""
    word_count = {}
    for each in tweetData:
        all_text += each["text"]
    all_text = all_text.lower()
    atb = TextBlob(all_text)
    word_list = atb.words
    for each in word_list:
        if len(each) > 3 and each.isalpha() == True and each != "https":
            if each not in word_count:
                word_count[each] = 1
            else:
                word_count[each] += 1
    wc = WordCloud(background_color="white", width=900,height=500,
    relative_scaling=1).generate_from_frequencies(list(word_count.items()))
    plt.imshow(wc, interpolation='bilinear')
    plt.show()

# Combined word cloud
word_cloud_freq(tweetData)
