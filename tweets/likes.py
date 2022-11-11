import tweepy
import pandas as pd
import csv
import time

# api_key="6BU82KJHCSH8mCdqUb9Tjs3Nh"
# api_key_secret="6h10LWIJ6mt7oYTOEouJGaYbvdhOKEhCFLXOiuhW0cdVaXQro8"
# access_token="1445948833930694657-WHGpPgnDAXyiZAEbvAV0R3Imy9Byyr"
# access_token_secret="UBEFbcgbFtmRr82eYyxxJoSBlBZ73AbH2OnJo5cNpSiha"
# bearer_token="AAAAAAAAAAAAAAAAAAAAAJkRiAEAAAAABiLqyhHgxiRwraCUS2pfrapk8wU%3Dqiv4nnyWwr7FFSSKAbric3Xg4t62W3XcVcuIegSsNUdamw6pxi"

api_key = "HBsZvZD9TX4cfJgnKGcs2SbBp"
api_key_secret = "b1QnHzvCaKKAn3abfYgWAs8VphUnsApCuHB5AvWMT804tkrdCl"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIh7hwEAAAAAPesav0XTuQ7KZGV5Kfbf76o46oA%3Dg1sG5Mrg1rx7ynNO7hWvwtg770NYSHBW98twlhQGo5Ph3oie0F"
access_token = "1569605362122371072-bjOAhAf40VPOPax7iK0fyguPQd9h1k"
access_token_secret = "BQisgCyxE8VZFdXN7JbyLzXj20uyzGUh8jxBq3aDxiZto"

# api_key = "TE0N3C9CKOnI8QZzm7yoDwngz"
# api_key_secret = "uRX4rN8o62p9qenC3pAboDWvcDYSEndWFXtCMlG3NPGCstPYB9"
# bearer_token = "AAAAAAAAAAAAAAAAAAAAAHD9igEAAAAAq9kvRyjvjcpRYMuzlbQPoNmmwxM%3DeZcVmbNdWWLVs1qW4zYKF8rp52Md57t7CsoMBd0n7HRbAw3V15"
# access_token = "1586680260409466880-0jJvhHOx5TL86ARodlkKUZfDs5Rsj6"
# access_token_secret = "qgRND8cuB38Ojfctygx7wF6ZR3toxb2ZGsIF6bgHwkI1i"


# authorization of consumer key and consumer secret
client=tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

with open("influ_likes_10.csv","a",encoding='gb18030',newline='') as csvfile: 
    writer = csv.writer(csvfile)
    f = open("full_neighbors.txt")               # 返回一个文件对象 
    line = f.readline()               # 调用文件的 readline()方法
    c=1 
    while line: 
        if c<10:
            c+=1 
            line = f.readline()
            continue
        print("count line: ",c)
        influ,subs=line.split()
        influ=str(influ)
        print("influ  "+influ)
        tweets = client.get_users_tweets(id=influ,max_results=20)
        tweets_data = list(tweets.data)
        likes=[]
        n=min(20,len(tweets_data))
        i=0
        while i<n:
            tid=tweets_data[i].id
            likeofone=0
            try:
                res=client.get_liking_users(id=tid)
                resmeta=res.meta
                likeofone+=resmeta['result_count']
                print(resmeta['result_count'])
                while 'next_token' in resmeta:
                    token=res.meta['next_token']
                    try:
                        res=client.get_liking_users(id=tid,pagination_token=token)
                        resmeta=res.meta
                        likeofone+=resmeta['result_count']
                        print(resmeta['result_count'])
                    except Exception as e:
                        print(str(e))
                        if str(e)=='429 Too Many Requests':
                            print('sleep 5 mintues')
                            time.sleep(300)
                print('like of one: ',likeofone)
                likes.append(likeofone)            
                i+=1
            except Exception as e:
                print(str(e))
                if str(e)=='429 Too Many Requests':
                    print('sleep 5 mintues')
                    time.sleep(300)
                else:
                    i+=1
        row=[influ,likes]
        writer.writerow(row)
        c+=1
        line = f.readline() 
     
    f.close()