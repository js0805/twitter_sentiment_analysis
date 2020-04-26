
import sys,tweepy,csv,re
from textblob import TextBlob
import matplotlib.pyplot as plt

class SentimentAnalysis:
   
                    
                
                    def __init__(self):
                        self.tweets = []
                        self.tweetText = []
                
                    def DownloadData(self):
                        
                        consumerKey = '2NYmSxHedbEaGN1mlmjkZBHZk'
                        consumerSecret = 'U7IPpFr2IMIlDTarytGTWx6QIQI6o0W6XM8dCW7OK3cqG9SeZA'
                        accessToken = '1206443485659664384-VdlDbTk4WaDWeXI9eA8zQz4EIMKXxg'
                        accessTokenSecret = 'yff4j1bRDrO2QyinAKhlUFDuatxRb8U7SgO6Hmtw6ZnqJ'
                        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
                        auth.set_access_token(accessToken, accessTokenSecret)
                        api = tweepy.API(auth,wait_on_rate_limit=True)
                
                       
                        
                        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en",since=data_from_date,place_id = location).items(NoOfTerms)
                
                        
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
                
                        
                        positive = self.percentage(positive, NoOfTerms)
                       
                        negative = self.percentage(negative, NoOfTerms)
                       
                        neutral = self.percentage(neutral, NoOfTerms)
                
                        
                        polarity = polarity / NoOfTerms
                
                        
                        print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets in " + str(location) + '.')
                        print()
                        print("General Report: ")
                
                        if (polarity == 0):
                            print("Neutral")
                        
                        elif (polarity > 0 and polarity <= 1):
                            print("Positive")
                       
                        elif (polarity > -1 and polarity < 0):
                            print("Negative")
                
                        print()
                        print("Detailed Report: ")
                        print(str(positive) + "% people thought it was positive")
                    
                        print(str(negative) + "% people thought it was negative")
                      
                        print(str(neutral) + "% people thought it was neutral")
                
                        self.plotPieChart(positive,  negative,  neutral, searchTerm, NoOfTerms)
                
                    def cleanTweet(self, tweet):
                        
                        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())
                
                    
                    def percentage(self, part, whole):
                        temp = 100 * float(part) / float(whole)
                        return format(temp, '.2f')
                
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
 t = int(input("Enter the number of test cases to be tested:"))
 for i in range(1,t+1):
    searchTerm = input("Enter Keyword/Tag to search about: ")
    NoOfTerms = int(input("Enter how many tweets to search: "))
    data_from_date = input("Enter the date in the yyyy-mm-dd fromat:")
    location = input("Enter the geographical loaction for analysing tweets:")
    sa = SentimentAnalysis()
    sa.DownloadData()
