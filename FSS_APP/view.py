from model import Food

foodlist=[]

foodlist.append(Food(1001,'Chicken Handi','Nonveg',500))
foodlist.append(Food(1002,'Veg Handi','Veg',400))


# Create
def save(fd):
    foodlist.append(fd)
    print('Food is Added Successfully.')

# Update 
def update(foodid,newfood):
    food=getFood(foodid)  #find which we want to update
    index=foodlist.index(food)    # index its index    
    foodlist[index].foodName=newfood.foodName   # replace with new value
    foodlist[index].foodType=newfood.foodType
    foodlist[index].foodPrice=newfood.foodPrice

# Delete
def delete(foodid):
    food=getFood(foodid)  #find which we want to update
    index=foodlist.index(food)
    foodlist.pop(index)

# Read All object
def getAll():
    return foodlist

# Read Single object
def getFood(foodId):
    l1=list(filter(lambda fd:fd.foodid==foodId,foodlist))
    if len(l1)==1:
        return l1[0]
    else:
        print('\tFood Not Found')

# Show Food by Name
def getfoodbyname(foodName):
    l1=list(filter(lambda fd:fd.foodName==foodName,foodlist))
    if len(l1)==1:
        return l1[0]
    else:
        print('\tFood Not Found')

# Show Food by Name
def getfoodbytype(foodType):
    l1=list(filter(lambda fd:fd.foodType==foodType,foodlist))
    if len(l1)>=1:
        return l1
    else:
        print('\tFood Not Found')

# Sort Food List by Name
def sortbyname():
    foodlist.sort(key=lambda fd:fd.foodName)
    return foodlist

# Sort Food List by Price
def sortbyprice():
    foodlist.sort(key=lambda fd:fd.foodPrice)
    return foodlist