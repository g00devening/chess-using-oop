import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Chess')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
FPS = 60

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
# 0 - ход белых, фигура не выбрана; 1 - ход белых, фигура выбрана;
# 2 - ход чёрных, фигура не выбрана; 3 - ход чёрных, фигура не выбрана
turn_step = 0
# 100 - никакая фигура не выбрана, для каждой фигуры своё число
selection = 100
valid_moves = []
# загрузка картиночек
black_queen = pygame.image.load('assets/images/black queen.svg')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/images/black king.svg')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.svg')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.svg')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.svg')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.svg')
black_pawn = pygame.transform.scale(black_pawn, (80, 80))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.svg')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.svg')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.svg')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.svg')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.svg')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.svg')
white_pawn = pygame.transform.scale(white_pawn, (80, 80))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

counter = 0
winner = ''
game_over = False
white_castling_short = True
white_castling_long = True
black_castling_short = True
black_castling_long = True
white_promotion = False
black_promotion = False


# рисует доску
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
        for j in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * j), (800, 100 * j), 2)
            pygame.draw.line(screen, 'black', (100 * j, 0), (100 * j, 800), 2)
        screen.blit(medium_font.render('RESIGN', True, 'black'), (820, 830))


# рисует фигуры на доске
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                 100, 100], 2)


# возвращает список с возможными ходами для каждой фигуры
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# проверяет возможные ходы короля
def check_king(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# проверяет возможные ходы ферзя
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


# проверяет возможные ходы слона
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# проверяет возможные ходы ладьи
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# проверяет возможные ходы коня
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# проверяет возможные ходы пешки
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        # ход на 1 клетку
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        # ход на 2 клетки
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        # взятие
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        # ход на 1 клетку
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        # ход на 2 клетки
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        # взятие
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list


# проверяет вохможные ходы для выбранной фигуры
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# рисует возможные ходы на доске
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


# рисует съеденные фигуры с краю
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50 * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50 * i))


# рисует окошко конца игры
def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 350, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (302, 360))
    screen.blit(font.render('press ENTER to restart!', True, 'white'), (290, 390))


# рисует мигающую обводку вокруг короля, когда тот под шахом
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,
                                                              white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)


# проверяет возможные варианты для рокировки
def check_castling():
    castling_options = []
    white_options_1d = []
    black_options_1d = []
    all_locations = white_locations + black_locations
    for i in range(len(white_pieces)):
        for j in white_options[i]:
            white_options_1d.append(j)
    for i in range(len(black_pieces)):
        for j in black_options[i]:
            black_options_1d.append(j)

    if white_castling_short and (1, 0) not in black_options_1d and \
            (2, 0) not in black_options_1d and (3, 0) not in black_options_1d and \
            (1, 0) not in all_locations and (2, 0) not in all_locations:
        castling_options.append((1, 0))
    if white_castling_long and (5, 0) not in black_options_1d and \
            (4, 0) not in black_options_1d and (3, 0) not in black_options_1d and \
            (4, 0) not in all_locations and (5, 0) not in all_locations and (6, 0) not in all_locations:
        castling_options.append((5, 0))
    if black_castling_short and (1, 7) not in white_options_1d and \
            (2, 7) not in white_options_1d and (3, 7) not in white_options_1d and \
            (1, 7) not in all_locations and (2, 7) not in all_locations:
        castling_options.append((1, 7))
    if black_castling_long and (5, 7) not in white_options_1d and \
            (4, 7) not in white_options_1d and (3, 7) not in white_options_1d and \
            (4, 7) not in all_locations and (5, 7) not in all_locations and (6, 7) not in all_locations:
        castling_options.append((5, 7))
    return castling_options


