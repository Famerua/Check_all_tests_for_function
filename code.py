class Matrix:
    def __init__(self, rows, cols, value=0, matrix=None):
        self.rows = rows
        self.cols = cols
        self.value = value
        if matrix is None:
            self.martrix = [[value]*cols for _ in range(rows)]
        else:
            self.martrix = matrix

    def get_value(self, rows, cols):
        return self.martrix[rows][cols]

    def set_value(self, rows, cols, value):
        self.martrix[rows][cols] = value

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __str__(self):
        return '\n'.join([' '.join(map(str, i)) for i in self.martrix])

    def __pos__(self):
        return Matrix(*self.__dict__.values())

    def __neg__(self):
        return Matrix(self.rows, self.cols, matrix=[[-i for i in j]for j in self.martrix])

    def __invert__(self):
        return Matrix(self.cols, self.rows, matrix=[i for i in zip(*self.martrix)])

    def __round__(self, n=None):
        return Matrix(self.rows, self.cols, matrix=[[round(i, n) for i in j]for j in self.martrix])
