#coding:UTF-8
"""
TwitterTimelineの操作を行うコントローラ
"""
import twitter

class TimelineController:
    """ クラス本体 """
    ## 定数定義
    # Timeline
    timeline: twitter.Status = {twitter.Status()}

    def __init__(self, a_timelines: twitter.Status):
        """ コンストラクタ """

    def get_new_tweet_text(self) -> str:
        """ 最新のtweetを返却する """
        return str(list(self.timeline)[0].text)

    def get_new_tweet_id(self) -> int:
        """ 最新のtweetのIDを返却する """
        return list(self.timeline)[0].id

    def get_new_important_tweet_text(self) -> str:
        """ 最新の重要なtweertを返却する """

        ## timelineの末尾から検索する。

        return 'hoge'
