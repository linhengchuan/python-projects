import pygame
import sys
import numpy as np

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 10, 10)
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300

class TicTacToe:
    def __init__(self):
        self._count = 0
        self._tic_map = np.zeros((3,3))
        self._circle_map = np.zeros((3,3))
        # self._text_font = pygame.font.SysFont("comicsansms", 35)
        
    def start(self):
        pygame.init()
        dis=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.update()
        pygame.display.set_caption("HC's Tic Tac Toe")
        game_over=False
        pygame.draw.rect(dis, WHITE, [0,0,WINDOW_WIDTH,WINDOW_HEIGHT])
        self.drawGrid(dis)
        pygame.display.update()
        text_font = pygame.font.SysFont("comicsansms", 35)
        while not game_over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    (x,y) = self.findTopLeftCorner(*pos)
                    if self._count==9:
                        dis.blit(text_font.render("DRAW", True, RED), [WINDOW_WIDTH / 6, WINDOW_HEIGHT / 2])
                        game_over = True
                    if self._count%2==0:
                        if self.edit_map(self._circle_map, self._tic_map, x, y):
                            self._count+=1
                            self.drawCircle(dis, x, y)
                            if self.check_win(self._circle_map):
                                dis.blit(text_font.render("Circle wins", True, RED), [WINDOW_WIDTH / 6, WINDOW_HEIGHT / 3])
                                game_over = True
                            pygame.display.update()
                    else:
                        if self.edit_map(self._tic_map, self._circle_map, x, y):
                            self._count+=1
                            self.drawTic(dis, x, y)
                            if self.check_win(self._tic_map):
                                dis.blit(text_font.render("Tic wins", True, RED), [WINDOW_WIDTH / 6, WINDOW_HEIGHT / 2])
                                game_over = True
                            pygame.display.update()
            while game_over:
                dis.blit(text_font.render("Press Q", True, RED), [WINDOW_WIDTH / 6, WINDOW_HEIGHT / 4])
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
        
    def edit_map(self, target_map, opp_map, x, y):
        x=int(x/100)
        y=int(y/100)
        if target_map[x][y]!=1 and opp_map[x][y]!=1:
            target_map[x][y]=1
            return True
        
    def check_win(self, np_map):
        if all(np_map[0]==np.array([1,1,1])) or all(np_map[1]==np.array([1,1,1])) or all(np_map[2]==np.array([1,1,1])) \
        or all(np_map[:,0]==np.array([1,1,1])) or all(np_map[:,1]==np.array([1,1,1])) or all(np_map[:,2]==np.array([1,1,1])) \
        or all(np.diag(np.fliplr(np_map))==np.array([1,1,1])) or all(np.diag(np_map)==np.array([1,1,1])):
            return True
    
    def drawGrid(self, dis):
        blockSize = 100 #Set the size of the grid block
        for x in range(0, WINDOW_WIDTH, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(dis, BLACK, rect, 1)

    def drawTic(self, dis, x, y):
        pygame.draw.line(dis, BLACK, (x+20,y+20),(x+80, y+80), width=10)
        pygame.draw.line(dis, BLACK, (x+80,y+20),(x+20, y+80), width=10)

    def drawCircle(self, dis, x, y):
        pygame.draw.circle(dis, BLACK, center=(x+50, y+50), radius=30, width=10)
        
    def findTopLeftCorner(self, x, y):
        return ((x//100)*100, (y//100)*100)
            
game = TicTacToe()
game.start()