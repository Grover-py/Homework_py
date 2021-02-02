class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return f'{self.name} - поехала'

    def stop(self):
        return f'{self.name} - остановилась'

    def turn(self, direction):
        return f'{self.name} - повернула, направление поворота: {direction}'

    def show_speed(self):
        return f'Текущая скорость: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Превышает скорость'
        else:
            return 'Скорость в норме'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'Превышает скорость'
        else:
            return 'Скорость в норме'

class PoliceCar(Car):
    pass

work_car = WorkCar(100, 'black', 'camry', 0)
print(work_car.name, work_car.color, work_car.is_police, work_car.show_speed())

town_car = TownCar(10, 'green', 'audi', 0)
print(town_car.name, town_car.color, town_car.is_police, town_car.show_speed())

sport_car = SportCar(100, 'blue', 'bmw', 0)
print(sport_car.name, sport_car.color, sport_car.is_police, sport_car.show_speed())

police_car = PoliceCar(90, 'hard blue', 'ford', 1)
print(police_car.name, police_car.color, police_car.is_police, police_car.show_speed())