#Imports
import pygame
import random

#Initialization
screen_width = 675
screen_height = 675
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Super TicTacToe")
clock = pygame.time.Clock()
in_game = True
player = random.choice([1,-1])
surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
clicked = False
next_move = []
winners = []
won_cell = []
valid =True
cell_remove = False
board = []
for i in range(3):
    board.append([0]*3)
main_board =[[[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]]

#Functions
#Draw Board
line_width = 6
def draw_board():

    y_pos = 0
    x_pos = 15
    for z in range(3):
        x_pos = 15
        for x in range(3):
            for y in range(1,3):
                pygame.draw.line(surface,(255,255,255,100),(x_pos,y*75+y_pos),(x_pos+195,y*75+y_pos),line_width)
                pygame.draw.line(surface,(255,255,255,100),(y*75+y_pos,x_pos),(y*75+y_pos,x_pos+195),line_width)
            x_pos+=225
        y_pos+=225
            
         
    for x in range(1,3):
        pygame.draw.line(surface,(255,255,255),(0,x*225),(screen_width,x*225),line_width)
        pygame.draw.line(surface,(255,255,255),(x*225,0),(x*225,screen_height),line_width)

#Board
#Check Win
def check_win(board):
    y_pos = 0
    win = False
    winner = 0
    for x in board:
        #Columns
        if sum(x) == 3:
           win = True
           winner = 1
        elif sum(x) == -3:
            win = True
            winner = -1
        #Rows
        elif board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == 3:
            win = True
            winner = 1
        elif board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == -3:
            win = True
            winner = -1
        y_pos += 1
    
    #Diagonals
    if (board[0][0] + board[1][1] + board[2][2] == 3) or (board[0][2] + board[1][1] + board[2][0] == 3):
        win = True
        winner = 1
    elif(board[0][0] + board[1][1] + board[2][2] == -3) or (board[0][2] + board[1][1] + board[2][0] == -3):
        win = True
        winner = -1
    return [win,winner]
    
#Valid move or no
def checkvalidmove(forced_cell,current_pos):

    allowed = False
    escape = False
    if forced_cell == []:
        allowed = True
    if [current_pos[0]//225,current_pos[1]//225] == forced_cell:
        allowed = True
    elif forced_cell != [] and [current_pos[0]//225,current_pos[1]//225] != forced_cell:
        for cell in main_board[forced_cell[0]][forced_cell[1]]:
            for fixed_cell in cell:
                if fixed_cell == 0:
                    allowed = False
                    escape = True
                    break
                else:
                    allowed = True
            if escape:
                break
        
    
    return allowed

#Draw on board
def draw_XO():

    x_pos = 0
    y_pos = 0
    main_row = 0
    main_column = 0
    for column in main_board:
        for cell in column:
            for column2 in cell:
                for cell2 in column2:
                    if cell2 == 1:
                        pygame.draw.line(screen,'red',(main_row*225+x_pos*75+15,main_column*225+y_pos*75+15),(main_row*225+x_pos*75+60,main_column*225+y_pos*75+60),line_width)
                        pygame.draw.line(screen,'red',(main_row*225+x_pos*75+15,main_column*225+y_pos*75+60),(main_row*225+x_pos*75+60,main_column*225+y_pos*75+15),line_width)
                    elif cell2 == -1:
                        radius = 25
                        pygame.draw.circle(screen,'blue',(main_row*225+x_pos*75+35,main_column*225+y_pos*75+35),radius,line_width)
                    y_pos += 1
                y_pos= 0
                x_pos+=1
            x_pos = 0
            main_column+=1
        main_row+=1
        main_column=0

#Check main game
def check_main(wins,winner):

    z = 0
    line_thick = 12
    for i in wins:
        board[i[0]][i[1]] = winner[z] 
        z+=1
    x_pos = 0
    for x in board:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen,'red',(x_pos*225+30,y_pos*225+30),(x_pos*225+205,y_pos*225+205),line_thick)
                pygame.draw.line(screen,'red',(x_pos*225+30,y_pos*225+205),(x_pos*225+205,y_pos*225+30),line_thick)
            elif y == -1:
                radius = 100
                pygame.draw.circle(screen,'blue',(x_pos*225+120,y_pos*225+120),radius,line_thick)
            y_pos += 1
        x_pos+=1

    
#Real game check
def final_check(wins,winner):

    z = 0
    run = True
    for i in wins:
        board[i[0]][i[1]] = winner[z] 
        z+=1
        y_pos = 0
    for x in board:
        #Columns
        if sum(x) == 3:
            print("X wins")
            run = False
        elif sum(x) == -3:
            print("O wins")
            run = False
        #Rows
        elif board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == 3:
            print("X wins")
            run = False
        elif board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == -3:
            print("O Wins")
            run = False
        y_pos += 1
    
    #Diagonals
    if (board[0][0] + board[1][1] + board[2][2] == 3) or (board[0][2] + board[1][1] + board[2][0] == 3):
        print("X Wins")
        run = False
    elif(board[0][0] + board[1][1] + board[2][2] == -3) or (board[0][2] + board[1][1] + board[2][0] == -3):
        print("O Wins")
        run = False
    return run

while in_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_game = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            mouse_pos = pygame.mouse.get_pos()
            if main_board[mouse_pos[0]//225][mouse_pos[1]//225][mouse_pos[0]//75-(mouse_pos[0]//225)*3][mouse_pos[1]//75-(mouse_pos[1]//225)*3] == 0:
                valid = checkvalidmove(next_move,mouse_pos)
                if valid:
                    main_board[mouse_pos[0]//225][mouse_pos[1]//225][mouse_pos[0]//75-(mouse_pos[0]//225)*3][mouse_pos[1]//75-(mouse_pos[1]//225)*3] = player
                    next_move = [mouse_pos[0]//75-(mouse_pos[0]//225)*3,mouse_pos[1]//75-(mouse_pos[1]//225)*3]
                    player *= -1
                    win_checker =check_win(main_board[mouse_pos[0]//225][mouse_pos[1]//225])
                    cell_remove = win_checker[0]
                    if cell_remove:
                        if [mouse_pos[0]//225,mouse_pos[1]//225] not in won_cell:
                            won_cell.append([mouse_pos[0]//225,mouse_pos[1]//225])
                            if win_checker[1] != 0:
                                winners.append(win_checker[1])
                        cell_remove = False
                        in_game = final_check(won_cell,winners)
                    valid = False

    screen.fill((0,0,0))
    draw_board()
    draw_XO()
    check_main(won_cell,winners)
    screen.blit(surface,(0,0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()