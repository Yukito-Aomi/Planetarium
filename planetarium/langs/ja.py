# -*- coding: utf-8 -*-


# 方位の名称に関する日本語訳の定義
DIRECTIONS = [
    '北',
    '北西',
    '西',
    '南西',
    '南',
    '南東',
    '東',
    '北東'
]

# 太陽系における恒星に関する日本語訳の定義
SUN_NAME = '太陽'

# 星座の名称に関する日本語訳の定義
CONSTELLATION_NAMES = {
    # アンドロメダ座，斗掻き星（Andromeda）
    'And': 'アンドロメダ',
    # ポンプ座（Antlia）
    'Ant': 'ポンプ',
    # 風鳥座（Apus）
    'Aps': 'ふうちょう',
    # 鷲座（Aquila）
    'Aql': 'わし',
    # 水瓶座（Aquarius）
    'Aqr': 'みずがめ',
    # 祭壇座（Ara）
    'Ara': 'さいだん',
    # 牡羊座（Aries）
    'Ari': 'おひつじ',
    # 馭者座，五角星（Auriga）
    'Aur': 'ぎょしゃ',
    # 牛飼座（Bootes）
    'Boo': 'うしかい',
    # 彫刻具座（Caelum）
    'Cae': 'ちょうこくぐ',
    # 麒麟座（Camelopardalis）
    'Cam': 'きりん',
    # 山羊座（Capricornus）
    'Cap': 'やぎ',
    # 竜骨座（Carina）
    'Car': 'りゅうこつ',
    # カシオペヤ座，錨星，山形星（Cassiopeia）
    'Cas': 'カシオペヤ',
    # ケンタウルス座（Centaurus）
    'Cen': 'ケンタウルス',
    # ケフェウス座（Cepheus）
    'Cep': 'ケフェウス',
    # 鯨座（Cetus）
    'Cet': 'くじら',
    # カメレオン座（Chamaeleon）
    'Cha': 'カメレオン',
    # コンパス座（Circinus）
    'Cir': 'コンパス',
    # 大犬座（Canis Major）
    'CMa': 'おおいぬ',
    # 小犬座（Canis Minor）
    'CMi': 'こいぬ',
    # 蟹座（Cancer）
    'Cnc': 'かに',
    # 鳩座（Columba）
    'Col': 'はと',
    # 髪の毛座（Coma Berenices）
    'Com': 'かみのけ',
    # 南の冠座（Corona Australis）
    'CrA': 'みなみのかんむり',
    # 冠座，車星（Corona Borealis）
    'CrB': 'かんむり',
    # コップ座（Crater）
    'Crt': 'コップ',
    # 南十字座（Crux）
    'Cru': 'みなみじゅうじ',
    # 烏座，帆掛け星，四つ星（Corvus）
    'Crv': 'からす',
    # 猟犬座（Canes Venatici）
    'CVn': 'りょうけん',
    # 白鳥座，十文字星（Cygnus）
    'Cyg': 'はくちょう',
    # 海豚座，菱星（Delphinus）
    'Del': 'いるか',
    # 旗魚座（Dorado）
    'Dor': 'かじき',
    # 竜座（Draco）
    'Dra': 'りゅう',
    # 小馬座（Equuleus）
    'Equ': 'こうま',
    # エリダヌス座（Eridanus）
    'Eri': 'エリダヌス',
    # 炉座（Fornax）
    'For': 'ろ',
    # 双子座（Gemini）
    'Gem': 'ふたご',
    # 鶴座（Grus）
    'Gru': 'つる',
    # ヘルクレス座（Hercules）
    'Her': 'ヘルクレス',
    # 時計座（Horologium）
    'Hor': 'とけい',
    # 海蛇座（Hydra）
    'Hya': 'うみへび',
    # 水蛇座（Hydrus）
    'Hyi': 'みずへび',
    # インディアン座（Indus）
    'Ind': 'インディアン',
    # 蜥蜴座（Lacerta）
    'Lac': 'とかげ',
    # 獅子座，樋掛け星（Leo）
    'Leo': 'しし',
    # 兎座（Lepus）
    'Lep': 'うさぎ',
    # 天秤座（Libra）
    'Lib': 'てんびん',
    # 小獅子座（Leo Minor）
    'LMi': 'こじし',
    # 狼座（Lupus）
    'Lup': 'おおかみ',
    # 山猫座（Lynx）
    'Lyn': 'やまねこ',
    # 琴座（Lyra）
    'Lyr': 'こと',
    # テーブル山座（Mensa）
    'Men': 'テーブルさん',
    # 顕微鏡座（Microscopium）
    'Mic': 'けんびきょう',
    # 一角獣座（Monoceros）
    'Mon': 'いっかくじゅう',
    # 蠅座（Musca）
    'Mus': 'はえ',
    # 定規座（Norma）
    'Nor': 'じょうぎ',
    # 八分儀座（Octans）
    'Oct': 'はちぶんぎ',
    # 蛇遣い座（Ophiuchus）
    'Oph': 'へびつかい',
    # オリオン座，鼓星（Orion）
    'Ori': 'オリオン',
    # 孔雀座（Pavo）
    'Pav': 'くじゃく',
    # ペガスス座，桝形星（Pegasus）
    'Peg': 'ペガスス',
    # ペルセウス座（Perseus）
    'Per': 'ペルセウス',
    # 鳳凰座（Phoenix）
    'Phe': 'ほうおう',
    # 画架座（Pictor）
    'Pic': 'がか',
    # 南の魚座（Piscis Austrinus）
    'PsA': 'みなみのうお',
    # 魚座（Pisces）
    'Psc': 'うお',
    # 船尾座（Puppis）
    'Pup': 'とも',
    # 羅針盤座（Pyxis）
    'Pyx': 'らしんばん',
    # レチクル座（Reticulum）
    'Ret': 'レチクル',
    # 彫刻室座（Sculptor）
    'Scl': 'ちょうこくしつ',
    # 蠍座，魚釣り星，釣り星（Scorpius）
    'Sco': 'さそり',
    # 楯座（Scutum）
    'Sct': 'たて',
    # 蛇座（Serpens）
    'Ser': 'へび',
    # 六分儀座（Sextans）
    'Sex': 'ろくぶんぎ',
    # 矢座（Sagitta）
    'Sge': 'や',
    # 射手座，箕星，南斗六星（Sagittarius）
    'Sgr': 'いて',
    # 牡牛座（Taurus）
    'Tau': 'おうし',
    # 望遠鏡座（Telescopium）
    'Tel': 'ぼうえんきょう',
    # 南の三角座（Triangulum Australe）
    'TrA': 'みなみのさんかく',
    # 三角座（Triangulum）
    'Tri': 'さんかく',
    # 巨嘴鳥座（Tucana）
    'Tuc': 'きょしちょう',
    # 大熊座（Ursa Major）
    'UMa': 'おおぐま',
    # 小熊座（Ursa Minor）
    'UMi': 'こぐま',
    # 帆座（Vela）
    'Vel': 'ほ',
    # 乙女座（Virgo）
    'Vir': 'おとめ',
    # 飛び魚座（Volans）
    'Vol': 'とびうお',
    # 小狐座（Vulpecula）
    'Vul': 'こぎつね'
}
