from collections import deque
from typing import List, Tuple, Set, Deque

# Константы для замены магических чисел
BOARD_SIZE = 4  # Размер доски 4x4
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
GOAL_STATE = tuple(range(1, BOARD_SIZE**2)) + (0,)  # Финишное состояние (1,2,3,...,15,0)

def count_inversions_and_empty_row(puzzle: List[int]) -> Tuple[int, int]:
    inversions = 0
    empty_row = 0
    for i in range(len(puzzle)):
        if puzzle[i] == 0:
            empty_row = i // BOARD_SIZE
            continue
        for j in range(i + 1, len(puzzle)):
            if puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inversions += 1
    return inversions, empty_row

def is_puzzle_solvable(puzzle: List[int]) -> bool:
    inversions, empty_row = count_inversions_and_empty_row(puzzle)
    is_even_row = (empty_row % 2 == 0)
    has_odd_inversions = (inversions % 2 == 1)
    return is_even_row == has_odd_inversions

def generate_next_state(state: Tuple[int, ...], empty_pos: int, new_pos: int) -> Tuple[int, ...]:
    new_state = list(state)
    new_state[empty_pos], new_state[new_pos] = new_state[new_pos], new_state[empty_pos]
    return tuple(new_state)

def solve_15_puzzle(initial_state: List[int]) -> List[int]:
    if not is_puzzle_solvable(initial_state):
        return []

    queue: Deque[Tuple[Tuple[int, ...], List[int]]] = deque([(tuple(initial_state), [])])
    visited: Set[Tuple[int, ...]] = {tuple(initial_state)}

    while queue:
        current_state, path = queue.popleft()
        
        if current_state == GOAL_STATE:
            return path

        empty_pos = current_state.index(0)
        row, col = empty_pos // BOARD_SIZE, empty_pos % BOARD_SIZE

        for delta_row, delta_col in DIRECTIONS:
            new_row, new_col = row + delta_row, col + delta_col
            if 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE:
                new_pos = new_row * BOARD_SIZE + new_col
                next_state = generate_next_state(current_state, empty_pos, new_pos)
                
                if next_state not in visited:
                    moved_tile = current_state[new_pos]
                    visited.add(next_state)
                    queue.append((next_state, path + [moved_tile]))
    
    return []

def main():
    
    print("Введите начальное состояние (16 чисел через пробел, 0 - пустая клетка):")
    try:
        puzzle = list(map(int, input().split()))
        if len(puzzle) != 16:
            print("Ошибка: нужно ввести ровно 16 чисел")
            return
        
        solution = solve_15_puzzle(puzzle)
        
        if solution:
            print("Последовательность ходов:", solution)
            print(f"Всего ходов: {len(solution)}")
        else:
            print("Данная расстановка не имеет решения")
    except ValueError:
        print("Ошибка: все элементы должны быть числами")

if __name__ == "__main__":
    main()