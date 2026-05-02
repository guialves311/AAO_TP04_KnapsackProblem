#Eliminar depois
class Item:
    def __init__(self, id, value, weight):
        self.id = id
        self.value = value
        self.weight = weight
        self.density = value / weight
        self.relaxed_value = 0.0
        self.selected = false
