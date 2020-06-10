#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tweepy
import datetime
import csv
import codecs

def gettwitterdata(keyword,dfile,sincedate,untildate):

    #python で Twitter APIを使用するためのConsumerキー、アクセストークン設定
    Consumer_key = '5xFc5PTRff3CrjvPVXJhJJjlc'
    Consumer_secret = '6E9u8tORYuKIGaTFiYXSuO8GYuVIqSJtg5oevD7HB9CWwxnN9l'
    Access_token = '189916635-ph27PYBhxy3xR6oO0cXwNEpNlhon2EvnxNqG0fnl'
    Access_secret = 'AYozTKlULIZ2ZSkgz3Z5DLK83ZDQj74BRYz2s5YseOjSj'

    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    #検索キーワード設定 
    q = keyword

    #つぶやきを格納するリスト
    tweets_data =[]

    #カーソルを使用してデータ取得
    for tweet in tweepy.Cursor(api.search, 
                               q=q, 
                               count=100,
                               tweet_mode='extended',
                               lang='ja',
                               since=sincedate+'_00:00:00_JST', 
                               until=untildate+'_23:59:59_JST'
                              ).items():

            #つぶやきテキスト(FULL)を取得
            tweets_data.append([tweet.user.screen_name,
                                tweet.created_at + datetime.timedelta(hours=9),
                                "'" + tweet.full_text.replace("\n"," "),
                                tweet.favorite_count,
                                tweet.retweet_count,
                                #tweet.place.name,
                                #tweet.quote_count,
                                #tweet.reply_count,
                                #tweet.hashtags.text,
                                tweet.lang,
                                tweet.user.location,
                                "'" + tweet.user.description.replace("\n"," "),
                                tweet.user.followers_count,
                                tweet.user.verified,
                                tweet.user.friends_count,
                                tweet.user.statuses_count,
                                tweet.user.created_at])

    #print(sincedate+'_00:00:00_JST')
    #print(untildate+'_00:00:00_JST')

    #出力ファイル名
    fname= r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #ファイル出力
    with open(fname, "w",newline='',encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(["アカウント",
                         "作成日",
                         "ツイート",
                         "良いね数",
                         "リツイート数",
                         #"場所",
                         #"引用数",
                         #"返信数",
                         #"ハッシュタグ",
                         "言語",
                         "場所",
                         "アカウントの説明",
                         "フォロワー数",
                         "認証の有無",
                         "フォローしている数",
                         "ツイート数",
                         "アカウント作成日"])
        writer.writerows(tweets_data)
        f.close

if __name__ == '__main__':

    ##検索キーワードを入力  ※リツイートを除外する場合 「キーワード -RT 」と入力
    #print ('====== Enter Serch KeyWord   =====')
    #keyword = input('>  ')
    keyword = "paypay -rt"

    ##"検索する期間（自）
    #"print ('====== 検索する期間（自）「yyyy-mm-dd」 =====')
    sincedate = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')

    ##検索する期間（至）
    #print ('====== 検索する期間（至）「yyyy-mm-dd」 =====')
    untildate = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
    
    ##出力ファイル名を入力(相対パス or 絶対パス)
    #print ('====== Enter Tweet Data file =====')
    dfile = r"C:\twitter\text_analysis\tweet_data\paypay_"+ sincedate +".csv"

    gettwitterdata(keyword,dfile,sincedate,untildate)


# In[ ]:




