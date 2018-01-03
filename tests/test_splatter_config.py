#coding:UTF-8
"""
SplatterConfigクラスのテストプログラム
"""

import os
import sys
import logging
import logging.config
sys.path.append(os.pardir)
from SplatterConfig import SplatterConfig

def main():
    """ テストのメイン処理 """
    # Loggerの定義
    logging.config.fileConfig('test_logging.conf')
    logger = logging.getLogger()

    # 本番同様にファイル読み込みを行うため、１つ上の階層に移動する。
    #os.chdir('../')
    test_get_search_list(SplatterConfig(), logger)

def test_get_search_list(a_s_config=SplatterConfig(), a_logger=logging.getLogger()):
    """ get_search_listのテスト関数 """
    a_logger.debug('start test_get_search_list')
    search_list = a_s_config.get_search_list()

    for index, item in enumerate(search_list):
        a_logger.debug(msg='index' + str(index) + ' : ' + str(item))

    a_logger.debug('end test_get_search_list')

if __name__ == '__main__':
    main()
