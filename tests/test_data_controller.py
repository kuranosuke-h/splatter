#coding:UTF-8
"""
DataControllerクラスのテストプログラム
"""

import os
import sys
sys.path.append(os.pardir)
from DataController import DataController

def main():
    """ テストのメイン処理 """

    # 本番同様にファイル読み込みを行うため、１つ上の階層に移動する。
    os.chdir('../')
    dataobj = DataController()
    dataobj.get_base_unixtime()

if __name__ == '__main__':
    main()
