import sys,tweepy,csv,re
from textblob import TextBlob
# class sentiment analysis is called by the main function.
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
                                              
                        self.tweets = tweepy.Cursor(api.search, q = ar[i], lang = "en",since = data_from_date, place_id = lc[j]).items(NoOfTerms)
                                        
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
                                
def Sort(res): 
    # key is set to sort using second element of sublist lambda has been used 
    res.sort(reverse = True, key = lambda x: x[1]) 
    return res
  
                    
if __name__== "__main__":
 
 NoOfTerms = int(input("Enter how many tweets to search: "))
 data_from_date = input("Enter the date in the yyyy-mm-dd format:")
 ar = ["iPhone","OnePlus","Samsung"]
 lc = ["New York","San Francisco","Chicago","Bangalore","Mumbai","London"]
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
     
