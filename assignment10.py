# Assigmnet 10
# Problem 1 solution :

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return 3.14 * self.radius * self.radius * self.height
    
    def surface_area(self):
        return 2 * 3.14 * self.radius * self.height + 2 * 3.14 * self.radius * self.radius
    
cy1 = Cylinder(radius = 5, height = 10)
print(cy1.volume())
print(cy1.surface_area())

# Problem 2 solution : 

class BankAccount:

    def __init__(self):
        self.balance = 0
        print("Opening account balance is 0")

    def diposite(self):
        amount = float(input("Enter amount to be diposite: "))
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdraw:", amount)
        else:
            print("Not enough balance in your account")

    def display_balance(self):
        print("Available balance is", self.balance)

print("Customer 1")
customer_1 = BankAccount()
print("Customer 2")
customer_2 = BankAccount()

print("For Customer 1")
customer_1.diposite()
customer_1.withdraw()
customer_1.display_balance()

print("For Customer 2")
customer_2.diposite()
customer_2.withdraw()
customer_2.display_balance()

# Problem 3 solution:

class Time:

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def DisplayTime(self):
        am_pm = "AM"
        hours = self.hours

        if self.hours >= 12:
            am_pm = "PM"
            hours = self.hours - 12

        if hours == 0:
            hours = 12

        if self.hours >= 24:
            print("The input hours should be less than 24")

        if self.minutes >= 60:
            print("The input minutes should be less than 60")

        print("{:02d}:{:02d} {}".format(hours, self.minutes, am_pm))

    def DisplayRatio(self):
        try:
            ratio = self.minutes / self.hours
            print("The ratio of minutes to hours is: {:.2f}".format(ratio))
        except:
            ratio = 0
            print("The ratio of minute to hours is not display")

hour_min_list = [(23,45), (34,50), (12,34), (14,67),(19,20), (2,15), (0, 10)]


for time in hour_min_list:
    t = Time(time[0], time[1])
    t.DisplayTime()
    t.DisplayRatio()