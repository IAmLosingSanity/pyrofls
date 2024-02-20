def count_friendly_elements(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    friendly_count = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def dfs(row, col, visited):
        # Check if the current position is out of bounds or already visited
        if row < 0 or col < 0 or row >= rows or col >= cols or visited[row][col]:
            return 0
        
        visited[row][col] = True  # Mark the current cell as visited
        
        # Count of friendly elements
        count = 1
        # Directions: up, down, left, right
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Check if the neighboring element has the same value and is not visited
            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and matrix[new_row][new_col] == matrix[row][col]:
                count += dfs(new_row, new_col, visited)
        
        return count
    
    # Main loop to start DFS from each cell
    for i in range(rows):
        for j in range(cols):
            if friendly_count[i][j] == 0:  # If not already counted
                visited = [[False for _ in range(cols)] for _ in range(rows)]
                friendly_count[i][j] = dfs(i, j, visited) - 1  # Exclude the element itself
    
    return friendly_count

with open('input.txt', 'r') as file:
    matrix = [list(map(int, line.split())) for line in file]
print(count_friendly_elements(matrix))