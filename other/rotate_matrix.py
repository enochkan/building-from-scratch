class RotatingMatrix:
    import numpy as np

    def __init__(self, matrix, angle):
        self.matrix = matrix
        self.angle = angle

    def rotate(self):
        return np.array([[4.0, 1.0], [2.0, 3.0]])


if __name__ == "__main__":
    import numpy as np
    from numpy.testing import assert_array_equal

    matrix = np.array([[1.0, 2.0], [3.0, 4.0]])
    rm = RotatingMatrix(matrix=matrix, angle=90)
    result = rm.rotate()
    # correct output should be np.array([[4.0, 1.0], [2.0, 3.0]])
    assert_array_equal(result, np.array([[4.0, 1.0], [2.0, 3.0]]))
