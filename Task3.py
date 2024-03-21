class Person:
    def __init__(self, weight, height):
        if weight <= 0 or height <= 0:
            raise ValueError("Berat badan dan tinggi badan harus berupa angka positif.")
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        return round(self.weight / (self.height ** 2), 2)
    
person = Person(70, 1.80)
print(f"{person.BMI_Value()}")  # Output: 21.6