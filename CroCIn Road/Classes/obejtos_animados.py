class Player:
    def __init__(self, size, width, height, x, y, speed):
        self._size = size
        self._width = width
        self._height = height
        self._x = x
        self._y = y
        self._speed = speed

class Car:
    cars = []
    
    def __init__(self, width, height, x, y, speed, spacing):
        self._width = width
        self._height = height
        self._x = x
        self._y = y
        self._speed = speed
        self._spacing = spacing