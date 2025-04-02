from collections import deque

def is_solvable(puzzle):
    # Проверяет, можно ли решить головоломку
    inversions = 0
    n = len(puzzle)
    for i in range(n):
        if puzzle[i] == 0:
            row = i // 4
            continue
        for j in range(i+1, n):
            if puzzle[j] == 0:
                continue
            if puzzle[i] > puzzle[j]:
                inversions += 1
    
    if (row % 2 == 0 and inversions % 2 == 1) or (row % 2 == 1 and inversions % 2 == 0):
        return True
    return False

def solve_puzzle(puzzle):
    # Находит решение головоломки, если оно существует
    if not is_solvable(puzzle):
        return []
    
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Вправо, вниз, влево, вверх
    
    # Преобразуем список в кортеж для хранения в visited
    start = tuple(puzzle)
    queue = deque([(start, [])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        if list(current) == goal:
            return path
        
        zero_pos = current.index(0)
        x, y = zero_pos // 4, zero_pos % 4
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                new_pos = nx * 4 + ny
                new_puzzle = list(current)
                new_puzzle[zero_pos], new_puzzle[new_pos] = new_puzzle[new_pos], new_puzzle[zero_pos]
                new_state = tuple(new_puzzle)
                
                if new_state not in visited:
                    moved_number = current[new_pos]
                    visited.add(new_state)
                    queue.append((new_state, path + [moved_number]))
    
    return []

# Пример использования
if __name__ == "__main__":
    puzzle = list(map(int, input("Введите расстановку (16 чисел через пробел): ").split()))
    if len(puzzle) != 16:
        print("Некорректный ввод. Нужно 16 чисел.")
    else:
        solution = solve_puzzle(puzzle)
        if not solution:
            print("Данная расстановка не имеет решения.")
        else:
            print("Последовательность ходов для решения:", solution)