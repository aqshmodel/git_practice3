'''
課題2
長方形の面積を計算するメソッド、areaが必要
長方形の対角線の長さを計算するメソッド、diagonalが必要
'''

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width

    def diagonal(self):
        import math
        return math.sprt((self.height ** 2) + (self.width ** 2))


# height5、width6の長方形
rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
rectangle1.diagonal()  # 7.81

# height3、width3の長方形
rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
#rectangle2.diagonal()  # 4.24