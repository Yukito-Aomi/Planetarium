# -*- coding: utf-8 -*-


from direct.showbase.ShowBase import ShowBase
from panda3d.core import *


class Planetarium(ShowBase):
    """
    プラネタリウムを作成するクラス
    """
    # デフォルトのウィンドウ・タイトル
    DEFAULT_WINDOW_TITLE = 'Planetarium'
    # デフォルトのウィンドウ・サイズ（縦幅／横幅）
    DEFAULT_WINDOW_SIZE = (640, 480)

    # 地球のモデル
    MODEL_EARTH = 'misc/sphere'
    # 軸のモデル
    MODEL_AXIS = 'zup-axis'

    def __init__(self, window_size: tuple[int] = DEFAULT_WINDOW_SIZE, window_title: str = DEFAULT_WINDOW_TITLE) -> None:
        """
        コンストラクタ
        """
        # スーパークラスの初期化
        ShowBase.__init__(self)

        # ウィンドウの設定
        self.props = WindowProperties()
        self.props.setTitle(window_title)
        self.props.setSize(window_size)
        self.win.requestProperties(self.props)
        self.setBackgroundColor(0, 0, 0)  # 黒色

        # 地球の追加
        self.earth = self.loader.loadModel(self.MODEL_EARTH)
        self.earth.setColor(0, 0, 1)  # 青色
        self.earth.reparentTo(self.render)
        # 座標軸の追加
        self.axis = self.loader.loadModel(self.MODEL_AXIS)
        self.axis.reparentTo(self.render)

    def __del__(self) -> None:
        """
        デストラクタ
        """
        pass
