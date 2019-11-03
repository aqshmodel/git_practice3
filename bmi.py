'''
class (成人の)BMI:
    関連しそうな属性:
        - 身長
        - 体重
        - BMIという値そのもの
    ルール:
        - BMI 10以上40以下 <-- 常識的な範囲
        - 表示するときは、小数点第2位まで
            - ex: 23.678 -> 23.67
            - ex: 23.671 -> 23.67
    できること:
        - ???
'''

# クラス名はUpperCamelCaseが普通
class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def culculate_bmi(self):
        return self.weight / (self.height ** 2)


# BMIのクラスのインスタンス化
hibiki_bmi = BMI(height=1.80, weight=67.0)
print('Hibiki')
print(hibiki_bmi.height, hibiki_bmi.weight)
print(hibiki_bmi.culculate_bmi())

noriya_bmi = BMI(height=1.78, weight=75.0)
print('Ohira')
print(noriya_bmi.height, noriya_bmi.weight)
print(noriya_bmi.culculate_bmi())