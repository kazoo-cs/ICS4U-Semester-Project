import pygame
from sys import exit
from random import randint,choice
from time import time

# Recycle Bin

# self.row_1 = [0 + self.tile_img.get_rect(center = (450+100*x, 800)) for x in range(8)]
# self.row_2 = [0 + self.tile_img.get_rect(center = (450+100*x, 700)) for x in range(8)]
# self.row_3 = [0 + self.tile_img.get_rect(center = (450+100*x, 600)) for x in range(8)]
# self.row_4 = [0 + self.tile_img.get_rect(center = (450+100*x, 500)) for x in range(8)]
# self.row_5 = [0 + self.tile_img.get_rect(center = (450+100*x, 400)) for x in range(8)]
# self.row_6 = [0 + self.tile_img.get_rect(center = (450+100*x, 300)) for x in range(8)]
# self.row_7 = [0 + self.tile_img.get_rect(center = (450+100*x, 200)) for x in range(8)]
# self.row_8 = [0 + self.tile_img.get_rect(center = (450+100*x, 100)) for x in range(8)]

# self.board = [0, self.row_1, self.row_2, self.row_3, self.row_4, self.row_5, self.row_6, self.row_7, self.row_8]

# piece stuff
# if (750, 400) coord should be row 5 (3, 5)
# self.x_coord = ((rect.x - 450)//100)+1 
# self.y_coord = ((rect.y - 100)//-100)+8
# if player == True:
#     self.b = pygame.image.load('graphics/tile_b.png').convert_alpha()
#     self.b_rect = rect
#     # convert rect to list index
#     # change valie to tile with piece
#     # (3, 5) -> (750, 400)
#     self.board[self.x_coord][self.y_coord] = self.b.get_rect(center = (450+100*self.x_coord,))

#     self.piece_w = pygame.image.load('graphics/tile_w.png').convert_alpha()
#     self.w_rect = rect

# self.pieces = [self.piece_b.get_rect(center = (750,400)), self.piece_b.get_rect(center = (850, 500))]

# class Piece(pygame.sprite.Sprite):
#     def __init__(self, type, rect):
#         super().__init__()

#         if type == 'player':
#             self.flipped = False
#             self.img = pygame.image.load('graphics/piece_1.png').convert_alpha()
#             self.rect = self.img.get_rect(center = rect)

#         else:
#             self.flipped = True
#             self.img = pygame.image.load('graphics/piece_2.png').convert_alpha()
#             self.rect = self.img.get_rect(center = rect)

#         self.x_coord = ((self.rect.x - 450)//100)+1
#         self.y_coord = ((self.rect.y - 100)//-100)+8
#         self.position = (self.x_coord,self.y_coord)

#         '''
#         x -> 450,1150
#         y -> 100, 800

#         (1,1)
#         400,50 would be the bottom left
#         X: Examples (450, 100), (1150,800)
#         -450 (0)  (700)
#         /100 (0)  (7)
#         +1   (1)  (8)

#         Y: Examples (450, 100), (1150,800)
#         -100  (0)  (700)
#         /-100 (0)  (-7)
#         +8    (8)  (1)
#         '''
#     def display_piece(self):
#         screen.blit(self.img,self.rect)

#     def update(self):
#         self.display_piece()

class Player:
    def __init__(self):
        super().__init__()
        global event, player_turn, board
        self.turn = 0
        self.turn_display = arial_font.render(f'Turn: {self.turn}',False,'Black')
        self.turn_display_rect = self.turn_display.get_rect(center = (200,400))

        self.piece_num = 0
        self.piece_num_display = arial_font.render(f'Pieces: {self.piece_num}',False,'Black')
        self.piece_num_rect = self.piece_num_display.get_rect(center = (200,500))

        if player_turn:
            self.turn_side = arial_font.render(f'Turn: Player',False,'Black')
        else:
            self.turn_side = arial_font.render(f'Turn: Opponent',False,'Black')
        self.turn_side_rect = self.turn_side.get_rect(center = (200,600))

    def display_turn(self):
        self.turn_display = arial_font.render(f'Turn: {self.turn}',False,'Black')
        screen.blit(self.turn_display,self.turn_display_rect)
        return self.turn
    
    def display_side(self):
        if player_turn:
            self.turn_side = arial_font.render(f'Turn: Player',False,'Black')
        else:
            self.turn_side = arial_font.render(f'Turn: Opponent',False,'Black')
        self.turn_side_rect = self.turn_side.get_rect(center = (200,600))
        screen.blit(self.turn_side,self.turn_side_rect)

    def display_piece_num(self):
        self.piece_num_display = arial_font.render(f'Pieces: {self.get_pieces()}',False,'Black')
        screen.blit(self.piece_num_display,self.piece_num_rect)

    def get_pieces(self):
        self.piece_num = 0
        for x in board:
            if x.is_player():
                self.piece_num += 1
        return self.piece_num
    
    def get_opp_pieces(self):
        y = 0
        for x in board:
            if x.is_occupied() and not x.is_player():
                y += 1
        return y
    
    def get_total_occupied(self):
        x = 0
        for y in board:
            if y.is_occupied():
                x += 1
        return x

    def finish_turn(self):
        self.turn += 1

    def update(self):
        self.display_turn()
        self.display_piece_num()
        self.display_side()

