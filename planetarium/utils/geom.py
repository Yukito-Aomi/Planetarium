# -*- coding: utf-8 -*-


from math import *

from panda3d.core import *


# 線の太さのデフォルト値
DEFAULT_THICKNESS = 1.0
# セグメント数のデフォルト値
DEFAULT_SEGMENTS = 64


def create_geom(parent, vertices: list, color: tuple[float, float, float, float], thickness: float = DEFAULT_THICKNESS):
    """
    図形オブジェクトを生成するヘルパー関数
    :param parent: スーパーノード
    :param vertices: 頂点の座標が格納されたリスト
    :param color: 図形の色
    :param thickness: 図形の線の太さ
    :return: 図形オブジェクト
    """
    # GeomVertexData オブジェクトの作成
    geom_vertex_data = GeomVertexData('shape', GeomVertexFormat.get_v3(), Geom.UHStatic)
    geom_vertex_data.set_num_rows(len(vertices))

    # 頂点のデータの作成
    vertex = GeomVertexWriter(geom_vertex_data, 'vertex')
    for v in vertices:
        vertex.add_data3f(*v)

    # プリミティヴの作成
    if len(vertices) == 3:  # 頂点数が３つである場合（三角形を描画する場合）
        primitive = GeomTriangles(Geom.UHStatic)
        primitive.add_vertices(0, 1, 2)
    else:
        primitive = GeomLines(Geom.UHStatic)
        for i in range(len(vertices) - 1):
            primitive.add_vertices(i, i + 1)

    primitive.close_primitive()

    # Geom オブジェクトの作成
    geom = Geom(geom_vertex_data)
    geom.add_primitive(primitive)

    # GeomNode オブジェクトの作成
    node = GeomNode('shape_node')
    node.addGeom(geom)

    # ノードパスの作成及びスーパーノードへの追加
    node_path = parent.attach_new_node(node)
    node_path.set_color(*color)
    node_path.set_render_mode_thickness(thickness)

    # 透過属性の設定
    if len(vertices) == 3:  # 頂点数が３つである場合（三角形を描画する場合）
        node_path.set_transparency(TransparencyAttrib.MAlpha)

    return node_path


def draw_line(parent, point1, point2, color: tuple[float, float, float, float], thickness: float = DEFAULT_THICKNESS):
    """
    直線を描画する関数
    :param parent: スーパーノード
    :param point1: 直線の端点１
    :param point2: 直線の端点２
    :param color: 図形の色
    :param thickness: 直線の太さ
    :return: 直線の図形オブジェクト
    """
    return create_geom(parent, [point1, point2], color, thickness)


def draw_circumference_zx(parent, radius, color: tuple[float, float, float, float], thickness: float = DEFAULT_THICKNESS, segments: int = DEFAULT_SEGMENTS):
    """
    ＺＸ平面上に円を描画する関数
    :param parent: スーパーノード
    :param radius: 円の半径
    :param color: 図形の色
    :param thickness: 円周の太さ
    :param segments: セグメント数
    :return: ＺＸ平面上の円の図形オブジェクト
    """
    vertices = [
        (radius * sin(2 * pi * i / segments), 0, radius * cos(2 * pi * i / segments)) for i in range(segments + 1)
    ]

    return create_geom(parent, vertices, color, thickness)


def draw_filled_triangle(parent, point1, point2, point3, color: tuple[float, float, float, float]):
    """
    面が塗りつぶされた三角形を描画する関数
    :param parent: スーパーノード
    :param point1: 三角形の頂点１
    :param point2: 三角形の頂点２
    :param point3: 三角形の頂点３
    :param color: 図形の色
    :return: 面が塗りつぶされた三角形の図形オブジェクト
    """
    return create_geom(parent, [point1, point2, point3], color)
