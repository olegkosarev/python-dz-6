class Worker:
	def __init__(self, name, surname, position, wage, bonus):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
	def get_full_name(self):
		return(f"{self.name} {self.surname} {self.position}")

	def get_total_income(self):
		return(int(self._income.get("wage"))+int(self._income.get("bonus")))


w = Position("john","smith","engineer",100,20)

print(w.get_full_name())
print(w.get_total_income())

