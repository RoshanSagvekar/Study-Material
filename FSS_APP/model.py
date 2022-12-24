# It is a Food model which represent food details.
class Food:
    def __init__(self,foodid=0,foodName='',foodType='',foodPrice=0.0):
        self.foodid=foodid
        self.foodName=foodName
        self.foodType=foodType
        self.foodPrice=foodPrice
    
    def __repr__(self):
        return f'Food[{self.foodid},{self.foodName},{self.foodType},{self.foodPrice}]'