import pygame,os
import random
import sudoku

def contained_in(pt):
    #3,63
    for r in range(9):
        for c in range(9):
            if pt[0] >= (3+(53*c)) and pt[0] <= (53+(53*c)) and pt[1] >= (63+(53*r)) and pt[1] <= (113+(53*r)):
                return c,r
    return False

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = '11,30'
size = w,h = 480,540
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku Solver")
dull_grey = (210,210,210)
white = (255,255,255)
black = (0,0,0)
screen.fill(white)

orange = (255,133,24)

background = pygame.image.load(os.path.relpath("boxes.png"))
highlight = pygame.image.load(os.path.relpath("highlight.png"))
halo = pygame.image.load(os.path.relpath("chosen.png"))
small_font = pygame.font.SysFont("Lucida Console", 16)
big_font = pygame.font.SysFont("Lucida Console", 45)
numbers = []
little_numbers = []
for i in range(9):
    numbers.append(big_font.render(str(i+1), 1, black))
    little_numbers.append(small_font.render(str(i+1), 1, black))

#input
done = False
selected = ()
board = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    screen.fill(white)
    for i in range(9):
        screen.blit(numbers[i],(60+(48*i),10))
    screen.blit(background,(0,60))
    slot = contained_in(pygame.mouse.get_pos())
    if slot:
        screen.blit(highlight,(4+(53*slot[0]),63+(53*slot[1])))
        if pygame.mouse.get_pressed()[0]:
            selected = slot
    if selected:
        screen.blit(halo,(4+(53*selected[0]),63+(53*selected[1])))
        if pygame.mouse.get_pos()[1] < 60 and pygame.mouse.get_pressed()[0]:
            num = pygame.mouse.get_pos()[0]/48
            board[selected[1]][selected[0]] = str(int(num))
    for r in range(9):
        for c in range(9):
            if board[r][c] in ("1","2","3","4","5","6","7","8","9"):
                screen.blit(numbers[int(board[r][c])-1],(16+(53*c),68+(53*r)))
    pygame.display.flip()

#easy
##board = [[0,"2","4",0,"7",0,"3",0,0],
##         ["9",0,0,"3",0,"1",0,0,0],
##         ["3",0,0,0,0,"9",0,0,"6"],
##         [0,0,0,0,0,0,"4","6",0],
##         ["1",0,0,0,0,0,0,0,"2"],
##         [0,"3","2",0,0,0,0,0,0],
##         ["5",0,0,"6",0,0,0,0,"4"],
##         [0,0,0,"2",0,"8",0,0,"3"],
##         ["2",0,"9",0,0,0,"7","5",0]]
##
###moderate - COMPLETE
##board = [[0,0,0,0,"9",0,0,0,"7"],
##         [0,"6",0,0,0,0,0,"5","2"],
##         [0,0,0,"7",0,0,0,0,0],
##         [0,0,0,0,"1","2",0,"8","4"],
##         [0,0,"2",0,0,0,"3",0,0],
##         ["4","1",0,"3","8",0,0,0,0],
##         [0,0,0,0,"6","8",0,0,0],
##         ["1","7",0,"5",0,0,0,"4","6"],
##         ["9",0,0,0,"3",0,0,0,0]]
##
###diabolical
##board = [[0,0,0,0,"1",0,0,"7","9"],
##         [0,0,"1",0,0,"4","2",0,0],
##         [0,0,0,0,"7",0,0,"8",0],
##         ["4",0,"7","6",0,"2",0,0,0],
##         [0,"6",0,0,0,0,0,"4",0],
##         [0,0,0,"8",0,"5",0,0,"3"],
##         [0,"1",0,0,"6",0,0,0,0],
##         [0,0,"6","7",0,0,"4",0,0],
##         ["3","9",0,0,0,0,0,0,0]]

board = sudoku.reallot(board)

#output
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    screen.fill(white)
    for r in range(9):
        for c in range(9):
            if board[r][c] in ("1","2","3","4","5","6","7","8","9"):
                screen.blit(numbers[int(board[r][c])-1],(16+(53*c),68+(53*r)))
            elif board[r][c] != "0" and board[r][c] != 0:
                for p in range(len(board[r][c])):
                    y = 0
                    if p > 5:
                        y = 30
                    elif p > 2:
                        y = 15
                    screen.blit(little_numbers[int(board[r][c][p])-1],(8+(53*c)+(15*(p%3)),66+(53*r)+y))
    screen.blit(background,(0,60))
    pygame.display.flip()
    board = sudoku.solve(board)
    #print "solving..."
pygame.quit()
