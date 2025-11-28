class SimpleCache:
    def __init__(self, filename='cache.txt'):
        self.filename = filename
        self.cache = {}
    
    def __enter__(self):
        # try to read old casche
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    if '=' in line:
                        key, value = line.strip().split('=')
                        self.cache[key] = value
            print(f"Old cache: {len(self.cache)} notes")
        except:
            print("Couldnt read old cache")
            self.cache = {}
        
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
       
        with open(self.filename, 'w') as f:
            for key, value in self.cache.items():
                f.write(f"{key}={value}\n")
        print(f"Saved cache : {len(self.cache)} notes")
    
    def get_value(self, key):

        if key in self.cache:
            print(f"Found in cache : {key} -> {self.cache[key]}")
            return self.cache[key]
        else:
            print(f"Not in cache: {key}")
            return None
    
    def save_value(self, key, value):
        self.cache[key] = str(value)
        print(f"Saved: {key} -> {value}")


print("First time")
with SimpleCache() as cache:

    result1 = cache.get_value('площадь_круга_5')
    result2 = cache.get_value('площадь_круга_10')

    if result1 is None:
        area = 3.14 * 5 * 5
        cache.save_value('площадь_круга_5', area)
    
    if result2 is None:
        area = 3.14 * 10 * 10
        cache.save_value('площадь_круга_10', area)

print("\n Second time")
with SimpleCache() as cache:
    # Теперь берем из кэша
    result1 = cache.get_value('площадь_круга_5')
    result2 = cache.get_value('площадь_круга_10')
    

    result3 = cache.get_value('площадь_круга_15')
    if result3 is None:
        area = 3.14 * 15 * 15
        cache.save_value('площадь_круга_15', area)