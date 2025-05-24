# Chapter3/story.py
import pygame

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

from ui import draw_text

# 画像の読み込み
STORY_IMAGE = pygame.image.load("assets/story.png")

def display_story(screen, story_text):
    """
    ストーリーをページごとに表示し、キー入力で進む
    :param screen: Pygameのスクリーン
    :param story_text: ストーリーの文章リスト
    """
    background = pygame.transform.scale(STORY_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # 🔹 BGM 再生（ループ）
    pygame.mixer.music.load("sound/background/story.mp3")
    pygame.mixer.music.set_volume(0.5)  # 音量調整 (0.0 ～ 1.0)
    pygame.mixer.music.play(-1)  # 無限ループ再生

    # 効果音
    page_sound = pygame.mixer.Sound("sound/effect/page.mp3")

    page = 0
    running = True

    color = BLACK

    while running:
        screen.blit(background, (0, 0))

        draw_text(screen, "Chapter 3", 47, SCREEN_WIDTH // 2, 100, color)  # タイトル

        # ストーリーの文章を表示
        y_offset = 200  # 開始Y位置
        for line in story_text[page]:  # 現在のページの文章を表示
            draw_text(screen, line, 25, SCREEN_WIDTH // 2, y_offset, color)
            y_offset += 50  # 次の行へ

        draw_text(screen, "Press any key to continue...", 20, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20, WHITE)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                page_sound.play()
                
                page += 1
                if page >= len(story_text):  # 最後のページなら終了
                    pygame.mixer.music.stop()
                    running = False

def st_story(screen):
    """ゲーム開始前のストーリー"""
    story_text = [
        ["Processed and shipped,",
         "you were displayed",
          "in local supermarkets."],
        ["Around you were",
         "your brothers and sisters,",  
         "your father and mother,",
         "and friends you had lived",
         "and played with",
         "in the neighborhood."],
        ["They were all cut up",
         "and turned into delicious",
         "looking pork."],
        ["Who among you on display",
         "will be the first to buy it?"],
        ["One by one,",
         "they are bought",
         "by the housewives."],
        ["Finally,",
         "the half-price sticker is",
         "put on you."],
        ["It is almost closing time.",
         "Freshness is important to you."],
        ["If you don't sell today,",
         "it may be discarded."],
        ["That's when! What a surprise,",  
         "one housewise with a punch perm",
         "took you in her hand",  
         "and put you in her basket!"],
        ["Perhaps this housewife does not have",  
         "much family money to spare",  
         "and is a big fan of",
         "half-price sale items."],
        ["You finally make it into the house",  
         "and are put",
         "under the knife in a kitchen",  
         "that is deserted",
         "and smells somewhat of iron."]
    ]
    display_story(screen, story_text)  # ストーリー終了後にゲーム開始

def en_story(screen):
    """ゲームクリア後のストーリー"""
    story_text = [
        ["Congratulations",
         "on reaching your goal!",
         "You have managed to reach a size",
         "that is both easy to eat",
         "and easy to cook."]
    ]
    display_story(screen, story_text)  # ストーリー終了後は何もしない（タイトル画面に戻る）
