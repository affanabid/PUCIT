# def pascalTriangle(n):
#     if n == 0:
#         return [0]
#     elif n == 1:
#         return [1]
#     else:
#         new_row = [1]
#         last_row = pascalTriangle(n-1)
#         for i in range(len(last_row)-1):
#             new_row.append(last_row[i] + last_row[i+1])
#         new_row += [1]
#     return new_row

# print(pascalTriangle(1))
def generate_pascals_triangle(rows):
    if rows == 0:
        return []
    elif rows == 1:
        return [[1]]
    else:
        triangle = generate_pascals_triangle(rows - 1)
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)
        return triangle

# Example usage
rows = 5
pascals_triangle = generate_pascals_triangle(rows)
for row in pascals_triangle:
    print(row)
