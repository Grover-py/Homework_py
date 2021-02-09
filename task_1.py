
class Matrix():
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for el in self.my_list:
            s = ''
            for i in el:
                s = f'{str(s)}   {str(i)}'
            print(s)
        return ''

    def __add__(self, other):
        for el in range(len(self.my_list)):
            for i in range(len(other.my_list[el])):
                self.my_list[el][i] = self.my_list[el][i] + other.my_list[el][i]
        return Matrix.__str__(self)


matrix = Matrix([[1, 2, 3, 7], [2, 5, 7, 1], [7, 6, 8, 4]])
print(matrix)
matrix_2 = Matrix([[4, 1, 5, 2], [1, 2, 1, 7], [15, 4, -8, 0]])
print(matrix.__add__(matrix_2))