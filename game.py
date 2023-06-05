import pygame
from sys import exit
from random import randint,choice
from time import time

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global event
        self.turn = 0
        self.turn_display = arial_font.render(f'Turn: {self.turn}',False,'Black')
        self.turn_display_rect = self.turn_display.get_rect(center = (200,400))
        self.piece_num = 2
        self.piece_num_display = arial_font.render(f'Pieces: {self.piece_num}',False,'Black')
        self.piece_num_rect = self.piece_num_display.get_rect(center = (200,500))
        self.test = True

    def display_turn(self):
        self.turn_display = arial_font.render(f'Turn: {self.turn}',False,'Black')
        screen.blit(self.turn_display,self.turn_display_rect)
        return self.turn

    def display_piece_num(self):
        self.piece_num_display = arial_font.render(f'Pieces: {self.piece_num}',False,'Black')
        screen.blit(self.piece_num_display,self.piece_num_rect)
        return self.piece_num

    def player_input(self,obj_group):
        if self.test:
            if event.type == pygame.MOUSEBUTTONDOWN and obj_group:
                self.test = False
                self.turn += 1
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                self.test = True

    def pieces(self):
        return 

    def surrender(self):
         pass

    def update(self):
        self.player_input()
        self.display_turn()
        self.display_piece_num()

class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pass

