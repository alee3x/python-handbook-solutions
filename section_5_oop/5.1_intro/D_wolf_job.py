class Programmer:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        if self.position == "Junior":
            self.payout = 10
        elif self.position == "Middle":
            self.payout = 15
        elif self.position == "Senior":
            self.payout = 20
        self.raises = 0
        self.work_time = 0
        self.salary = 0

    def work(self, time):
        self.work_time += time
        self.salary += time * self.payout

    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
            self.payout = 15
        elif self.position == "Middle":
            self.position = "Senior"
            self.payout = 20
        elif self.position == "Senior":
            self.raises += 1
            self.payout = 20 + self.raises

    def info(self):
        return f"{self.name} {self.work_time}ч. {self.salary}тгр."


programmer = Programmer("Васильев Иван", "Junior")
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
