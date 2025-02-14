# -*- coding: utf-8 -*-


from .langs.ja import DIRECTIONS
from .text_drawer import TextDrawer3D
from .utils.geom import *


class CelestialSphere:
    """
    天球を描画するためのクラス
    """
    # 球のライン・カラーのデフォルト値
    DEFAULT_SPHERE_LINE_COLOR = (0.5, 0.5, 0.5, 1)
    # 球のサーフェス・カラーのデフォルト値
    DEFAULT_SPHERE_SURFACE_COLOR = (0, 1, 0, 0.3)

    def __init__(self, base, line_color: tuple[float, float, float, float] = DEFAULT_SPHERE_LINE_COLOR, surface_color: tuple[float, float, float, float] = DEFAULT_SPHERE_SURFACE_COLOR) -> None:
        """
        コンストラクタ
        :param base: ベース
        """
        self.base = base
        # 天球の設定
        self.radius = self.base.CELESTIAL_SPHERE_RADIUS
        self.line_color = line_color
        self.surface_color = surface_color

        # 天球の作成
        self.create()

    def create(self) -> None:
        """
        天球を作成するメソッド
        """
        # 天球における縦線の描画
        for i in range(12):
            angle = i * 360 / 24
            thickness = 4 if i % 3 == 0 else 1

            circle_path = draw_circumference_zx(self.base.sphere_node, self.radius, self.line_color, thickness)
            circle_path.set_h(angle)

        # 天球における横線の描画
        for i in range(1, 12):
            angle = (6 - i) * 180 / 12
            radius = self.radius * cos(radians(angle))
            z = self.radius * sin(radians(angle))

            circle_path = draw_circumference_zx(self.base.sphere_node, radius, self.line_color)
            circle_path.set_p(90)
            circle_path.set_pos(0, 0, z)

        # 水平面における同心円の描画
        for i in range(1, 11):
            radius = i * self.radius / 10

            circle_path = draw_circumference_zx(self.base.sphere_node, radius, self.line_color)
            circle_path.set_p(90)

        # 水平面における放射線の描画
        for i in range(12):
            angle = i * 180 / 12
            thickness = 4 if i % 3 == 0 else 1

            line_path = draw_line(self.base.sphere_node, (self.radius, 0, 0), (-self.radius, 0, 0), self.line_color, thickness)
            line_path.set_h(angle)

        # 水平面における三角形の描画
        for i in range(24):
            angle1 = i * 360 / 24
            angle2 = (i + 1) * 360 / 24
            point0 = (0, 0, 0)
            point1 = (self.radius * cos(radians(angle1)), self.radius * sin(radians(angle1)), 0)
            point2 = (self.radius * cos(radians(angle2)), self.radius * sin(radians(angle2)), 0)

            draw_filled_triangle(self.base.sphere_node, point0, point1, point2, self.surface_color)

        # 方角の描画
        for i, direction in enumerate(DIRECTIONS):
            angle = i * 45
            angle_rad = radians(angle)
            x, y, z = self.radius * cos(angle_rad + pi/2), self.radius * sin(angle_rad + pi/2), 0

            text_label = TextDrawer3D(direction, self.base.font, self.base.sphere_node, pos=(0, 3), scale=7, fg=(1, 0, 0, 1))
            text_label.label_node.setPos(x, y, z)
            text_label.look_at_origin(x, y, z)