black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True
while run:
    timer.tick(FPS)
    # штучка для мигания клетки
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    castling_squares = check_castling()
    # проверка на потерю прав для рокировки
    if (3, 0) in white_locations and (0, 0) in white_locations:
        if white_pieces[white_locations.index((3, 0))] != 'king' or white_pieces[white_locations.index((0, 0))] != 'rook':
            white_castling_short = False
    else:
        white_castling_short = False
    if (3, 0) in white_locations and (7, 0) in white_locations:
        if white_pieces[white_locations.index((3, 0))] != 'king' or white_pieces[white_locations.index((7, 0))] != 'rook':
            white_castling_long = False
    else:
        white_castling_long = False
    if (3, 7) in black_locations and (0, 7) in black_locations:
        if black_pieces[black_locations.index((3, 7))] != 'king' or black_pieces[black_locations.index((0, 7))] != 'rook':
            black_castling_short = False
    else:
        black_castling_short = False
    if (3, 7) in black_locations and (7, 7) in black_locations:
        if black_pieces[black_locations.index((3, 7))] != 'king' or black_pieces[black_locations.index((7, 7))] != 'rook':
            black_castling_long = False
    else:
        black_castling_long = False
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    # вывод окошка выбора фигуры при проведении пешки
    if white_promotion:
        pygame.draw.rect(screen, 'black', [200, 350, 400, 50])
        screen.blit(white_queen_small, (230, 350))
        screen.blit(white_rook_small, (330, 350))
        screen.blit(white_knight_small, (430, 350))
        screen.blit(white_bishop_small, (530, 350))
    if black_promotion:
        pygame.draw.rect(screen, 'black', [200, 350, 400, 50])
        screen.blit(black_queen_small, (230, 350))
        screen.blit(black_rook_small, (330, 350))
        screen.blit(black_knight_small, (430, 350))
        screen.blit(black_bishop_small, (530, 350))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            # выбор фигуры для превращения пешки
            if white_promotion:
                if click_coords == (2, 3):
                    white_pieces[promoted_pawn] = "queen"
                elif click_coords == (3, 3):
                    white_pieces[promoted_pawn] = "rook"
                elif click_coords == (4, 3):
                    white_pieces[promoted_pawn] = "knight"
                elif click_coords == (5, 3):
                    white_pieces[promoted_pawn] = "bishop"
                white_promotion = False
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')
                turn_step = 2
                selection = 100
                valid_moves = []
                break
            if black_promotion:
                if click_coords == (2, 3):
                    black_pieces[promoted_pawn] = "queen"
                elif click_coords == (3, 3):
                    black_pieces[promoted_pawn] = "rook"
                elif click_coords == (4, 3):
                    black_pieces[promoted_pawn] = "knight"
                elif click_coords == (5, 3):
                    black_pieces[promoted_pawn] = "bishop"
                black_promotion = False
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')
                turn_step = 0
                selection = 100
                valid_moves = []
                break
            if turn_step <= 1:
                # проверка на нажатие кнопки "сдаться"
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if turn_step == 1:
                    # рокировка
                    if click_coords in castling_squares and white_pieces[selection] == 'king':
                        if click_coords == (1, 0):
                            white_locations[selection] = click_coords
                            white_locations[0] = (2, 0)
                        elif click_coords == (5, 0):
                            white_locations[selection] = click_coords
                            index = white_locations.index((7, 0))
                            white_locations[index] = (4, 0)
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 2
                        selection = 100
                        valid_moves = []
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    # достижение пешкой последней линии
                    if click_coords[1] == 7 and white_pieces[selection] == 'pawn':
                        white_promotion = True
                        promoted_pawn = selection
                        if click_coords in black_locations:
                            black_piece = black_locations.index(click_coords)
                            captured_pieces_white.append(black_pieces[black_piece])
                            if black_pieces[black_piece] == 'king':
                                winner = 'white'
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                        break
                    # взятие вражеской фигуры
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []

            elif turn_step > 1:
                # роверка на нажатие кнопки "сдаться"
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if turn_step == 3:
                    # рокировка
                    if click_coords in castling_squares and black_pieces[selection] == 'king':
                        if click_coords == (1, 7):
                            black_locations[selection] = click_coords
                            black_locations[0] = (2, 7)
                        elif click_coords == (5, 7):
                            black_locations[selection] = click_coords
                            index = black_locations.index((7, 7))
                            black_locations[index] = (4, 7)
                        black_options = check_options(black_pieces, black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        turn_step = 0
                        selection = 100
                        valid_moves = []
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    # достижение пешкой последней линии
                    if click_coords[1] == 0 and black_pieces[selection] == 'pawn':
                        black_promotion = True
                        promoted_pawn = selection
                        if click_coords in white_locations:
                            white_piece = white_locations.index(click_coords)
                            captured_pieces_black.append(white_pieces[white_piece])
                            if white_pieces[white_piece] == 'king':
                                winner = 'black'
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)
                        break
                    # взятие вражеской фигуры
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        # перезапуск игры
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')
                white_castling_short = True
                white_castling_long = True
                black_castling_short = True
                black_castling_long = True
                white_promotion = False
                black_promotion = False
    if winner != '':
        game_over = True
        draw_game_over()
    pygame.display.flip()
pygame.quit()
