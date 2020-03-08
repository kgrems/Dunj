class Item:
    def __init__(self, x_pos, y_pos, name, image_path, visible, cost, data_symbol, inventory_thumb):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = name
        self.image_path = image_path
        self.visible = visible
        self.cost = cost
        self.data_symbol = data_symbol
        self.inventory_thumb = inventory_thumb
    
    def use(self, player):
        print(player.name + ' used and item!')
