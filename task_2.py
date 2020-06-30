
from sys import argv

_, _length, _width, mass_metr_kv, thickness = argv


class Road:

	def __init__(self,length,width,mass_metr_kv,thickness):
		self._length = length
		self._width = width
		self.mass_metr_kv = mass_metr_kv
		self.thickness = thickness

	def mass(self):
		return(int(_length)*int(_width)*int(mass_metr_kv)*int(thickness))

r = Road(_length, _width, mass_metr_kv, thickness)
print(r.mass())
