""" Problem 2: Inheritance
               https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md"""

# Base class
class TV:

    # Constructor with brand, price and inches as parameters
    def __init__(self,brand,price,inches):
        self.brand = brand
        self.price = price
        self.inches = inches
        # Default value of Volume and Channel
        self.volume = 50
        print("Volume by default:", self.volume)
        self.channel = 1
        print("Default Channel:", self.channel)

        # TV is OFF by default
        self.on = False

    # Method to increase/decrease TV volume with new_volume parameter
    def IncreaseOrDecreaseVol(self, new_volume):
        # Condition to check TV is ON or OFF
        if self.on:
            print("TV is Off")
        else:
            self.new_volume = new_volume

            # Checking if the volume is between 0-100, if it is not in range then the volume will be default/current volume
            if self.new_volume < 0 or self.new_volume > 100:
                volume = self.volume
                print("Volume=", self.volume)
            # If the volume is in the range, new volume
            else:
                self.volume = self.new_volume
                print("Volume=", self.new_volume)

   # Method to change Channel with new_channel parameter
    def SetChannel(self,new_channel):
        # Condition to check TV is ON or OFF
        if self.on:
            print("TV is Off")
        else:
            self.new_channel = new_channel

            # Condition to check the Channel is more than 50, if it is then it stays at current channel.
            if self.new_channel > 50:
                channel = self.channel
                print("Current Channel:", self.channel)
            # Else new channel
            else:
                self.channel = self.new_channel
                print("Current channel:", self.channel)

    # A method to reset TV, by creating a new object inside the class method to call the constructor.
    def ResetTv(self):
        new_obj = TV("intel",50000,5)

    # Status method to return current info of the TV status
    def status(self):
        return f"TV Status: {self.brand} at Channel {self.channel} ,Volume {self.volume}"


# Creating an object for TV class
obj=TV("Intel",50000,5)

# Accessing class methods using object
obj.IncreaseOrDecreaseVol(45)
obj.SetChannel(22)
# Prints the current status after changing the value
print(obj.status())

obj.IncreaseOrDecreaseVol(65)
print(obj.status())

obj.ResetTv()
print(obj.status())

# LedTv class(child) inherits TV class(base)
class LedTv(TV):
    # Constructor with additional properties
    def __init__(self, brand, price, inches, energy_usage, lifespan, refresh_rate):
        # Allows to call functions in the base class
        super().__init__(brand, price, inches)

        # Screen is thinner than Plasma
        self.screen_thickness = "Thinner than Plasma"
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0
        self.backlight = False

    # Method to set viewing angle
    def SetViewingAngle(self, angle):
        # Condition to check it's between 0-180
        if angle < 0 or angle > 180:
            print("Invalid viewing angle. It must be between 0 and 180 degrees.")
        else:
            self.viewing_angle = angle

    # Method to set backlight to ON/OFF
    def SetBacklight(self):
        self.backlight = not self.backlight

    # Method to display all the properties of the TV, including those added in LedTv
    def DisplayDetails(self):
        details = ("\n--- Details of LED TV--- \n"
            f"Brand: {self.brand}\n"
            f"Price: Rs.{self.price}\n"
            f"Inches of TV: {self.inches}\" \n"
            f"Channel: {self.channel}\n"
            f"Volume: {self.volume}\n"
            f"Screen Thickness: {self.screen_thickness} \n"
            f"Energy Usage: {self.energy_usage} W\n"
            f"Lifespan: {self.lifespan} hours\n"
            f"Refresh Rate: {self.refresh_rate} Hz\n"
            f"Viewing Angle: {self.viewing_angle} degrees\n"
            f"Backlight: {'On' if self.backlight else 'Off'}")
        return details



# PlasmaTv class(child) inherits TV class(base)
class PlasmaTv(TV):
    # Constructor with additional properties
    def __init__(self, brand,price,inches, energy_usage, lifespan, refresh_rate):
        # Allows to call functions in the base class
        super().__init__(brand,price,inches)

        # Screen is thicker than LED
        self.screen_thickness = "Thick"
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0
        self.backlight = "No Backlight"

    # Method to set viewing angle
    def SetViewingAngle(self, angle):
        # Condition to check it's between 0-180
        if angle<0 or angle>180:
            print("Invalid viewing angle. It must be between 0 and 180 degrees.")
        else:
            self.viewing_angle = angle

    # Method to display all the properties of the TV, including those added in PlasmaTv
    def DisplayDetails(self):
        details = ("\n---Details of PLASMA TV---\n"
            f"Brand: {self.brand}\n"
            f"Price: Rs.{self.price}\n"
            f"Inches of TV: {self.inches}\" \n"
            f"Channel: {self.channel}\n"
            f"Volume: {self.volume}\n"
            f"Screen Thickness: {self.screen_thickness} \n"
            f"Energy Usage: {self.energy_usage} W\n"
            f"Lifespan: {self.lifespan} hours\n"
            f"Refresh Rate: {self.refresh_rate} Hz\n"
            f"Viewing Angle: {self.viewing_angle} degrees\n"
            f"Backlight: { self.backlight}")
        return details

# Object created for child class 'LedTv'
led_obj=LedTv("Sony",50000,42,120,100000,240)

# Access Base class methods using child class object
led_obj.IncreaseOrDecreaseVol(86)
print(led_obj.status())

# Accessing class methods using object
led_obj.SetViewingAngle(45)
led_obj.SetBacklight()
print(led_obj.DisplayDetails())


# Object created for child class 'PlasmaTv'
plasma_obj=PlasmaTv("Panasonic Plasma",35000,32,120,60000,550)
# Access Base class methods using child class object
plasma_obj.SetChannel(22)

plasma_obj.SetViewingAngle(55)
print(plasma_obj.DisplayDetails())


""" The difference between the LED and PLSAMA TV are the screen thickness & backlight"""