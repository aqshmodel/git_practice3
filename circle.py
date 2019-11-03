'''
課題1
動くようにクラスを設計
円の面積を計算するメソッド.areaが必要
円の円周長を計算するメソッド.perimeterが必要

'''


class Circle:

    def __init__(self, radius):
        self.radius = radius
    def area(self):
        pi = 3.14
        return self.radius ** 2 * pi

    def perimeter(self):
        pi = 3.14
        return self.radius * 2 * pi


# 半径1の円
circle1 = Circle(radius=1)
print('半径1の円')
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle1 = Circle(radius=3)
print('半径3の円')
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28