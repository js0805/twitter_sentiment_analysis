import sys,tweepy,csv,re
from tweepy import StreamListener
from textblob import TextBlob
import datetime

class TweetListener(StreamListener):
            def on_status(self, status):
                  startDate = datetime.datetime(2020,1,1)
                  stopDate = datetime.datetime(2020,1,2)
# class sestiment analysis is called by the main function.
# This class contains the function which access data requiring to fetching tweets..
#  .., cleaning the tweets from special characters and returning the number of tweets (positive, negative and neutral).
class SentimentAnalysis:         
                
                    

                    def __init__(self):
                        self.tweets = []
                        self.tweetText = []

      
                    
                    #This function is verifying the access of the twitter developer acccount and then fetching them using the variable api.
                    def DownloadData(self, i, j):
                        
                        consumerKey = '2NYmSxHedbEaGN1mlmjkZBHZk'
                        consumerSecret = 'U7IPpFr2IMIlDTarytGTWx6QIQI6o0W6XM8dCW7OK3cqG9SeZA'
                        accessToken = '1206443485659664384-VdlDbTk4WaDWeXI9eA8zQz4EIMKXxg'
                        accessTokenSecret = 'yff4j1bRDrO2QyinAKhlUFDuatxRb8U7SgO6Hmtw6ZnqJ'
                        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
                        auth.set_access_token(accessToken, accessTokenSecret)
                        api = tweepy.API(auth,wait_on_rate_limit=True)                
                                              
                        self.tweets = tweepy.Stream(auth,TweetListener(),secure = True,)
                        self.tweets.filter(track = ar[i])
                        self.tweets.filter(locations=lc[j])

                        csvFile = open('result.csv', 'a')
                                       
                        csvWriter = csv.writer(csvFile)
                                        
                        polarity = 0
                        positive = 0
                        
                        negative = 0
                      
                        neutral = 0
            #This funtion is classifying tweets through the words analysis by the TextBlob funtion.
                        for tweet in self.tweets:
                            
                            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
                            
                            analysis = TextBlob(tweet.text)
                            
                            polarity += analysis.sentiment.polarity  
                
                            if (analysis.sentiment.polarity == 0):  
                                neutral += 1
                            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 1):
                                positive += 1
                            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= 0):
                                negative += 1              
                        
                        csvWriter.writerow(self.tweetText)
                        csvFile.close()
                           
                        return [positive,negative,neutral]         
                                                                        
                #This function is simply removing the special symbols from the tweets.
                    def cleanTweet(self, tweet):
                        
                        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())
                                
                
                   


def compare(res):
    res1 = []
    res2 = res
    n = len(res)
    m = n
    for i in range(0,n):
      min = res[0][1]
      pos = 1
      for j in range(0,m):
        if(res[j][1] > min):
          min = res[j][1]
          pos = j
        elif(res[j][1] == min):
          if(res[j][2] < res[pos][2]):
            min = res[j][1]
            pos = j
          elif(res[j][2] == res[pos][2]):
            if(res[j][3] > res[pos][3]):
              min = res[j][1]
              pos = j
      res1.append(res[pos])
      h = res2.pop(pos)
      m = m-1
    return res1  




def Sort(res): 
    # key is set to sort using second element of sublist lambda has been used 
    res.sort(reverse = True, key = lambda x: x[1]) 
    return res
  
                    
if __name__== "__main__":
 

 ar = ["iPhone","OnePlus","Samsung"]
 lc = [[-74.25909,40.477399,-73.700181,40.916178],[-123.173825,37.640314,-122.28178,37.929844],[-87.940101,41.643919,-87.523984,42.023022],[75.23,9.46,79.95,16.4],[72.776333,18.893957,72.979731,19.270177],[-0.5104,51.2868,0.334,51.6919]]
 no_of_loc = len(lc)
 no_of_items = len(ar)
 
 for j in range(0,no_of_loc):
    location = lc[j]
    res = []
    
    for i in range(0, no_of_items):
       searchTerm = '#'+ar[i] 
       sa = SentimentAnalysis()
       list = sa.DownloadData(i,j)
       list1 = []
       list1.append(ar[i])
       for l in range(0,3):
         list1.append(list[l])
       res.append(list1)
       
    res1 = Sort(res)   
    print('Store '+lc[j])
    print(res1)
    print('Shipping priority')    
    
    k = 0
    x = 0
    h = 1
    ind = []
    for i in range(0,no_of_items):
      ind.append(0)
    

    while((x != no_of_items)&(k != no_of_items-1)):
      if((res[k][2] == res[k+1][2])&(res[k][3] == res[k+1][3])&(res1[k][1] == res1[k+1][1])):
          print(h,' - ',res1[k][0],' & ',res1[k+1][0])
          ind[k] = 1
          ind[k+1] = 1
          x = x+2
      elif(res1[k][1] == res1[k+1]):
        if(res1[k][2] > res1[k+1][2]):
          print(h,' - ',res1[k+1][0])
          ind[k+1] = 1
          x = x+1
        elif(res1[k][2] == res1[k][2]):
          if(res1[k][3] > res1[k+1][3]):
            print(h,' - ',res1[k][0])
            ind[k] = 1
            x = x+1
          else:  
            print(h,' - ',res1[k+1][0])
            ind[k+1] = 1
            x = x+1
        else:
          print(h,' - ',res1[k][0])   
          ind[k] = 1
          x = x+1
      else:    
          print(h,' - ',res1[k][0])
          ind[k] = 1
          x = x+1
      h = h+1
      k = k+1
    
    for z in range(0,no_of_items):
      
      if(ind[z] == 0):
        print(h,' - ',res1[z][0])
        h = h+1
    res.clear() 
    res1.clear()    
     
