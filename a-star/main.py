import numpy as np

class Cell:
    def __init__(self, char: str, l: int, c: int) -> None:
        self.is_free = False if char == "0" else True # True if char is 1, I or F
        self.cost = 0
        self.char = char
        self.l = l
        self.c = c
        self.is_opened = False
        self.is_expanded = False

def build_map(path: str) -> tuple[np.ndarray, tuple[int, int] | None, tuple[int, int] | None]:
    matrix = []
    with open("entrada.txt", "r") as f:
        map = f.readlines()
    
    start_position = None
    end_position = None
    for i, line in enumerate(map):
        matriz_line = []

        for j, c in enumerate(line):
            if c.isalnum(): # Ignores /n
                matriz_line.append(Cell(c, i, j))
            if c == "I":
                start_position = (i, j)
            if c == "F":
                end_position = (i, j)
                

        matrix.append(matriz_line)
    
    return np.array(matrix), start_position, end_position

def find_lower_cell_cost(cells: list[Cell]) -> Cell | None:
    lower = None
    for cell in cells:
        if lower == None:
            lower = cell
        else:
            if cell.cost < lower.cost:
                lower = cell
    return lower

def find_adjacent_cells(map: np.ndarray, cell: Cell) -> tuple[Cell] | None:
    len_l = map.shape[0]
    len_c = map.shape[1]
    adjacent_cells = []

    # Up
    if cell.l - 1 >= 0:
        up_cell = map[cell.l - 1, cell.c]
        if up_cell.is_free and not up_cell.is_opened and not up_cell.is_expanded:
            adjacent_cells.append(up_cell)

    # Right
    if cell.c + 1 < len_c:
        right_cell = map[cell.l, cell.c + 1]
        if right_cell.is_free and not right_cell.is_opened and not right_cell.is_expanded:
            adjacent_cells.append(right_cell)

    # Down
    if cell.l + 1 < len_l:
        down_cell = map[cell.l + 1, cell.c]
        if down_cell.is_free and not down_cell.is_opened and not down_cell.is_expanded:
            adjacent_cells.append(down_cell)
    
    # Left
    if cell.c - 1 >= 0:
        left_cell = map[cell.l, cell.c - 1]
        if left_cell.is_free and not left_cell.is_opened and not left_cell.is_expanded:
            adjacent_cells.append(left_cell)
    
    return tuple(adjacent_cells)

def open_cell(opened_cells: list, cell: Cell, parent: Cell) -> None:
    cell.cost = parent.cost + 1
    cell.is_opened = True
    opened_cells.append(cell)

def expand_cell(expanded_cells: list, opened_cells: list) -> Cell | None:
    curr = find_lower_cell_cost(opened_cells)
    if curr:
        opened_cells.remove(curr)
        curr.is_expanded = True
        expanded_cells.append(curr)
        return curr
    else:
        print("curr = None in expand_cell()")
        exit()


def a_star(map: np.ndarray, start: Cell) -> list:
    opened_cells = []
    expanded_cells = []

    opened_cells.append(start)

    while(len(opened_cells) > 0):
        curr = expand_cell(expanded_cells, opened_cells)
        if curr:
            if curr.char == "F":
                return expanded_cells
            else:
                adj_cells = find_adjacent_cells(map, curr)
                if adj_cells:
                    for cell in adj_cells:
                        open_cell(opened_cells, cell, curr)
    return expanded_cells

def build_path(expanded_cells: list) -> tuple:
    path = []
    end = expanded_cells[-1]
    path.append(end)

    while(True):
        cell = None
        for cell in expanded_cells:
            if cell.cost == end.cost - 1:
                if cell.c + 1 == end.c or cell.c - 1 == end.c or cell.c == end.c:
                    if cell.l + 1 == end.l or cell.l - 1 == end.l or cell.l == end.l:
                        path.append(cell)
                        break
        if cell:
            if cell.cost == 0:
                return tuple(path)
        else:
            print("cell is None in build_path()!")
            exit()
        end = cell



def main():
    map, start, end = (build_map("entrada.txt"))

    l = c = 0
    if start:
        l, c = start
    expanded_cells = a_star(map, map[l, c])

    path = build_path(expanded_cells)

    for cell in path:
        print((cell.l, cell.c))
    
    print(f"lower_path_cost: {path[0].cost}")


if __name__ == "__main__":
    main()