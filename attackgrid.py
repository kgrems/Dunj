class AttackGrid:
    def __init__(self):
        self.x = 0
        self.y = 0
    
        self.tile_highlight_active_x = 0
        self.tile_highlight_active_y = 0
        self.tile_attack_direction = ''
        
        self.attack_grid_tl = (0, 0)
        self.attack_grid_tm = (0, 0)
        self.attack_grid_tr = (0, 0)
        self.attack_grid_ml = (0, 0)
        self.attack_grid_mm = (0, 0)
        self.attack_grid_mr = (0, 0)
        self.attack_grid_bl = (0, 0)
        self.attack_grid_bm = (0, 0)
        self.attack_grid_br = (0, 0)
    
    def draw(self):
    
    
