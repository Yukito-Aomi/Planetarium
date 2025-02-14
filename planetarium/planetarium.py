# -*- coding: utf-8 -*-

import platform

from direct.showbase.ShowBase import ShowBase
from panda3d.core import *

from .camera import Camera
from .celestial_sphere import CelestialSphere


class Planetarium(ShowBase):
    """
    プラネタリウムを作成するためのクラス
    """
    # ウィンドウ・サイズのデフォルト値（縦幅／横幅）
    DEFAULT_WINDOW_SIZE = (640, 480)
    # ウィンドウ・タイトルのデフォルト値
    DEFAULT_WINDOW_TITLE = 'Planetarium'
    # 天球における半径のデフォルト値
    DEFAULT_CELESTIAL_SPHERE_RADIUS = 100
    # 観測地点における緯度のデフォルト値
    DEFAULT_LOCATION_LATITUDE = 35

    # Windows におけるシステム・フォントのパス
    FONT_WINDOWS = '/c/Windows/Fonts/msgothic.ttc'
    # macOS におけるシステム・フォントのパス
    FONT_MAC = '/System/Library/Fonts/Hiragino Sans GB.ttc'

    # 地球のモデル
    MODEL_EARTH = 'misc/sphere'
    # 座標軸のモデル
    MODEL_AXIS = 'zup-axis'


    def __init__(self) -> None:
        """
        コンストラクタ
        """
        # ShowBase の初期化
        ShowBase.__init__(self)

        self.CELESTIAL_SPHERE_RADIUS = self.DEFAULT_CELESTIAL_SPHERE_RADIUS
        self.location_latitude = self.DEFAULT_LOCATION_LATITUDE

        # フォントの設定
        if platform.system() == 'Windows':
            self.font = self.loader.load_font(self.FONT_WINDOWS)
        else:
            self.font = self.loader.load_font(self.FONT_MAC)

        # ウィンドウの設定
        self.props = WindowProperties()
        self.props.set_size(self.DEFAULT_WINDOW_SIZE)
        self.props.set_title(self.DEFAULT_WINDOW_TITLE)
        self.win.request_properties(self.props)
        self.set_background_color(0, 0, 0)  # 黒色

        # 地球の追加
        self.earth = self.loader.load_model(self.MODEL_EARTH)
        self.earth.set_color(0, 0, 1)  # 青色
        self.earth.reparent_to(self.render)
        # 座標軸の追加
        self.axis = self.loader.load_model(self.MODEL_AXIS)
        self.axis.reparent_to(self.render)
        self.axis.hide()

        self.sphere_node = self.render.attach_new_node('sphere_node')
        self.celestial_sphere = CelestialSphere(self)

        Camera(self)
