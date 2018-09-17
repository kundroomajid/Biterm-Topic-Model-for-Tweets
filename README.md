# Biterm-Topic-Model-for-Tweets
Implementation of Biterm Topic Model for short texts like tweets
 The origin BTM is in here: https://github.com/xiaohuiyan/BTM

Steps:
1. First we need to preprocess Tweets for this use PreprocessTweets.py 
   script to preprocess tweets and for stopword removal
2. Go to BTM-Java folder and run the java code as
   java BTM [data_path] [topic_num] [alpha] [beta] [iter_num] [instance_num]```

   * `[data_path]    string, path of training docs`
   * `[topic_num]    int, number of topics`
   * `[alpha]    double, Symmetric Dirichlet prior of P(z)`
   * `[beta]   double, Symmetric Dirichlet prior of P(w|z)`
   * `[iter_num]   int, number of iterations of Gibbs sampling`
   * `[instance_num]   int, number of times to run this program`

   Examples
    ========
   ```java BTM sample-data.txt 100 0.1 0.01 2000 1```

   After iterations are completed out put can be seen as
 
   Output
   ========
   * `'model-final.theta'  Doc*Topic matrix`
   * `'model-final.phi'  Topic*Word matrix`
   * `'model-final.twords'  top 20 words of each topics`
   * `'model-final.wordmap'  word dictionary`



3. model-final.wordmap file which contains word frequency matrix can be 
   used to generate WordClouds using WordCloud.py script.
