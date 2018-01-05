#coding:UTF-8
"""
jsonデータの取扱を行うクラス。
"""
import json

class SplatterConfig:
    """
    ・指定したファイルの値を返すメソッドを提供する。
    ・判定の上で返却が必要な値については判定結果を返却する。
    """

    #定数定義
    #jsonファイル名
    filename = 'config.json'

    #json param name (twitter)
    jpn_twt = 'twitter'

    #json param name (LINE)
    jpn_line = 'line_notify'

    def __init__(self):
        """ jsonファイルの読み込みを行う """
        json_file = open(self.filename, 'r', encoding='utf-8')
        self.json_dist = json.load(json_file)

    def get_param(self, sent1, sent2):
        """ jsonデータを返却する """
        return str(self.json_dist[sent1][sent2])

    def get_param_twt(self, sent):
        """ twitterのデータを指定して返却する """
        return str(self.get_param(self.jpn_twt, sent))

    def get_param_line(self, sent):
        """ LINEのデータを指定して返却する """
        return str(self.get_param(self.jpn_line, sent))

    def get_target_notify(self):
        """ LINEの通知先を返すメソッド """
        return self.get_param(sent1=self.jpn_line,
                              sent2=self.get_param(sent1=self.jpn_line
                                                   , sent2="notify_level"))

    def get_search_list(self):
        """ 検索対象の文字列を配列で返却する。 """
        return str(self.json_dist['search_string']).split(',')
        