# -*- coding: utf-8 -*-


from direct.showbase.ShowBase import ShowBase
from panda3d.core import *


class Planetarium(ShowBase):
    """
    プラネタリウムを作成するためのクラス
    """
    # デフォルトのウィンドウ・タイトル
    DEFAULT_WINDOW_TITLE = 'Planetarium'
    # デフォルトのウィンドウ・サイズ（縦幅／横幅）
    DEFAULT_WINDOW_SIZE = (640, 480)

    # 地球のモデル
    MODEL_EARTH = 'misc/sphere'
    # 座標軸のモデル
    MODEL_AXIS = 'zup-axis'

    def __init__(self, size: tuple[int, int] = DEFAULT_WINDOW_SIZE, title: str = DEFAULT_WINDOW_TITLE) -> None:
        """
        コンストラクタ
        :param size: ウィンドウのサイズ（縦幅／横幅）
        :param title: ウィンドウのタイトル
        """
        # ShowBase の初期化
        ShowBase.__init__(self)

        # ウィンドウの設定
        self.props = WindowProperties()
        self.props.set_title(title)
        self.props.set_size(size)
        self.win.request_properties(self.props)
        self.set_background_color(0, 0, 0)  # 黒色

        # 地球の追加
        self.earth = self.loader.load_model(self.MODEL_EARTH)
        self.earth.set_color(0, 0, 1)  # 青色
        self.earth.reparent_to(self.render)
        # 座標軸の追加
        self.axis = self.loader.load_model(self.MODEL_AXIS)
        self.axis.reparent_to(self.render)
