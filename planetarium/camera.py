# -*- coding: utf-8 -*-


from panda3d.core import Point3

from .utils.vector import convert_to_cartesian


class Camera:
    """
    カメラを操作するためのクラス
    """
    # 内部カメラにおける視野角の最小値
    INTERNAL_CAMERA_FOV_MIN = 30
    # 内部カメラにおける視野角の最大値
    INTERNAL_CAMERA_FOV_MAX = 150
    # 外部カメラにおける原点からの距離（半径）の最小値
    EXTERNAL_CAMERA_RADIUS_MIN = 5
    # 外部カメラにおける原点からの距離（半径）の最大値
    EXTERNAL_CAMERA_RADIUS_MAX = 800


    def __init__(self, base) -> None:
        """
        コンストラクタ
        :param base: ベース
        """
        self.base = base

        # カメラの位置が原点にあるかどうかのフラグ
        self.is_at_origin = True

        # マウス操作の無効化
        self.base.disable_mouse()
        # ニア・クリッピングの設定
        self.base.camLens.set_near(0.1)

        # 内部カメラの設定
        self.internal_camera_fov = 100
        self.internal_camera_theta = 25
        self.internal_camera_phi = 0

        # 外部カメラの設定
        self.external_camera_fov = 35
        self.external_camera_radius = self.base.CELESTIAL_SPHERE_RADIUS * 4
        self.external_camera_theta = 60
        self.external_camera_phi = -60

        self.update_position()

        # キー操作割り当ての設定
        self.base.accept('arrow_up', self.move, [0, -1, 0])
        self.base.accept('arrow_up-repeat', self.move, [0, -1, 0])
        self.base.accept('w', self.move, [0, -1, 0])
        self.base.accept('w-repeat', self.move, [0, -1, 0])
        self.base.accept('arrow_left', self.move, [0, 0, -1])
        self.base.accept('arrow_left-repeat', self.move, [0, 0, -1])
        self.base.accept('a', self.move, [0, 0, -1])
        self.base.accept('a-repeat', self.move, [0, 0, -1])
        self.base.accept('arrow_down', self.move, [0, 1, 0])
        self.base.accept('arrow_down-repeat', self.move, [0, 1, 0])
        self.base.accept('s', self.move, [0, 1, 0])
        self.base.accept('s-repeat', self.move, [0, 1, 0])
        self.base.accept('arrow_right', self.move, [0, 0, 1])
        self.base.accept('arrow_right-repeat', self.move, [0, 0, 1])
        self.base.accept('d', self.move, [0, 0, 1])
        self.base.accept('d-repeat', self.move, [0, 0, 1])
        self.base.accept('wheel_up', self.move, [-1, 0, 0])
        self.base.accept('=', self.move, [-1, 0, 0])
        self.base.accept('=-repeat', self.move, [-1, 0, 0])
        self.base.accept('wheel_down', self.move, [1, 0, 0])
        self.base.accept('-', self.move, [1, 0, 0])
        self.base.accept('--repeat', self.move, [1, 0, 0])
        self.base.accept('r', self.reset_position)
        self.base.accept('c', self.toggle)

    def update_position(self) -> None:
        """
        カメラの位置を更新する関数
        """
        # カメラの位置の更新
        if self.is_at_origin:  # カメラが原点にある場合
            theta = self.internal_camera_theta
            phi = self.internal_camera_phi
            # 内部カメラの位置の更新
            self.base.camera.set_pos(0, 0, 0.5)
            self.base.camera.set_hpr(phi, theta, 0)
            self.base.camLens.set_fov(self.internal_camera_fov)
            self.base.camera.reparent_to(self.base.sphere_node)
        else:
            r = self.external_camera_radius
            theta = self.external_camera_theta
            phi = self.external_camera_phi
            pos = Point3(*convert_to_cartesian(r, theta, phi))
            # 外部カメラの位置の更新
            self.base.camera.set_pos(pos)
            self.base.camera.set_hpr(0, 0, 0)
            self.base.camera.look_at(0, 0, 0)
            self.base.camLens.set_fov(self.external_camera_fov)
            self.base.camera.reparent_to(self.base.render)

    def move(self, r_diff, theta_diff, phi_diff) -> None:
        """
        カメラを移動する関数
        :param r_diff: 動径（r）の差分
        :param theta_diff: 偏角（θ）の差分
        :param phi_diff: 偏角（φ）の差分
        """
        # カメラの位置及び視野角の変更
        if self.is_at_origin:  # カメラが原点にある場合
            self.internal_camera_fov += r_diff
            self.internal_camera_theta += -theta_diff
            self.internal_camera_phi += -phi_diff
            # 設定値の補正
            self.internal_camera_fov = max(self.INTERNAL_CAMERA_FOV_MIN, min(self.internal_camera_fov, self.INTERNAL_CAMERA_FOV_MAX))
            self.internal_camera_theta = 0 if abs(self.internal_camera_theta) == 360 else self.internal_camera_theta
            self.internal_camera_phi = 0 if abs(self.internal_camera_phi) == 360 else self.internal_camera_phi
            # DEBUG:
            # print(f"- internal_camera_fov:   {self.internal_camera_fov: 5}")
            # print(f"- internal_camera_theta: {self.internal_camera_theta: 5}")
            # print(f"- internal_camera_phi:   {self.internal_camera_phi: 5}")
        else:
            self.external_camera_radius += 5 * r_diff
            self.external_camera_theta += theta_diff
            self.external_camera_phi += phi_diff
            # 設定値の補正
            self.external_camera_radius = max(self.EXTERNAL_CAMERA_RADIUS_MIN, min(self.external_camera_radius, self.EXTERNAL_CAMERA_RADIUS_MAX))
            self.external_camera_theta = 0 if abs(self.external_camera_theta) == 360 else self.external_camera_theta
            self.external_camera_phi = 0 if abs(self.external_camera_phi) == 360 else self.external_camera_phi
            # DEBUG:
            # print(f"- external_camera_radius: {self.external_camera_radius: 5}")
            # print(f"- external_camera_theta:  {self.external_camera_theta: 5}")
            # print(f"- external_camera_phi:    {self.external_camera_phi: 5}")

        self.update_position()

    def reset_position(self) -> None:
        """
        カメラの位置を初期化する関数
        """
        # 内部カメラの再設定
        self.internal_camera_fov = 100
        self.internal_camera_theta = 25
        self.internal_camera_phi = 0
        # 外部カメラの再設定
        self.external_camera_fov = 35
        self.external_camera_radius = self.base.CELESTIAL_SPHERE_RADIUS * 4
        self.external_camera_theta = 60
        self.external_camera_phi = -60

        self.update_position()

    def toggle(self) -> None:
        """
        内部カメラと外部カメラを切り替える関数
        """
        self.is_at_origin = not self.is_at_origin

        self.update_position()