class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pass


class Tile:
    def __init__(self, x, y, is_occupied, is_player):
        global event
        # tile stuff
        self.x = x
        self.y = y
        self.occupied = is_occupied
        self.player_piece = is_player
        if self.occupied:
            if self.player_piece:
                self.image = pygame.image.load('graphics/tile_b.png').convert()
            else:
                self.image = pygame.image.load('graphics/tile_w.png').convert()
        else:
            self.image = pygame.image.load('graphics/tile.png').convert()
        self.rect = self.image.get_rect(center = (450+100*x, 900-(y*100)))


    def player_turn(self):
        if self.occupied:
            self.image = pygame.image.load('graphics/tile_b.png').convert()
            self.rect = self.image.get_rect(center = (450+100*self.x, 900-(self.y*100)))
            self.player_piece = True
        else:
            self.image = pygame.image.load('graphics/tile_b.png').convert()
            self.rect = self.image.get_rect(center = (450+100*self.x, 900-(self.y*100)))
            self.occupied = True
            self.player_piece = True

    def opp_turn(self):
        if self.occupied:
            self.image = pygame.image.load('graphics/tile_w.png').convert()
            self.rect = self.image.get_rect(center = (450+100*self.x, 900-(self.y*100)))
            self.player_piece = False
        else:
            self.image = pygame.image.load('graphics/tile_w.png').convert()
            self.rect = self.image.get_rect(center = (450+100*self.x, 900-(self.y*100)))
            self.occupied = True
            self.player_piece = False

    def get_rect(self):
        return self.rect
    
    def get_y(self):
        return self.y
    
    def get_x(self):
        return self.x
    
    def get_coords(self):
        return (self.x, self.y)
    
    def is_player(self):
        return self.player_piece
    
    def is_occupied(self):
        return self.occupied
    
    def flip(self):
        self.player_piece = not self.player_piece

    def display(self):
        screen.blit(self.image,self.rect)

    def update(self):
        if self.player_piece == False and self.occupied:
            self.image = pygame.image.load('graphics/tile_w.png').convert()
            self.rect = self.image.get_rect(center = (450+100*self.x, 900-(self.y*100)))
        elif self.player_piece == True and self.occupied:
            self.image = pygame.image.load('graphics/tile_b.png').convert()
            self.rect = self.image.get_rect(center = (450+100*self.x, 900-(self.y*100)))
        


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

