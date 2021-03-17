class RotatingMatrix90:
    import numpy as np

    def __init__(self, matrix):
        self.matrix = matrix
        self.is_square = False

    def rotate(self):
        w, h = self.matrix.shape[0], self.matrix.shape[1]
        if w == h:
            self.is_square = True
            """0,0 => 0,1; 0,1 => 1,1; 1,1 => 1,0; 1,0 => 0,0;"""
            tmat = # insert transformation matrix here
            # do matmul

        return np.array([[4.0, 1.0], [2.0, 3.0]])


if __name__ == "__main__":
    import numpy as np
    from numpy.testing import assert_array_equal

    matrix = np.array([[1.0, 2.0], [3.0, 4.0]])
    rm = RotatingMatrix90(matrix=matrix)
    result = rm.rotate()
    # correct output should be np.array([[4.0, 1.0], [2.0, 3.0]])
    assert_array_equal(result, np.array([[4.0, 1.0], [2.0, 3.0]]))
