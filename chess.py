# import pygame  
# import random  
  
# # 初始化pygame  
# pygame.init()  
  
# # 设置屏幕大小和标题  
# screen_width = 800  
# screen_height = 600  
# screen = pygame.display.set_mode((screen_width, screen_height))  
# pygame.display.set_caption("三子棋游戏")  
  
# # 设置颜色  
# WHITE = (255, 255, 255)  
# BLACK = (0, 0, 0)  
# RED = (255, 0, 0)  
# GREEN = (0, 255, 0)  
  
# # 设置棋盘大小和棋子大小  
# board_width = 16  
# board_height = 16  
# tile_size = 30  
# margin = 10  
  
# # 创建棋盘和棋子列表  
# board = [[0 for _ in range(board_width)] for _ in range(board_height)]  
# tiles = []  
# for row in range(board_height):  
#     for col in range(board_width):  
#         x = margin + col * tile_size + tile_size // 2  
#         y = margin + row * tile_size + tile_size // 2  
#         tiles.append((x, y))  
  
# # 游戏主循环  
# running = True  
# while running:  
#     for event in pygame.event.get():  
#         if event.type == pygame.QUIT:  
#             running = False  
#         elif event.type == pygame.MOUSEBUTTONDOWN:  # 如果点击了鼠标左键，则放置棋子并检查是否获胜  
#             mouse_x, mouse_y = pygame.mouse.get_pos()  
#             row = (mouse_y - margin) // tile_size + 1  
#             col = (mouse_x - margin) // tile_size + 1  
#             if board[row][col] == 0:  # 如果该位置没有棋子，则放置棋子并检查是否获胜  
#                 board[row][col] = 1  # 放置白棋子（玩家1）  
#                 if check_win(board, row, col, 1):  # 检查是否获胜（玩家1）胜出  
#                     pygame.font.init()  # 初始化字体模块（如果之前没有初始化）  
#                     font = pygame.font.SysFont("Arial", 36)  # 创建字体对象（36号字体）  
#                     text = font.render("玩家1胜出！", True, GREEN)  # 创建获胜提示文本对象（绿色字体）  
#                     screen.blit(text, (20, 20))  # 在屏幕上显示获胜提示文本（左上角位置）  
#                     pygame.display.flip()  # 更新屏幕显示内容  
#                     running = False  # 结束游戏循环（获胜）  
#                 else:  # 如果玩家1没有获胜，则轮到玩家2下棋（交替下棋）  
#                     pygame.time.wait(1000)  # 等待1秒钟（等待时间可调整）  
#                     board[row][col] = -1  # 放置黑棋子（玩家2）  
#                     if check_win(board, row, col, -1):  # 检查是否获胜（玩家2）胜出  
#                         pygame.font.init()  # 初始化字体模块（如果之前没有初始化）  
#                         font = pygame.font.SysFont("Arial", 36)  # 创建字体对象（36号字体）  
#                         text = font.render("玩家2胜出！", True, RED)  # 创建获胜提示文本对象（红色字体）  
#                         screen.blit(text, (20, 20))  # 在屏幕上显示获胜提示文本（左上角位置）  
#                         pygame.display.flip()  # 更新屏幕显示内容  
#                         running = False  # 结束游戏循环（获胜）  
#             else:  # 如果该位置已经有棋子，则不放置棋子（无法重复下棋）  
#                 pygame.font.init()  # 初始化字体模块（如果之前没有初始化）  
#                 font = pygame.font.SysFont("Arial", 24)  # 创建字体对象（24号字体）  
#                 text


def minimax(self, player, depth, alpha, beta):
   if player == self.current_player:
      best_score = -math.inf

      for row in range(3):
         for col in range(3):
            if self.board.board[row][col] == 0:
               self.board.board[row][col] = player.piece
               player.moves.append((row, col))
               score = self.minimax(self.player2, depth+1, alpha, beta)
               self.board.board[row][col] = 0
               player.moves.pop()
               best_score = max(best_score, score)
               alpha = max(alpha, score)
               if beta <= alpha:
                  break

      return best_score

   else:
      best_score = math.inf

      for row in range(3):
         for col in range(3):
            if self.board.board[row][col] == 0:
               self.board.board[row][col] = player.piece
               player.moves.append((row, col))
               score = self.minimax(self.player1, depth+1, alpha, beta)
               self.board.board[row][col] = 0
               player.moves.pop()
               best_score = min(best_score, score)
               beta = min(beta, score)
               if beta <= alpha:
                  break

      return best_score