import tweepy
import datetime
import csv
import twconfig
def gettwitterdata(keyword,dfile,sincedate,untildate):
    
    #認証情報
    CK = twconfig.CONSUMER_KEY
    CS = twconfig.CONSUMER_SECRET
    AT = twconfig.ACCESS_TOKEN
    ATS = twconfig.ACCESS_TOKEN_SECRET
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, ATS)
    
    api = tweepy.API(auth)
    
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
                                tweet.full_text.replace('\n',''),
                                tweet.favorite_count,
                                tweet.retweet_count])
    
    #print(sincedate+'_00:00:00_JST')
    #print(untildate+'_00:00:00_JST')
    
    #出力ファイル名
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")
    
    #ファイル出力
    with open(fname, "w",newline='',encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(["id","created_at","text","fav","RT"])
        writer.writerows(tweets_data)
    f.close

if __name__ == '__main__':

    #検索キーワードを入力  ※リツイートを除外する場合 「キーワード -RT 」と入力
    print ('====== Enter Serch KeyWord   =====')
    keyword = input('>  ')

    #出力ファイル名を入力(相対パス or 絶対パス)
    print ('====== Enter Tweet Data file =====')
    dfile = input('>  ')

    #検索する期間（自）
    print ('====== 検索する期間（自）「yyyy-mm-dd」 =====')
    sincedate = input('>  ')

    #検索する期間（至）
    print ('====== 検索する期間（至）「yyyy-mm-dd」 =====')
    untildate = input('>  ')

    gettwitterdata(keyword,dfile,sincedate,untildate)