def placeable(target_index, obj_group):
    '''
    Must DETERMINE if clicked tile is available by the player
    It is already known that the tile clicked is UNOCCUPIED
    Conditions
    1. There is at least ONE adjacent ENEMY piece
    2. The ENEMY piece is being sandwitched by another PLAYER PIECE behind

    Steps
    1. IDENTIFY which adjacent tile has an ENEMY PIECE
    2. TRACE down each direction in which there is an ENEMY PIECE
        Ex. Let x and y be the target objects coordinates
        8 different trace checks
        (x,y+1)        UPWARD                  = START INDEX + 1
        (x+1,y+1)      DIAGONAL UPWARD RIGHT   = START INDEX + 9
        (x+1,y)        HORIZONTAL RIGHT        = START INDEX + 8
        (x+1,y-1)      DIAGONAL DOWNWARD RIGHT = START INDEX + 7
        (x,y-1)        DOWNWARD                = START INDEX - 1
        (x-1,y-1)      DIAGONAL DOWNWARD LEFT  = START INDEX - 9
        (x-1,y)        HORIZONTAL LEFT         = START INDEX - 8
        (x-1,y+1)      DIAGONAL UPWARD LEFT    = START INDEX - 7

    3. If direction has PLAYER OCCUPIED or UNOCCUPIED tile, it is marked as FALSE
       If direction has ENEMY OCCUPIED, temporarily mark as TRUE
       If direction is TRUE, use the same direction indicator (i.e. (x-1,y-1))
       If traced tile AFTER the previously identified ENEMY TILE is ANOTHER ENEMY TILE, mark as TRUE and continue
       If traced tile AFTER the previous is UNOCCUPIED, mark the entire direction as FALSE
       If traced tile FINDS EVEN ONE PLAYER tile, mark the entire direction as TRUE
       Having even ONE DIRECTION marked as TRUE will allow the tile to be OCCUPIED

    '''

    def upward(i,g,direction=True,count=1):
        if i+1 <= 63:
            if not g[i+1].is_occupied() or g[i+1].is_player() and count == 1: # FIRST CHECK. If EMPTY or is PLAYER, FALSE
                direction = False
                return direction
            elif not g[i+1].is_occupied() and count >= 2: # On 2+ checks, if unoccupied, FALSE
                direction = False
                return direction
            elif g[i+1].is_occupied() and g[i+1].is_player(): # if player after 2+ checks, TRUE
                direction = True
                for x in range(target_index, i+1):
                    g[x].flip()
                return direction
            elif g[i+1].is_occupied() and not g[i+1].is_player(): # If enemy piece on 1+ checks, RECURSIONNNN
                if ((i+1)-7)%8 == 0:
                    return False
                else:
                    return upward(i+1,g,direction,count+1)
        else:
            return False
            
    def downward(i,g,direction=True,count=1):
        if i-1 >= 0:
            if not g[i-1].is_occupied() or g[i-1].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i-1].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i-1].is_occupied() and g[i-1].is_player(): 
                direction = True
                for x in range(i,target_index):
                    g[x].flip()
                return direction
            elif g[i-1].is_occupied() and not g[i-1].is_player(): 
                if (i-1)%8 == 0:
                    return False
                else:
                    return downward(i-1,g,direction,count+1)
        else:
            return False
        
    def left(i,g,direction=True,count=1):
        if i-8 >= 0:
            if not g[i-8].is_occupied() or g[i-8].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i-8].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i-8].is_occupied() and g[i-8].is_player():
                direction = True
                for x in range(i,target_index,8):
                    g[x].flip()
                return direction
            elif g[i-8].is_occupied() and not g[i-8].is_player():
                return left(i-8,g,direction,count+1)
        else:
            return False
        
    def right(i,g,direction=True,count=1):
        if i+8 <= 63:
            if not g[i+8].is_occupied() or g[i+8].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i+8].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i+8].is_occupied() and g[i+8].is_player(): 
                direction = True
                for x in range(target_index,i+8,8):
                    g[x].flip()
                return direction
            elif g[i+8].is_occupied() and not g[i+8].is_player(): 
                return right(i+8,g,direction,count+1)
        else:
            return False
        
    def upward_right(i,g,direction=True,count=1):
        if i+9 <= 63:
            if not g[i+9].is_occupied() or g[i+9].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i+9].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i+9].is_occupied() and g[i+9].is_player(): 
                direction = True
                for x in range(target_index,i+9,9):
                    g[x].flip()
                return direction
            elif g[i+9].is_occupied() and not g[i+9].is_player(): 
                if ((i+1)-7)%8 == 0:
                    return False
                else:
                    return upward_right(i+9,g,direction,count+1)
        else:
            return False
        
    def downward_right(i,g,direction=True,count=1):
        if i+7 <= 63:
            if not g[i+7].is_occupied() or g[i+7].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i+7].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i+7].is_occupied() and g[i+7].is_player(): 
                direction = True
                for x in range(target_index,i+7,7):
                    g[x].flip()
                return direction
            elif g[i+7].is_occupied() and not g[i+7].is_player(): 
                if (i-1)%8 == 0:
                    return False
                else:
                    return downward_right(i+7,g,direction,count+1)
        else:
            return False
        
    def upward_left(i,g,direction=True,count=1):
        if i-7 >= 0:
            if not g[i-7].is_occupied() or g[i-7].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i-7].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i-7].is_occupied() and g[i-7].is_player(): 
                direction = True
                for x in range(i,target_index,7):
                    g[x].flip()
                return direction
            elif g[i-7].is_occupied() and not g[i-7].is_player(): 
                if ((i+1)-7)%8 == 0:
                    return False
                else:
                    return upward_left(i-7,g,direction,count+1)
        else:
            return False
        
    def downward_left(i,g,direction=True,count=1):
        if i-9 >= 0:
            if not g[i-9].is_occupied() or g[i-9].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i-9].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i-9].is_occupied() and g[i-9].is_player(): 
                direction = True
                for x in range(i,target_index,9):
                    g[x].flip()
                return direction
            elif g[i-9].is_occupied() and not g[i-9].is_player(): 
                if (i-1)%8 == 0:
                    return False
                else:
                    return downward_left(i-9,g,direction,count+1)
                
        else:
            return False
    
    available = 0
    if target_index % 8 == 0: # bottom row
        if upward(target_index, obj_group): 
            available += 1
        if left(target_index, obj_group): 
            available += 1
        if right(target_index, obj_group): 
            available += 1
        if upward_right(target_index, obj_group):
            available += 1
        if upward_left(target_index, obj_group):
            available += 1
    elif (target_index-7)%8 == 0: # top row
        if downward(target_index, obj_group): 
            available += 1
        if left(target_index, obj_group): 
            available += 1
        if right(target_index, obj_group): 
            available += 1
        if downward_right(target_index, obj_group): 
            available += 1
        if downward_left(target_index, obj_group): 
            available += 1
    else:
        if upward(target_index, obj_group): 
            available += 1
        if downward(target_index, obj_group): 
            available += 1
        if left(target_index, obj_group): 
            available += 1
        if right(target_index, obj_group): 
            available += 1
        if upward_right(target_index, obj_group): 
            available += 1
        if downward_right(target_index, obj_group): 
            available += 1
        if upward_left(target_index, obj_group): 
            available += 1
        if downward_left(target_index, obj_group): 
            available += 1
        
    if available >= 1:
        obj_group[target_index].player_turn()
        return True
    else:
        return False

