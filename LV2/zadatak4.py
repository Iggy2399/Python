import numpy as np
import matplotlib.pyplot as plt

def generate_board(square_size, num_squares_height, num_squares_width):
    red_square = np.ones((square_size, square_size, 3), dtype=np.uint8) * [255, 0, 0]
    blue_square = np.ones((square_size, square_size, 3), dtype=np.uint8) * [0, 0, 255]
   
    row1 = np.hstack([red_square, blue_square] * (num_squares_width // 2))
    row2 = np.hstack([blue_square, red_square] * (num_squares_width // 2))
    checkerboard = np.vstack([row1, row2] * (num_squares_height // 2))
   
   
    if num_squares_height % 2 == 1:
        last_row = np.hstack([red_square, blue_square] * (num_squares_width // 2))
        checkerboard = np.vstack([checkerboard, last_row])
    if num_squares_width % 2 == 1:
        last_column = np.vstack([red_square, blue_square] * (num_squares_height // 2))
        checkerboard = np.hstack([checkerboard, last_column])
       
    return checkerboard


img = generate_board(50, 4, 5)
plt.imshow(img)
plt.show()
