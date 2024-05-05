import random as rd

##### python labyrinth.py #####

def create_matrix(r, c, x):
    matriz = []
    for i in range(r):
        fila = []
        for j in range(c):
            fila.append(x) # Puedes reemplazar esto con cualquier valor que necesites
        matriz.append(fila)
    return matriz

def show_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end='')
        print()
    print()

def I_update(matrix, row, column):
    matrix[row][column] = 'I'

def valid_position(r, c, h, w):
    if (r >= 0 and r < h and c >= 0 and c < w):
        return True
    else:
        return False

def F_update(matrix, row, column, arr_pos_F):
    height = len(matrix)
    width = len(matrix[0])
    arr_valid_pos = []
    #print(row-1, column, height, width)
    if (valid_position(row-1, column, height, width)):
        arr_valid_pos.append((row-1, column))
    #print(row+1, column, height, width)
    if (valid_position(row+1, column, height, width)):
        arr_valid_pos.append((row+1, column))
    #print(row, column-1, height, width)
    if (valid_position(row, column-1, height, width)):
        arr_valid_pos.append((row, column-1))
    #print(row, column+1, height, width)
    if (valid_position(row, column+1, height, width)):
        arr_valid_pos.append((row, column+1))
    print(f"arr_valid_pos: {arr_valid_pos}")
    for (r, c) in arr_valid_pos:
        #validar cambiar a 'F' solo si tiene 'u'
        if (matrix[r][c] == 'u'):
            matrix[r][c] = 'F'
            arr_pos_F.append((r,c))

def exit_labyrinth_room_mm(rows, columns):
    r, c = 0, 0
    direction = rd.randint(0,3) # 0:↑ 1:↓ 2:← 3:→
    if direction == 0:
        r = 0
        c = rd.randint(0, columns-1)
    if direction == 1:
        r = rows - 1
        c = rd.randint(0, columns-1)
    if direction == 2:
        r = rd.randint(0, rows-1)
        c = 0
    if direction == 3:
        r = rd.randint(0, rows-1)
        c = columns - 1
    return r, c, direction

def func(r_origin, c_origin, r_destiny, c_destiny):
    r_m_w_o = int(((2*r_origin+1) + (2*r_destiny+1)) / 2)
    c_m_w_o = int(((2*c_origin+1) + (2*c_destiny+1)) / 2)
    print(f"== r_m_w_o, c_m_w_o: ({r_m_w_o, c_m_w_o}) ==")
    arr_down_walls.append((r_m_w_o, c_m_w_o))

def add_path(mini_matrix, coord_selected):
    row, column = coord_selected
    height = len(mini_matrix)
    width = len(mini_matrix[0])
    arr_valid_pos = []
    arr_pos_possible_origin = []
    if (valid_position(row-1, column, height, width)):
        arr_valid_pos.append((row-1, column))
    if (valid_position(row+1, column, height, width)):
        arr_valid_pos.append((row+1, column))
    if (valid_position(row, column-1, height, width)):
        arr_valid_pos.append((row, column-1))
    if (valid_position(row, column+1, height, width)):
        arr_valid_pos.append((row, column+1))
    print(f"arr_valid_pos: {arr_valid_pos}")
    for (r, c) in arr_valid_pos:
        #validar si tiene 'I' es un posible origen
        if (mini_matrix[r][c] == 'I'):
            #matrix[r][c] = 'F'
            arr_pos_possible_origin.append((r,c))
    
    index = rd.randint(0, len(arr_pos_possible_origin)-1)
    print(f"index: {index}")
    coord_origin = arr_pos_possible_origin.pop(index)
    print(f"arr_pos_possible_origin.pop(index): {coord_origin}")
    r_origin, c_origin = coord_origin
    # Agregar las coordenas al arr_down_walls
    func(r_origin, c_origin, row, column)

def create_solved_min_matrix(rows, columns):
    # if rows <= 2 and columns <= 2:
    #     print("Al menos 1 de los lados del laberinto debe ser mayor a 2")
    #     return
    if rows < 3 or columns < 3:
        print("Cada lado del laberinto debe ser mínimo 3 unidades")
        return
    arr_pos_F = []
    m = create_matrix(rows, columns, 'u')
    show_matrix(m)
    # Declarar la salida del laberinto
    r_exit, c_exit, direction = exit_labyrinth_room_mm(rows, columns)
    I_update(m, r_exit, c_exit)
    F_update(m, r_exit, c_exit, arr_pos_F)
    print(f"arr_pos_F: {arr_pos_F}")
    show_matrix(m)
    while len(arr_pos_F) > 0:
        print(f"len(arr_pos_F): {len(arr_pos_F)}")
        index = rd.randint(0, len(arr_pos_F)-1)
        print(f"index: {index}")
        coord_selected = arr_pos_F.pop(index)
        print(f"arr_pos_F.pop(index): {coord_selected}")
        add_path(m, coord_selected)

        r, c = coord_selected
        I_update(m, r, c)
        F_update(m, r, c, arr_pos_F)
        print(f"arr_pos_F: {arr_pos_F}")
        show_matrix(m)
    print("Se creó el laberinto exitosamente.")
    return m, r_exit, c_exit, direction

def make_path_in_matrix_wall(matrix_wall, r_exit, c_exit, direction):
    rows = len(matrix_wall)
    columns = len(matrix_wall[0])
    # Celdas vacías iniciales
    for r in range(rows):
        for c in range(columns):
            if r%2 == 1 and c%2 == 1:
                matrix_wall[r][c] = " "
    # Celda de salida
    r_m_w_e = 2*r_exit+1
    c_m_w_e = 2*c_exit+1
    ## 0:↑ 1:↓ 2:← 3:→
    if direction == 0:
        r_m_w_e -= 1
    if direction == 1:
        r_m_w_e += 1
    if direction == 2:
        c_m_w_e -= 1
    if direction == 3:
        c_m_w_e += 1
    matrix_wall[r_m_w_e][c_m_w_e] = " "
    # Celdas de camino
    for r, c in arr_down_walls:
        matrix_wall[r][c] = " "
    # EXTRA: multiconectado
    for r in range(rows):
        for c in range(columns):
            if (r%2 == 1 and c%2 == 0) or (r%2 == 0 and c%2 == 1) and matrix_wall[r][c] == "#":
                if r != 0 and c != 0 and r != rows-1 and c != columns-1:
                    random_number = rd.random()
                    if random_number < multi_connect_threshold:
                        matrix_wall[r][c] = " "
    return matrix_wall

def create_matrix_wall(mini_matrix, r_exit, c_exit, direction):
    rows = len(mini_matrix)
    columns = len(mini_matrix[0])
    matrix_wall = create_matrix(2*rows+1, 2*columns+1, "#")
    matrix_wall = make_path_in_matrix_wall(matrix_wall, r_exit, c_exit, direction)
    show_matrix(matrix_wall)


arr_down_walls = []
multi_connect_threshold = 0.3
m, r_e, c_e, d = create_solved_min_matrix(5, 9)
mw = create_matrix_wall(m, r_e, c_e, d)