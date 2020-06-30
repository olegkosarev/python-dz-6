class Stationery:
	def __init__(self,title):
		self.title = title

	def draw(self):
		print("Запуск отрисовки")


class Pen(Stationery):
	def draw(self):
		print("Запуск отрисовки ручкой")

class Pencil(Stationery):
	def draw(self):
		print("Запуск отрисовки карандашом")

class Handle(Stationery):
	def draw(self):
		print("Используем ластик")

s = Stationery("")
s.draw()

pen = Pen("")
pen.draw()

pencil = Pencil("")
pencil.draw()

