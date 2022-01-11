class circle:
    def __init__(self,radius:int):
        self.radius=radius

    def area(self)->None:
        area=3.14*(self.radius**2)
        print(f'the area of the triangle with {self.radius} is : {area}')


if __name__== '__main__':
    print('this code is used to find area of a given circle')
    radius = int(input('enter the radius of the circle ->'))
    obj = circle(radius) #obj.init(side)
    obj.area()