#coding:UTF-8
"""
TwitterTimelineの操作を行うコントローラ
"""

from datetime import datetime
import logging
import logging.config
import twitter
from DataController import DataController


class TimelineController:
    """ クラス本体 """
    ## 定数定義
    # Timeline
    timeline: list = {}

    # 検索対象の文字列
    search_list: list = {}

    # データ読み込み用のクラスをクラスを定義
    data_conf: DataController = None

    # Logger設定
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger()

    def __init__(self, a_timelines: list, a_search_list: list):
        """ コンストラクタ """
        self.timeline = a_timelines
        self.search_list = a_search_list
        self.data_conf = DataController()

    def get_new_tweet_text(self) -> str:
        """ 最新のtweetを返却する """
        return str(self.timeline[0].text)

    def get_new_tweet_id(self) -> int:
        """ 最新のtweetのIDを返却する """
        return self.timeline[0].id

    def get_new_important_tweet(self) -> twitter.Status:
        """ 最新の重要なtweert objを返却する """
        result: twitter.Status = None

        for tweet in self.timeline:
            # 基準時刻に一番近い通知対象のtweetを取得する。
            unixtime_tmp = self.data_conf.get_base_unixtime()
            #print(unixtime_tmp)
            #print(msg='hoge::' + str(unixtime_tmp.timestamp()))

            if tweet.created_at_in_seconds > unixtime_tmp.timestamp():
                # 基準時刻よりも新しいtweetは通知判定を行う。
                if self.check_text(tweet.text):
                    result = tweet
            else:
                # 基準時刻よりも古いtweetにたどり着いたらループは終了。
                break

        # 時刻設定を行う
        if result is not None:
            # 時刻を通知対象のtweetの時刻で上書きする
            self.logger.debug(msg="通知対象のtweet時刻で上書きします。")
            self.data_conf.set_basetime(datetime.fromtimestamp(result.created_at_in_seconds).strftime('%Y/%m/%d %H:%M:%S'))
        else:
            # 時刻設定がされていない場合、検索対象が見つかっていないため、現在時刻をセットする
            self.logger.debug(msg="現在時刻をセットします。")
            self.data_conf.set_basetime(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

        return result

    def check_text(self, text) -> bool:
        """ 対象のテキストに検索対象の文字列が含まれているかをチェックする。 """
        for item in self.search_list:
            if str(text).find(item) != -1:
                return True

        return False