class Piece(pygame.sprite.Sprite):
    def __init__(self, type, rect):
        super().__init__()

        if type == 'player':
            self.flipped = False
            self.img = pygame.image.load('graphics/piece_1.png').convert_alpha()
            self.rect = self.img.get_rect(center = rect)

        else:
            self.flipped = True
            self.img = pygame.image.load('graphics/piece_2.png').convert_alpha()
            self.rect = self.img.get_rect(center = rect)

        self.x_coord = ((self.rect.x - 450)//100)+1
        self.y_coord = ((self.rect.y - 100)//-100)+8
        self.position = (self.x_coord,self.y_coord)

        '''
        x -> 450,1150
        y -> 100, 800

        (1,1)
        400,50 would be the bottom left
        X: Examples (450, 100), (1150,800)
        -450 (0)  (700)
        /100 (0)  (7)
        +1   (1)  (8)

        Y: Examples (450, 100), (1150,800)
        -100  (0)  (700)
        /-100 (0)  (-7)
        +8    (8)  (1)
        '''
    def display_piece(self):
        screen.blit(self.img,self.rect)

    def update(self):
        self.display_piece()



class Board(pygame.sprite.Sprite):
    def __init__(self, player, rect):
        super().__init__()
        global event
        '''
        CHANGE OF MIND
        Board object in the group will be REPLACED everytime theres an INPUT
        '''

        # tile stuff
        if type == 'board':
            self.tile_img = pygame.image.load('graphics/tile.png').convert()

            self.row_1 = [0 + self.tile_img.get_rect(center = (450+100*x, 800)) for x in range(8)]
            self.row_2 = [0 + self.tile_img.get_rect(center = (450+100*x, 700)) for x in range(8)]
            self.row_3 = [0 + self.tile_img.get_rect(center = (450+100*x, 600)) for x in range(8)]
            self.row_4 = [0 + self.tile_img.get_rect(center = (450+100*x, 500)) for x in range(8)]
            self.row_5 = [0 + self.tile_img.get_rect(center = (450+100*x, 400)) for x in range(8)]
            self.row_6 = [0 + self.tile_img.get_rect(center = (450+100*x, 300)) for x in range(8)]
            self.row_7 = [0 + self.tile_img.get_rect(center = (450+100*x, 200)) for x in range(8)]
            self.row_8 = [0 + self.tile_img.get_rect(center = (450+100*x, 100)) for x in range(8)]

            self.board = [0, self.row_1, self.row_2, self.row_3, self.row_4, self.row_5, self.row_6, self.row_7, self.row_8]

        # piece stuff
        else:
            # if (750, 400) coord should be row 5 (3, 5)
            self.x_coord = ((rect.x - 450)//100)+1 
            self.y_coord = ((rect.y - 100)//-100)+8
            if player == True:
                self.b = pygame.image.load('graphics/tile_b.png').convert_alpha()
                self.b_rect = rect
                # convert rect to list index
                # change valie to tile with piece
                # (3, 5) -> (750, 400)
                self.board[self.x_coord][self.y_coord] = self.b.get_rect(center = (450+100*self.x_coord,))
            else:
                self.piece_w = pygame.image.load('graphics/tile_w.png').convert_alpha()
                self.w_rect = rect

        # self.pieces = [self.piece_b.get_rect(center = (750,400)), self.piece_b.get_rect(center = (850, 500))]

        self.test = True

    def player_turn(self):
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in self.board:
                    for y in x:
                        if y.collidepoint(event.pos) and y not in self.pieces:
                            self.b_rect = y
                            self.pieces.append((self.b_rect.x + 10, self.b_rect.y + 10))
                        

    def display_board(self):
        for x in self.board[1::]:
            for y in x[1::]:
                screen.blit(self.tile_img,y)
    


    def update(self):
        if type == 'board':
            self.display_board()
        self.player_turn()
        if type == 'piece':
            self.display_piece()

        


def circle_animation(circle_list):
    for circle_rect in circle_list:
        circle_rect.x += 10

        if circle_rect.x > 2000:
            circle_list.remove(circle_rect)
            
        screen.blit(circle_surf,circle_rect)

def circle_animation_2(circle_list):
    for circle_rect in circle_list:
        circle_rect.x -= 10

        if circle_rect.x < -600:
            circle_list.remove(circle_rect)

        screen.blit(circle_surf_2,circle_rect)

def rules_text_display(rule_list):
    y = 200
    for rule_text in rule_list:
        screen.blit(rule_text,rule_text.get_rect(midleft = (50, y)))
        y += 100

# def pieces_display(piece_dict):
#     global piece_b,piece_w

#     i = -1
#     for piece_rect in piece_dict:
#         i += 1
#         if i % 2 == 0:
#             screen.blit(piece_b,piece_dict[i])
#         else:
#             screen.blit(piece_w,piece_dict[i])

    

pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption('Othelol')
clock = pygame.time.Clock()
game_active = False
menu = True
rules_menu = False
music_playing = False

# MENU VARIABLES

circle_surf = pygame.image.load('graphics/circle.png').convert_alpha()
circle_surf_2 = pygame.image.load('graphics/circle2.png').convert_alpha()

circle_rect = circle_surf.get_rect(midright = (100,200))
circle_rect_2 = circle_surf_2.get_rect(midleft = (0,0))
circles = []
circles2 = []

title = pygame.image.load('graphics/game_title.png').convert_alpha()
title_rect = title.get_rect(center = (800,150))
arial_font_2 = pygame.font.Font('font/Arialn.ttf',50)
play_msg = arial_font_2.render('Tap to play!',True,'Red')
play_msg_rect = play_msg.get_rect(midtop = (800, 450))

# RULES VARIABLES

rules = pygame.image.load('graphics/rules.png').convert()
rules_rect = rules.get_rect(center = (120,70))
arial_font = pygame.font.Font('font/Arialn.ttf',40)
rules_text_1 = arial_font.render('1. Pieces can be placed as long as there are at least 1 adjacent enemy piece',True,'Black')
rules_text_2 = arial_font.render('2. When placing a piece, opposing pieces that are surrounded vertically, horizontally,',True,'Black')
rules_text_3 = arial_font.render('    and diagonally by two ends including the placed piece are flipped',True,'Black')
rules_text_4 = arial_font.render('3. Player with the most remaining pieces win the game',True,'Black')
rules_text_5 = arial_font.render('4. The 4 corner pieces cannot be flipped (tip)',True,'Black')
rules_texts = [rules_text_1,rules_text_2,rules_text_3,rules_text_4,rules_text_5]
rules_text_rect = rules_text_1.get_rect(midleft = (100, 300))

# MUSIC VARIABLES

music_button = pygame.image.load('graphics/toggle_music.png').convert()
music_button_2 = pygame.image.load('graphics/toggle_music_2.png').convert()
music_rect = music_button.get_rect(center = (70, 190))

bg_music = pygame.mixer.Sound('audio/kurukuru.mp3')
bg_music.set_volume(0.5)

# GAME VARIABLES

# board_surf = pygame.image.load('graphics/board.png').convert()
# board_rect = board_surf.get_rect(center = (800, 450))


surrender_surf = pygame.image.load('graphics/surrender.png').convert()
surrender_rect = surrender_surf.get_rect(center = (120,70))

piece_b = pygame.image.load('graphics/piece_1.png').convert_alpha()
piece_b_rect = piece_b.get_rect(center = (750,400))

piece_w = pygame.image.load('graphics/piece_2.png').convert_alpha()
piece_w_rect = piece_b.get_rect(center = (750,500))

# pieces_list = [piece_b_rect, 
#           piece_w_rect, 
#           piece_b.get_rect(center = (850,500)),
#           piece_w.get_rect(center = (850,400))]

player = pygame.sprite.GroupSingle()
player.add(Player())

board = pygame.sprite.Group()
board.add(Board('board',0,0))
board.add(Board('piece',True,piece_b.get_rect(center = (750,400))))
board.add(Board('piece',True,piece_b.get_rect(center = (850,500))))

circle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(circle_timer, 600)

circle_timer_2 = pygame.USEREVENT + 2
pygame.time.set_timer(circle_timer_2, 600)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if surrender_rect.collidepoint(event.pos):
                    menu = True
                    game_active = False
                    break
            
            
                
        if menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rules_rect.collidepoint(event.pos):
                    menu = False
                    rules_menu = True
                    break
                        
                elif music_rect.collidepoint(event.pos):
                    music_playing = not music_playing
                    if music_playing:
                        bg_music.play(loops = -1)
                    else:
                        bg_music.stop()
                
                else:
                    menu = False
                    game_active = True

            if event.type == circle_timer:
                circles.append(circle_surf.get_rect(center = (-200, randint(0,900))))

            if event.type == circle_timer_2:
                circles2.append(circle_surf_2.get_rect(center = (1800, randint(0,900))))

        if rules_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu = True
                rules_menu = False

        else:
            pass

    if menu:

        screen.fill('Green')
        circle_animation(circles)
        circle_animation_2(circles2)
        screen.blit(title,title_rect)
        screen.blit(play_msg,play_msg_rect)
        screen.blit(rules, rules_rect)
        if music_playing:
            screen.blit(music_button, music_rect)
        else: 
            screen.blit(music_button_2, music_rect)

    if rules_menu:
        
        screen.fill('White')
        rules_text_display(rules_texts)

    if game_active:

        screen.fill('White')
        # screen.blit(board_surf,board_rect)
        screen.blit(surrender_surf,surrender_rect)

        # pieces_display(pieces)

        player.update()

        board.update()

        # screen.blit(piece_b,piece_b_rect)




        

    pygame.display.update()
    clock.tick(60)