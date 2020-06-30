from time import sleep

class TrafficLight:
	__color = None

	def running(self):
		print('red')
		sleep(7)
		print('yellow')
		sleep(2)
		print('green')
		sleep(3)


t = TrafficLight()
t.running()

