# Sentiment Analysis of Big Data on Social and Political Events
**Final Year Project'16 [B.E.]**

Project Phase - 1 [PP1]
----------------------

###[Project Approval Presentation](https://github.com/suraj-jayakumar/capstoneproject/blob/master/PP1%20Project%20Approval/Project%20Review%20Presentation.pptx)

###[Project Review Presentation](https://github.com/suraj-jayakumar/capstoneproject/blob/master/PP1%20Project%20Approval/Project%20Review%20Presentation.pptx)

### [Literature Survey](https://github.com/suraj-jayakumar/capstoneproject/tree/master/PP1%20Literature%20Survey%20Review)

### [Report](https://github.com/suraj-jayakumar/capstoneproject/tree/master/PP1%20Report)

### [Pre-alpha]

#### Movie Sentiment HeartBeat
* Collect Tweets of particular movie and store it in .csv file
* Run NBayesClassifier.py first
* Run normalplot.py parallely to get sentiment heartbeat graph

#### Stream Tweets
Run GetTweets.py or newTwitterStream.py to stream tweets based on topic


Project Phase - 2 [PP2]
------------------------
## [Architecture Details](https://github.com/suraj-jayakumar/capstoneproject/blob/master/PP2%20src/T1.png)

* **Data Collection Center**
      - [Stream ~2000+ Tweets of a given user](https://github.com/suraj-jayakumar/capstoneproject/blob/master/PP2%20src/data_collection_center/StreamTweets.py)
      - [Stream ~2000+ Tweets for a given topic](https://github.com/suraj-jayakumar/capstoneproject/blob/master/PP2%20src/data_collection_center/TweetsByTopic.py)

* **Training Datsets Used**
      - [Huge Tweet Corpus - Classified](http://help.sentiment140.com/for-students/)
      - [University of Michigan Sentiment Analysis competition on Kaggle](https://inclass.kaggle.com/c/si650winter11)
      - [Twitter Sentiment Corpus by Niek Sanders](http://www.sananalytics.com/lab/twitter-sentiment/)

* **Preprocessing**
      - [Tweet Data Cleaning](https://github.com/suraj-jayakumar/sentiment-analysis/blob/master/src/supervised_learning/classifier_tweets/PreProcessing.py)     
* **Supervised Learning Model**
      - [Naive-Bayes Classifier for Tweets](https://github.com/suraj-jayakumar/sentiment-analysis/blob/master/src/supervised_learning/classifier_tweets/TrainData.py)
      - [Naive-Bayes Classifier for Articles](https://github.com/suraj-jayakumar/sentiment-analysis/blob/master/src/supervised_learning/classifier_articles/simpleNB)
      - [Multinomial Baysian Classifier using Term Frequency - Inverse Document Frequency [TF-IDF]  for Articles](https://github.com/suraj-jayakumar/sentiment-analysis/blob/master/src/supervised_learning/classifier_articles/multinomialNB)
      - [Long Short Term Memory [LSTM] with Word2Vector Model [word2vec]  for Articles](https://github.com/suraj-jayakumar/sentiment-analysis/blob/master/src/supervised_learning/classifier_articles/lstm_w2v)
      - [Long Short Term Memory [LSTM] with Document2Vector Model [doc2vec]  for Articles](https://github.com/suraj-jayakumar/sentiment-analysis/tree/master/src/supervised_learning/classifier_articles/lstm_d2v)
* **Visualization Center**
      - [Word Cloud Graph](https://github.com/suraj-jayakumar/sentiment-analysis/blob/master/src/visualization/wordcloud.py)
      - [Stacked Represenation of Postive and Negative Tweets](https://github.com/suraj-jayakumar/sentiment-analysis/blob/master/src/visualization/bar_stacked.py)
      - [Location Bubble Graph]()


&copy; 2015-2016 Suraj Jayakumar under [MIT License](https://github.com/suraj-jayakumar/capstoneproject/blob/master/LICENSE.txt "Title") 
