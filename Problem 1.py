""" Problem 1: Create a Python class called Circle with constructor which will
               take a list as an argument for the task. The list is [10,501,22,37,100,999,87,351].
    Problem 2: Create proper member variable inside the task if required and use
               them when necessary. For example for this task create a class
               private variable named pi=3.141
    Problem 3: From the list create two class methods Area and Perimeter which will be going
               to calculate the area and perimeter."""


# Created a class 'Circle'
class Circle:
    # Constructor with list as an argument
    def __init__(self,listn):
        self.listn=listn
        print(listn)

        # Private variable
        self.__pi=3.141

    # Method for calculating the Area for the values in the list
    def AreaOfCircle(self):
        # Iterate through the list to calculate the area
        for i in self.listn:
            area= self.__pi*i*i
            print("The area of ",i,":",area)

    # Method for calculating the Perimeter for the values in the list
    def PerimeterOfCircle(self):
        for i in self.listn:
            perimeter= 2*self.__pi*i
            print("The perimeter of ",i,":",perimeter)

# Created an object for the class Circle with list as a parameter
obj= Circle([10,501,22,37,100,999,87,351])

# Using object to access the class methods
obj.AreaOfCircle()
obj.PerimeterOfCircle()