import pygame

from ui import draw_timer, draw_score, draw_text

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TASK_TIME_LIMIT, RED, WHITE

def failure_screen(screen):
    """失敗時の画面表示（キー入力でホーム画面に戻る）"""
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text(screen, "Failure!!", 60, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, RED)
        draw_text(screen, "Press any button", 40, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50, RED)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                return  # ホーム画面に戻る