def placeable_opp(target_index, obj_group):

    def upward(i,g,direction=True,count=1):
        if i+1 <= 63:
            if not g[i+1].is_occupied() or not g[i+1].is_player() and count == 1: # FIRST CHECK. If EMPTY or is PLAYER, FALSE
                direction = False
                return direction
            elif not g[i+1].is_occupied() and count >= 2: # On 2+ checks, if unoccupied, FALSE
                direction = False
                return direction
            elif g[i+1].is_occupied() and not g[i+1].is_player(): # if player after 2+ checks, TRUE
                direction = True
                for x in range(target_index, i+1):
                    g[x].flip()
                return direction
            elif g[i+1].is_occupied() and g[i+1].is_player(): # If enemy piece on 1+ checks, RECURSIONNNN
                if ((i+1)-7)%8 == 0:
                    return False
                else:
                    return upward(i+1,g,direction,count+1)
        else:
            return False
            
    def downward(i,g,direction=True,count=1):
        if i-1 >= 0:
            if not g[i-1].is_occupied() or not g[i-1].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i-1].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i-1].is_occupied() and not g[i-1].is_player(): 
                direction = True
                for x in range(i,target_index):
                    g[x].flip()
                return direction
            elif g[i-1].is_occupied() and g[i-1].is_player(): 
                if (i-1)%8 == 0:
                    return False
                else:
                    return downward(i-1,g,direction,count+1)
        else:
            return False
        
    def left(i,g,direction=True,count=1):
        if i-8 >= 0:
            if not g[i-8].is_occupied() or not g[i-8].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i-8].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i-8].is_occupied() and not g[i-8].is_player():
                direction = True
                for x in range(i,target_index,8):
                    g[x].flip()
                return direction
            elif g[i-8].is_occupied() and g[i-8].is_player(): 
                return left(i-8,g,direction,count+1)
        else:
            return False
        
    def right(i,g,direction=True,count=1):
        if i+8 <= 63:
            if not g[i+8].is_occupied() or not g[i+8].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i+8].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i+8].is_occupied() and not g[i+8].is_player(): 
                direction = True
                for x in range(target_index,i+8,8):
                    g[x].flip()
                return direction
            elif g[i+8].is_occupied() and g[i+8].is_player(): 
                return right(i+8,g,direction,count+1)
        else:
            return False
        
    def upward_right(i,g,direction=True,count=1):
        if i+9 <= 63:
            if not g[i+9].is_occupied() or not g[i+9].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i+9].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i+9].is_occupied() and not g[i+9].is_player(): 
                direction = True
                for x in range(target_index,i+9,9):
                    g[x].flip()
                return direction
            elif g[i+9].is_occupied() and g[i+9].is_player(): 
                if ((i+1)-7)%8 == 0:
                    return False
                else:
                    return upward_right(i+9,g,direction,count+1)
        else:
            return False
        
    def downward_right(i,g,direction=True,count=1):
        if i+7 <= 63:
            if not g[i+7].is_occupied() or not g[i+7].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i+7].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i+7].is_occupied() and not g[i+7].is_player(): 
                direction = True
                for x in range(target_index,i+7,7):
                    g[x].flip()
                return direction
            elif g[i+7].is_occupied() and g[i+7].is_player(): 
                if (i-1)%8 == 0:
                    return False
                else:
                    return downward_right(i+7,g,direction,count+1)
        else:
            return False
        
    def upward_left(i,g,direction=True,count=1):
        if i-7 >= 0:
            if not g[i-7].is_occupied() or not g[i-7].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i-7].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i-7].is_occupied() and not g[i-7].is_player(): 
                direction = True
                for x in range(i,target_index,7):
                    g[x].flip()
                return direction
            elif g[i-7].is_occupied() and g[i-7].is_player(): 
                if ((i+1)-7)%8 == 0:
                    return False
                else:
                    return upward_left(i-7,g,direction,count+1)
        else:
            return False
        
    def downward_left(i,g,direction=True,count=1):
        if i-9 >= 0:
            if not g[i-9].is_occupied() or not g[i-9].is_player() and count == 1: 
                direction = False
                return direction
            elif not g[i-9].is_occupied() and count >= 2: 
                direction = False
                return direction
            elif g[i-9].is_occupied() and not g[i-9].is_player(): 
                direction = True
                for x in range(i,target_index,9):
                    g[x].flip()
                return direction
            elif g[i-9].is_occupied() and g[i-9].is_player():
                if (i-1)%8 == 0:
                    return False
                else: 
                    return downward_left(i-9,g,direction,count+1)
        else:
            return False
    
    available = 0
    if target_index % 8 == 0: # bottom row
        if upward(target_index, obj_group): 
            available += 1
        if left(target_index, obj_group): 
            available += 1
        if right(target_index, obj_group): 
            available += 1
        if upward_right(target_index, obj_group):
            available += 1
        if upward_left(target_index, obj_group):
            available += 1
    elif (target_index-7)%8 == 0: # top row
        if downward(target_index, obj_group): 
            available += 1
        if left(target_index, obj_group): 
            available += 1
        if right(target_index, obj_group): 
            available += 1
        if downward_right(target_index, obj_group): 
            available += 1
        if downward_left(target_index, obj_group): 
            available += 1
    else:
        if upward(target_index, obj_group): 
            available += 1
        if downward(target_index, obj_group): 
            available += 1
        if left(target_index, obj_group): 
            available += 1
        if right(target_index, obj_group): 
            available += 1
        if upward_right(target_index, obj_group): 
            available += 1
        if downward_right(target_index, obj_group): 
            available += 1
        if upward_left(target_index, obj_group): 
            available += 1
        if downward_left(target_index, obj_group): 
            available += 1
    
    
    if available >= 1:
        obj_group[target_index].opp_turn()
        return True
    else:
        return False

pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption('AIthello')
clock = pygame.time.Clock()
game_active = False
player_turn = True
menu = True
rules_menu = False
score_screen = False
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
exit_button = arial_font_2.render('X',True,'Red')
exit_rect = exit_button.get_rect(topright = (1580,20))

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

skip_surf = pygame.image.load('graphics/skip.png').convert()
skip_rect = skip_surf.get_rect(center = (120,190))

piece_b = pygame.image.load('graphics/piece_1.png').convert_alpha()
piece_b_rect = piece_b.get_rect(center = (750,400))

piece_w = pygame.image.load('graphics/piece_2.png').convert_alpha()
piece_w_rect = piece_b.get_rect(center = (750,500))

player = Player()

board = []
for x in range(1,9):
    for y in range(1,9):
        if (x == 4 and y == 4) or (x == 5 and y == 5):
            board.append(Tile(x, y, True, True))
        elif (x == 4 and y == 5) or (x == 5 and y == 4):
            board.append(Tile(x, y, True, False))
        else:
            board.append(Tile(x, y, False, False))

# Score screen variables

retry_surf = pygame.image.load('graphics/retry.png').convert()
retry_rect = retry_surf.get_rect(center = (400,700))

exit_to_menu = pygame.image.load('graphics/menu.png').convert()
menu_exit_rect = exit_to_menu.get_rect(center = (1200,700))

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
                    menu = False
                    game_active = False
                    score_screen = True
                elif skip_rect.collidepoint(event.pos):
                    player_turn = not player_turn
                    player.finish_turn()
                else:
                    for x in range(0,64): # Cycles through board group using INDEX
                        if board[x].get_rect().collidepoint(event.pos) and not board[x].is_occupied() and player_turn:
                            if placeable(x,board):
                                player.finish_turn()
                                player_turn = not player_turn
                        elif board[x].get_rect().collidepoint(event.pos) and not board[x].is_occupied() and not player_turn:
                            if placeable_opp(x,board):
                                player.finish_turn()
                                player_turn = not player_turn
            if player.get_total_occupied() == 64:
                game_active = False
                score_screen = True
            if player.get_pieces() == 0:
                game_active = False
                score_screen = True
            if player.get_opp_pieces() == 0:
                game_active = False
                score_screen = True
                            
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

                elif exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()

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

        if score_screen:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(event.pos):
                    score_screen = False
                    game_active = True
                    player = Player()
                    board = []
                    for x in range(1,9):
                        for y in range(1,9):
                            if (x == 4 and y == 4) or (x == 5 and y == 5):
                                board.append(Tile(x, y, True, True))
                            elif (x == 4 and y == 5) or (x == 5 and y == 4):
                                board.append(Tile(x, y, True, False))
                            else:
                                board.append(Tile(x, y, False, False))
                    
                if menu_exit_rect.collidepoint(event.pos):
                    score_screen = False
                    menu = True
                    player = Player()
                    board = []
                    for x in range(1,9):
                        for y in range(1,9):
                            if (x == 4 and y == 4) or (x == 5 and y == 5):
                                board.append(Tile(x, y, True, True))
                            elif (x == 4 and y == 5) or (x == 5 and y == 4):
                                board.append(Tile(x, y, True, False))
                            else:
                                board.append(Tile(x, y, False, False))
                    pass
            

    if menu:
        screen.fill('Green')
        circle_animation(circles)
        circle_animation_2(circles2)
        screen.blit(title,title_rect)
        screen.blit(play_msg,play_msg_rect)
        screen.blit(rules, rules_rect)
        screen.blit(exit_button,exit_rect)
        if music_playing:
            screen.blit(music_button, music_rect)
        else: 
            screen.blit(music_button_2, music_rect)

    if rules_menu:
        screen.fill('White')
        rules_text_display(rules_texts)

    if game_active:
        screen.fill('White')
        screen.blit(surrender_surf,surrender_rect)
        screen.blit(skip_surf,skip_rect)

        player.update()

        for x in board:
            x.update()
            x.display()
    if score_screen:
        if player.get_pieces() == player.get_opp_pieces():
            #draw 
            screen.fill('Yellow')
            end_msg = arial_font.render(f'Draw!',True,'White')
            pass
        elif player.get_pieces() > player.get_opp_pieces():
            #win
            screen.fill('Green')
            end_msg = arial_font.render(f'Player won with a difference of {player.get_pieces() - player.get_opp_pieces()}',True,'White') 
            pass
        else:
            #loss
            screen.fill('Red')
            end_msg = arial_font.render(f'Player lost with a difference of {player.get_opp_pieces() - player.get_pieces()}',True,'White')
            pass
        screen.blit(end_msg,end_msg.get_rect(center = (800,450)))
        screen.blit(retry_surf,retry_rect)
        screen.blit(exit_to_menu,menu_exit_rect)
    pygame.display.update()
    clock.tick(60)