# -*- coding: utf-8 -*-


from math import acos, atan2, sin, cos, degrees, radians, sqrt
import numpy as np


def convert_to_polar(x: float, y: float, z: float) -> tuple[float,float,float]:
    """
    直交座標を極座標に変換する関数
    :param x: 直交座標系におけるＸ座標（x）
    :param y: 直交座標系におけるＹ座標（y）
    :param z: 直交座標系におけるＺ座標（z）
    :return: 極座標（(r, θ, φ)）
    """
    # 極座標系における動径（r）及び偏角（θ，φ）の算出
    r = sqrt(x**2 + y**2 + z**2)
    theta = degrees(acos(z / r))
    phi = degrees(atan2(y, x))

    return r, theta, phi


def convert_to_cartesian(r: float, theta: float, phi: float) -> tuple[float,float,float]:
    """
    極座標を直交座標に変換する関数
    :param r: 極座標系における動径（r）
    :param theta: 極座標系における偏角（θ）
    :param phi: 極座標系における偏角（φ）
    :return: 直交座標（(x, y, z)）
    """
    theta_rad, phi_rad = radians(theta), radians(phi)

    # 直交座標系におけるＸ座標，Ｙ座標，及びＺ座標の算出
    x = r * sin(theta_rad) * cos(phi_rad)
    y = r * sin(theta_rad) * sin(phi_rad)
    z = r * cos(theta_rad)

    return x, y, z


def get_point_from_rotated_coordinates(x: float, y: float, z: float, heading: float, pitch: float, roll: float):
    """
    回転された座標系における固定点の座標を取得する関数
    :param x: 固定点のＸ座標（x）
    :param y: 固定点のＹ座標（y）
    :param z: 固定点のＺ座標（z）
    :param heading: 回転された座標系における固定点のヨー角
    :param pitch: 回転された座標系における固定点のピッチ角
    :param roll: 回転された座標系における固定点のロール角
    :return: 回転された座標系における固定点の座標
    """
    heading_rad, pitch_rad, roll_rad = radians(heading), radians(pitch), radians(roll)

    # ヨー軸周りの回転行列の算出
    heading_rotation_matrix = np.array([
        [cos(-heading_rad), -sin(-heading_rad), 0],
        [sin(-heading_rad), cos(-heading_rad), 0],
        [0, 0, 1]
    ])
    # ピッチ軸周りの回転行列の算出
    pitch_rotation_matrix = np.array([
        [1, 0, 0],
        [0, cos(-pitch_rad), -sin(-pitch_rad)],
        [0, sin(-pitch_rad), cos(-pitch_rad)]
    ])
    # ロール軸周りの回転行列の算出
    roll_rotation_matrix = np.array([
        [cos(-roll_rad), 0, sin(-roll_rad)],
        [0, 1, 0],
        [-sin(-roll_rad), 0, cos(-roll_rad)]
    ])

    # 逆回転行列の作成
    rotation_matrix = np.dot(roll_rotation_matrix, np.dot(pitch_rotation_matrix, heading_rotation_matrix))

    return rotation_matrix.dot(np.array([x, y, z]))


def convert_star_position(h_ra, m_ra, s_ra, d_dec, m_dec, s_dec, radius) -> tuple[float,float,float]:
    """
    恒星，星座線，又は星座名ラベルの位置する赤道座標を直行座標に変換する関数
    :param h_ra: 赤経における時（hours）
    :param m_ra: 赤経における分（minutes）
    :param s_ra: 赤経における秒（seconds）
    :param d_dec: 赤緯における度（degrees）
    :param m_dec: 赤緯における分（minutes）
    :param s_dec: 赤緯における秒（seconds）
    :param radius: 半径
    :return: 直交座標（(x, y, z)）
    """
    # 赤経及び赤緯の単位変換（°）
    ra = (h_ra + m_ra/60 + s_ra/3600) * 15
    dec = d_dec + m_dec/60 + s_dec/3600

    # 赤道座標の極座標変換
    r, theta, phi = radius, 90 - dec, ra
    # 極座標の直行座標変換
    x, y, z = convert_to_cartesian(r, theta, phi)

    return x, y, z
