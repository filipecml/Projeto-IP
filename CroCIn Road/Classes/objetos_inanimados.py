class Collectable:
    
    collectables = []
    
    def __init__(self, width, height, x, y, sprite):
        self._width = width
        self._height = height
        self._x = x
        self._y = y
        self._sprite = sprite