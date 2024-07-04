


class Car():
    def __init__(self,name: str, year: int, speed: float, consumption: float, tank_size: float) -> None:
        self.name = name
        self.year = year
        self.sign = None
        self.speed = speed
        self.consumption = consumption
        self.tank_size = tank_size
        self.litr = 0 

        """
        Fields:
        -------
            Public:
                name (str):             [Name of vehicle]
                year (int):             [Year of production]
                speed (float):          [Vehicle average speed]
                consumption (float):    [Fuel consumption on 100 km (litres)]
                tank_size (float):      [Vehicle tank size (litres)]
            Private:
                __fuel__ (float):       [Current fuel amount]
                __sign__ (str):         [Registration Sign]
        """


    def calculate_time(self, distance: float) -> float:
        """Calculate time needed to travel distance.

        Parameters:
        -----------
            distance (float):           [Distance wished to travel]

        Returns:
        --------
            float:                      [Time needed to travel that distance]
        """
        return distance/self.speed
    


    def register(self, new_sign_number: str) -> bool:
        """Check if new sign is valid and register it if yes.

        Validation means, the first two chars of new sign must be digits,
        followed by two uppercase letters and 3 digits.
        Also, if car is already registered, return False and do not
        change anything.

        Parameters:
        -----------
            new_sign_number (str):      [New sign number]

        Returns:
        --------
            bool:                       [Registered or not]
        """
        stringnumber = new_sign_number
        if self.sign is None:
            new_sign_number = list(new_sign_number)
            firsstep = new_sign_number[0:2:1]
            secondstep = new_sign_number[2:4:1]
            therdstep = new_sign_number[4::1]
            for i in firsstep:
                if i.isdigit():
                    firstTrue = True
                else:
                    firstTrue = False
            for j in secondstep:
                if j.isupper():
                    secondTrue = True
                else:
                    secondTrue = False
            for k in therdstep:
                if k.isdigit():
                    therdTrue = True
                else:
                    therdTrue = False
            if firstTrue and secondTrue and therdTrue:
                self.sign = stringnumber
                return True
            else:
                return False

    def fill(self, fuel_amount: float) -> None:
        """Fill car tank with the amount specified.

        Fill car tank, but do not exceed the tank's capacity.


        Parameters:
        ----------
            fuel_amount (float):        [Amount needed to be filled]
        """
        if fuel_amount < self.tank_size - self.litr:
            self.litr += fuel_amount
            print("Your petrol: ",self.litr,"litr")
        elif fuel_amount > (self.tank_size - self.litr):
            self.litr = self.tank_size
            print("Your petrol: ",self.litr, "litr")


    def go(self, distance: float) -> bool:
        """Travel providen distance

        Calculate the fuel amount needed to be spent on the distance.
        If there is enough fuel, calculate how much fuel is left after distance,
        write the result in car's fuel amount field and return True.
        If there isn't enough fuel, return False.

        Parameters:
        -----------
            distance (float):           [Distance wished to travel]

        Returns:
        --------
            bool:                      [Traveled or not]
        """
        required_petrol = distance * (self.consumption / 100)
        if required_petrol >= self.litr:
            how_need_add = (required_petrol - self.litr)
            print(False)
            print("You need: ", how_need_add, "litr")
        else:
            self.litr = self.litr - required_petrol
            print(True)

    def get_sign(self) -> str:
        """Return car registration sign."""
        return self.sign


    def get_fuel(self) -> float:
        """Return left fuel amount."""
        return self.litr


    def max_distance_can_travel(self) -> float:
        """Return max distance car can travel with current fuel amount"""
        return self.litr/self.consumption


# Write an example for usage of your Car class.

my_car = Car("Mustang",
             2024,
             100,
             20,
             80
             )

print(my_car.calculate_time(150))
print(my_car.register('34YT827'))
my_car.fill(50)
my_car.fill(10)
my_car.go(20)
print(my_car.get_sign())
print(my_car.get_fuel())
print(my_car.max_distance_can_travel())