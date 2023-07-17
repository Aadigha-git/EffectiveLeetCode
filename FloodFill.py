def floodFill(image, sr, sc, color):
    if not (0 <= sr < len(image)) or not (0 <= sc < len(image[0])) or image[sr][sc] == color:
        return image

    # Get the old color at the starting position
    oldColor = image[sr][sc]

    # Recursive helper function to perform flood fill
    def dfs(row, col):
        # Check if the current position is out of bounds or has a different color
        if not (0 <= row < len(image)) or not (0 <= col < len(image[0])) or image[row][col] != oldColor:
            return

        # Change the color of the current position
        image[row][col] = color

        # Recursively flood fill the neighboring positions
        dfs(row - 1, col)  # Up
        dfs(row + 1, col)  # Down
        dfs(row, col - 1)  # Left
        dfs(row, col + 1)  # Right

    # Start the flood fill from the starting position
    dfs(sr, sc)

    return image

image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr, sc = 1, 1
newColor = 2

filled_image = floodFill(image, sr, sc, newColor)
print(filled_image)

"""
Question9:

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.
"""