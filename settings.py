# settings.py

import os

# 画面設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

CLEAR_SCORE = 200

# タイルサイズ
TILE_SIZE = 50

""""""""""""""""""""""""""""""""
PLAYER_WIDTH_1 = 300
PLAYER_HEIGHT_1 = 400

PLAYER_SIZE = 40
""""""""""""""""""""""""""""""""

# プレイヤー設定
PLAYER_SPEED = 10

# タスクの時間制限
TASK_TIME_LIMIT = 60  # 60秒

# 色設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 223, 0)
RED = (255, 0, 0)      # 赤（ペナルティ）
GREEN = (0, 255, 0)    # 緑（加点）

chapter1_clear = -1
chapter2_clear = -1
chapter3_clear = -1
chapter4_clear = -1
chapter5_clear = -1

# フォントのパスを絶対パスにする
BASE_DIR = os.path.dirname(__file__)
FONT_PATH = os.path.join(BASE_DIR, "fonts", "NotoSansJP-Regular.otf")

# フォントが存在しない場合、デフォルトフォントを使用
if not os.path.exists(FONT_PATH):
    print(f"Warning: フォント '{FONT_PATH}' が見つかりません。代わりに pygame のデフォルトフォントを使用します。")
    FONT_PATH = None  # None を指定すると pygame のデフォルトフォントが使用される