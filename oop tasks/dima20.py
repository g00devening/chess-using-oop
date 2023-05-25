class SparseArray:
    def __init__(self):
        self.values = dict()
        self.keys = []

    def __setitem__(self, key, v):
        self.values[key] = v
        self.keys.append(key)

    def __getitem__(self, key):
        if key in self.keys:
            return self.values[key]
        else:
            return 0
        

    
        
