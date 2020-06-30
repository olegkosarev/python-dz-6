class Car:
	def __init__ (self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police
		self.direction = direction

	def go(self):
		print(f"{self.name} поехала")

	def stop(self):
		print(f"{self.name} остановилась")

	def turn(self):
		print(f"{self.name} повернула {self.direction}")

	def show_speed(self):
		if self.name == "TownCar" and self.speed > 60 or self.name == "WorkCar" and self.speed > 40:
			print(f"превышение скорости! текущая скорость {self.speed}")
		else:
			print(self.speed)


class TownCar(Car):
	def __init__ (self, speed, color):
		self.speed = speed
		self.color = color
		self.name = "TownCar"
		self.is_police = False

class SportCar(Car):
	def __init__ (self, speed, color):
		self.speed = speed
		self.color = color
		self.name = "SportCar"
		self.is_police = False

class WorkCar(Car):
	def __init__ (self, speed, color):
		self.speed = speed
		self.color = color
		self.name = "WorkCar"
		self.is_police = False

class PoliceCar(Car):
	def __init__ (self, speed, direction):
		self.speed = speed
		self.color = "balck and white"
		self.name = "PoliceCar"
		self.is_police = True		
		self.direction = direction				


tc = TownCar(70,"blue")
tc.show_speed()

sc = SportCar(120,"red")
sc.go()
		

wc = WorkCar(120,"red")
wc.stop()

pc = PoliceCar(60,"направо")
pc.turn()

