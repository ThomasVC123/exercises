class BMICalculator:
    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height
    
    @property
    def bmi(self):
        return self.__weight / self.__height**2

    @property
    def category(self):
        bmi = BMICalculator.bmi
        if bmi < 18.5:
            return "underweight"
        elif bmi < 25:
            return "normal"
        else:
            return "overweight"
