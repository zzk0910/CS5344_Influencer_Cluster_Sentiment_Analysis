import tweepy
import pandas as pd
import csv
import time

api_key = "HBsZvZD9TX4cfJgnKGcs2SbBp"
api_key_secret = "b1QnHzvCaKKAn3abfYgWAs8VphUnsApCuHB5AvWMT804tkrdCl"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIh7hwEAAAAAPesav0XTuQ7KZGV5Kfbf76o46oA%3Dg1sG5Mrg1rx7ynNO7hWvwtg770NYSHBW98twlhQGo5Ph3oie0F"
access_token = "1569605362122371072-bjOAhAf40VPOPax7iK0fyguPQd9h1k"
access_token_secret = "BQisgCyxE8VZFdXN7JbyLzXj20uyzGUh8jxBq3aDxiZto"
client=tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

with open("top50_test.csv","a",encoding='gb18030',newline='') as csvfile: 
    writer = csv.writer(csvfile)
    f = open("top50_neighbors.txt")               # 返回一个文件对象 
    line = f.readline()               # 调用文件的 readline()方法
    c=1 
    while line: 
        print("count line: ",c)
        influ,subs=line.split()
        subs=list(subs.split(','))

        subs.insert(0,str(influ))
        ids=subs
        center=influ
        print(influ,subs)

        for j in range(len(ids)):
            id=ids[j]
            print("id  "+id+"  "+str(j)+"/"+str(len(ids)))
            try:
                row=[id,center]
                tweets = client.get_users_tweets(id=id,max_results=50)
                tweets_data = list(tweets.data)
                print(tweets_data)
                # print(tweets)
                text_list=[None]*50
                for i in range(min(50,len(tweets_data))):
                    text_list[i]=tweets_data[i].text
                writer.writerow(row+text_list)
            except Exception as e:
                print(str(e))
                if str(e)=='429 Too Many Requests':
                    print('sleep 5 mintues')
                    time.sleep(300)
        c+=1
        line = f.readline() 
     
    f.close()