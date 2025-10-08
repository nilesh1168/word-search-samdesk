def read_text_to_matrix(filename: str) -> list[list[str]]:
    """
    Reads a .txt file and converts it into a matrix of characters.
    
    Each line in the file becomes a row in the matrix.
    Blank lines (if any) are ignored.
    
    Example:
        Input file:
            MMMSXXMASM
            MSAMXMSMSA
        
        Output:
            [
                ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
                ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A']
            ]
    """
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # remove \n and spaces
            if line:  # ignore empty lines
                matrix.append(list(line))
    return matrix

def count_words(matrix: list[list[str]], word: str = "XMAS") -> int:
    rows, cols = len(matrix), len(matrix[0])
    word_len = len(word)
    found_positions = set()  # track coordinates used in any "XMAS"
    count = 0

    # Directions: 8 possible movements (dx, dy)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Search for "XMAS" starting from each position
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                # Try to match "XMAS" in this direction
                positions = []
                for k in range(word_len):
                    x, y = i + dx * k, j + dy * k
                    if not is_valid(x, y) or matrix[x][y] != word[k]:
                        break
                    positions.append((x, y))
                else:
                    # Found one occurrence
                    count += 1
                    found_positions.update(positions)

    # # Create visualization grid
    # visualization = [
    #     ['.' for _ in range(cols)] for _ in range(rows)
    # ]
    # for x, y in found_positions:
    #     visualization[x][y] = matrix[x][y]

    # # Print the visualization
    # for row in visualization:
    #     print(''.join(row))

    return count

if __name__ == "__main__":
    matrix = read_text_to_matrix("input.txt")
    result = count_words(matrix, "XMAS")
    print(f"Total 'XMAS' found: {result}")