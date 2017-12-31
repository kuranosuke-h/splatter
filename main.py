#coding:UTF-8
"""This is main program"""
import twitter
import requests
from SplatterConfig import SplatterConfig

def main():
    """メイン関数"""
    # Configファイル読み込み用のクラスを定義
    spla_conf = SplatterConfig()

    # twitter用のAPIインスタンス取得。
    api = twitter.Api(consumer_key=spla_conf.get_param_twt('consumer_key')
                      , consumer_secret=spla_conf.get_param_twt('consumer_secret')
                      , access_token_key=spla_conf.get_param_twt('access_token_key')
                      , access_token_secret=spla_conf.get_param_twt('access_token_secret')
                      , cache=None)

    # SplatoonJPのタイムラインを取得し、最新のtweetをメッセージに設定。
    timeline = api.GetUserTimeline(user_id=int(spla_conf.get_param_twt('userid')))
    message = timeline[0].text + '\n\n' + spla_conf.get_param_twt('acct') + str(timeline[0].id)

    #取得したtweetをログ出力。
    print('TweetID:' + str(timeline[0].id))

    # LINE通知を実施。
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + str(spla_conf.get_target_notify())}
    requests.post(spla_conf.get_param_line('api_url'), data=payload, headers=headers)

if __name__ == '__main__':
    main()
