#coding:UTF-8
"""
DB代わりに使用するdata.jsonを取り扱うためのクラス。
"""
import json
import logging
import logging.config
from datetime import datetime

class DataController:
    """ クラス本体 """

    ## 定数定義
    # Logger
    logger = ''

    # jsonファイル名
    filename = 'data.json'

    # jsonファイルインスタンスの格納先変数
    json_file = ''

    # jsonデータ上の基準時刻の名称
    name_basetime = 'base_time'

    # 基準時刻のオブジェクト
    base_time = ''

    # 基準時刻のフォーマット
    base_time_format = '%Y/%m/%d %H:%M:%S'

    def __init__(self):
        """ コンストラクタ """
        # Logger設定
        logging.config.fileConfig('logging.conf')
        self.logger = logging.getLogger()

        # jsonファイルの読み込みを行う
        self.json_file = open(self.filename, 'r')
        self.json_dict = json.load(self.json_file)

        ## 時刻がjsonに設定されているかチェックし、設定されていない場合には現在時刻を設定しておく。
        #  jsonデータから時刻のオブジェクトを生成
        try:
            self.base_time = datetime.strptime(self.json_dict[self.name_basetime]
                                               , self.base_time_format)
        except ValueError:
            # 適切なフォーマットの値が取得できない場合は現在時刻を設定する。
            self.base_time = datetime.now().strftime(self.base_time_format)
            self.set_basetime(self.base_time)

        self.logger.debug(msg='基準値取得:' + str(self.base_time))

    def get_base_unixtime(self):
        """ json内のデータをunixtimeに変換して渡す。 """
        return self.base_time

    def set_basetime(self, a_base_time):
        """ unixtimeを引き渡し、timeの文字列としてjsonファイルに設定する。 """
        w_json_file = open(self.filename, 'w')
        self.json_dict[self.name_basetime] = a_base_time
        json.dump(self.json_dict, w_json_file)

    def __del__(self):
        """ デコストラクタ """
        # 生成した結果を書き込む
        try:
            w_json_file = open(self.filename, 'w')
            json.dump(self.json_dict, w_json_file)
        finally:
            pass
