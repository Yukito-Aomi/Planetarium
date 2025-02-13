# -*- coding: utf-8 -*-


from math import degrees, atan2, sqrt

from direct.gui.DirectGui import OnscreenText
from panda3d.core import TextNode, PandaNode


class TextDrawer2D(OnscreenText):
    """
    ２Ｄテキストを描画するためのクラス
    """
    # デフォルトのテキスト・ポジション
    DEFAULT_TEXT_POSITION = (0.05, -0.1)
    # デフォルトのテキスト・スケール
    DEFAULT_TEXT_SCALE = 0.1
    # デフォルトのテキスト・カラー（前景）
    DEFAULT_TEXT_COLOR_FOREGROUND = (1, 1, 1, 1)

    def __init__(self, text, font, parent, pos=DEFAULT_TEXT_POSITION, scale=DEFAULT_TEXT_SCALE, fg=DEFAULT_TEXT_COLOR_FOREGROUND) -> None:
        """
        コンストラクタ
        :param text: テキストの内容
        :param font: テキストのフォント
        :param parent: 親ノード
        :param pos: テキストの位置
        :param scale: テキストのスケール
        :param fg: テキストの前景色
        """
        # スーパークラスのコンストラクタ呼出し
        super().__init__(text=text, pos=pos, scale=scale, fg=fg, align=TextNode.ALeft, font=font, parent=parent, mayChange=True)


class TextDrawer3D(OnscreenText):
    """
    ３Ｄテキストを描画するクラス
    """
    # デフォルトのテキスト・ポジション
    DEFAULT_TEXT_POSITION = (0, 0)
    # デフォルトのテキスト・スケール
    DEFAULT_TEXT_SCALE = 5
    # デフォルトのテキスト・カラー（前景）
    DEFAULT_TEXT_COLOR_FOREGROUND = (1, 1, 1, 1)

    def __init__(self, text, font, parent, pos=DEFAULT_TEXT_POSITION, scale=DEFAULT_TEXT_SCALE, fg=DEFAULT_TEXT_COLOR_FOREGROUND) -> None:
        """
        コンストラクタ
        :param text: テキストの内容
        :param font: テキストのフォント
        :param parent: スーパーノード
        :param pos: テキストの位置
        :param scale: テキストのスケール
        :param fg: テキストの前景色
        """
        self.label_node = parent.attach_new_node(PandaNode('label_node'))

        # スーパークラスのコンストラクタ呼出し
        super().__init__(text=text, pos=pos, scale=scale, fg=fg, font=font, parent=self.label_node)

    def look_at_origin(self, x, y, z) -> None:
        """
        ３Ｄテキストのスーパーノード（label_node）を原点方向に回転するメソッド
        :param x: Ｘ座標
        :param y: Ｙ座標
        :param z: Ｚ座標
        """
        # ヨー角（Ｚ軸を中心とする回転角度）
        h = degrees(atan2(y, x)) - 90
        # ピッチ角（Ｘ軸を中心とする回転角度）
        p = degrees(atan2(z, sqrt(x**2 + y**2)))
        # ロール角（Ｙ軸を中心とする回転角度）
        r = 0

        self.label_node.set_hpr(h, p, r)
