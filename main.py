import numpy as np

def build_map(path: str) -> tuple[np.ndarray[float], tuple[int, int], tuple[int, int]]:
    matrix = []
    with open("entrada.txt", "r") as f:
        map = f.readlines()

        print("oi")
        print(map)
    
    for i, line in enumerate(map):
        matriz_line = []
        for j, c in enumerate(line):
            if c.isalnum():
                matriz_line.append(c)
            if c == "I":
                start_position = (i, j)
            if c == "F":
                end_position = (i, j)
                

        matrix.append(matriz_line)
    
    return np.array(matrix), start_position, end_position

# def a_star(map: np.ndarray) -> list:


def main():
    print(build_map("entrada.txt"))


if __name__ == "__main__":
    main()