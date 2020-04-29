import sys,tweepy,csv,re
from textblob import TextBlob
import matplotlib.pyplot as plt

class SentimentAnalysis:         
                
                    def __init__(self):
                        self.tweets = []
                        self.tweetText = []
                
                    def DownloadData(self, i, j):
                        
                        consumerKey = '2NYmSxHedbEaGN1mlmjkZBHZk'
                        consumerSecret = 'U7IPpFr2IMIlDTarytGTWx6QIQI6o0W6XM8dCW7OK3cqG9SeZA'
                        accessToken = '1206443485659664384-VdlDbTk4WaDWeXI9eA8zQz4EIMKXxg'
                        accessTokenSecret = 'yff4j1bRDrO2QyinAKhlUFDuatxRb8U7SgO6Hmtw6ZnqJ'
                        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
                        auth.set_access_token(accessToken, accessTokenSecret)
                        api = tweepy.API(auth,wait_on_rate_limit=True)                
                                              
                        self.tweets = tweepy.Cursor(api.search, q=ar[i], lang = "en",since=data_from_date,place_id = lc[j]).items(NoOfTerms)
                                        
                        csvFile = open('result.csv', 'a')
                                       
                        csvWriter = csv.writer(csvFile)
                                        
                        polarity = 0
                        positive = 0
                        
                        negative = 0
                      
                        neutral = 0
                                  
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
                                                                        
                
                    def cleanTweet(self, tweet):
                        
                        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())
                                
                
                    def plotPieChart(self, positive,  negative, neutral, searchTerm, noOfSearchTerms):
                        labels = ['Positive [' + str(positive) + '%]',  'Neutral [' + str(neutral) + '%]',
                                  'Negative [' + str(negative) + '%]']
                        sizes = [positive, neutral, negative]
                        colors = ['lightgreen', 'gold', 'red']
                        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
                        plt.legend(patches, labels, loc="best")
                        plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets for ' + str(location) + '.')
                        plt.axis('equal')
                        plt.tight_layout()
                        plt.show()
                    
if __name__== "__main__":
 
 NoOfTerms = int(input("Enter how many tweets to search: "))
 data_from_date = input("Enter the date in the yyyy-mm-dd format:")
 ar = ["Samsung","OnePlus","iPhone"]
 lc = ["New York","San Francisco","Chicago","Bangalore","Mumbai","London"]
 
 
 for j in range(0,6):
    location = lc[j]
    res = []
    for i in range(0,3):
       searchTerm = '#'+ar[i] 
       sa = SentimentAnalysis()
       list1 = sa.DownloadData(i,j)
       res.append(list1)
    print('Store '+lc[j])
    print('Shipping priority')    
    ans = []
    
    if (res[0][0] == res[1][0]):
         if(res[0][0] > [2][0]):
           if(res[0][1] < res[1][1]):
             ans.append(ar[0])
             ans.append(ar[1])
             
           else:
             ans.append(ar[1])
             ans.append(ar[0])
           ans.append(ar[2])

         else:
           ans.append(ar[2])  
           if(res[0][1] < res[1][1]):
             ans.append(ar[0])
             ans.append(ar[1])
           else:
             ans.append(ar[1])
             ans.append(ar[0])

    if (res[0][0] == res[2][0]):
         if(res[0][0] > [1][0]):
           if(res[0][1] < res[2][1]):
             ans.append(ar[0])
             ans.append(ar[2])
             
           else:
             ans.append(ar[2])
             ans.append(ar[0])
           ans.append(ar[1])

         else:
           ans.append(ar[1])  
           if(res[0][1] < res[2][1]):
             ans.append(ar[0])
             ans.append(ar[2])
           else:
             ans.append(ar[2])
             ans.append(ar[0])

    if (res[1][0] == res[2][0]): 
         if(res[1][0] > [0][0]):
           if(res[1][1] < res[2][1]):
             ans.append(ar[1])
             ans.append(ar[2])
             
           else:
             ans.append(ar[2])
             ans.append(ar[1])
           ans.append(ar[0])

         else:
           ans.append(ar[0])  
           if(res[1][1] < res[2][1]):
             ans.append(ar[1])
             ans.append(ar[2])
           else:
             ans.append(ar[2])
             ans.append(ar[1]) 

    if ((res[0][0] > res[1][0])&(res[0][0] > res[2][0])):
         ans.append(ar[0])
         if(res[1][0] > res[2][0]):
           ans.append(ar[1])
           ans.append(ar[2])
         else:
           ans.append(ar[2])
           ans.append(ar[1])

    elif ((res[1][0] > res[0][0])&(res[1][0] > res[2][0])):  
         ans.append(ar[1])
         if(res[2][0] > res[0][0]):
           ans.append(ar[2])
           ans.append(ar[0])
         else:
           ans.append(ar[0])
           ans.append(ar[2])

    elif ((res[2][0] > res[0][0])&(res[2][0] > res[1][0])):  
         ans.append(ar[2]) 
         if(res[1][0] > res[0][0]):
           ans.append(ar[1])
           ans.append(ar[0])
         else:
           ans.append(ar[0])
           ans.append(ar[1])
    
    print('1 - ',ans[0])
    print('2 - ', ans[1])     
    print('3 - ',ans[2])
    
    
    res.clear()     
    ans.clear()  
    
