#coding:UTF-8
"""This is main program"""
import logging
import logging.config
import twitter
import requests
from SplatterConfig import SplatterConfig
from TimelineController import TimelineController

def main():
    """メイン関数"""
    # Logger設定
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger()

    # Configファイル読み込み用のクラスを定義
    spla_conf = SplatterConfig()

    # twitter用のAPIインスタンス取得。
    api = twitter.Api(consumer_key=spla_conf.get_param_twt('consumer_key')
                      , consumer_secret=spla_conf.get_param_twt('consumer_secret')
                      , access_token_key=spla_conf.get_param_twt('access_token_key')
                      , access_token_secret=spla_conf.get_param_twt('access_token_secret')
                      , cache=None)

    # SplatoonJPのタイムラインを取得し、最新のtweetをメッセージに設定。
    tl_controller = TimelineController(
        api.GetUserTimeline(user_id=int(spla_conf.get_param_twt('userid'))))
    message = tl_controller.get_new_tweet_text + '\n\n' \
              + spla_conf.get_param_twt('acct') + str(tl_controller.get_new_tweet_id)

    logger.info(msg='TweetID:' + str(tl_controller.get_new_tweet_id))

    # LINE通知を実施。
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + str(spla_conf.get_target_notify())}
    requests.post(spla_conf.get_param_line('api_url'), data=payload, headers=headers)

if __name__ == '__main__':
    main()
