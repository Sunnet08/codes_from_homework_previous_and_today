class Mock:
    def __init__(self, obj, **attrs):
        self.obj = obj
        self.new_attrs = attrs
        self.old_attrs = {}
    
    def __enter__(self):
        for attr_name in self.new_attrs:
            if hasattr(self.obj, attr_name):
                self.old_attrs[attr_name] = getattr(self.obj, attr_name)
            setattr(self.obj, attr_name, self.new_attrs[attr_name])
        return self.obj
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        for attr_name in self.new_attrs:
            if attr_name in self.old_attrs:
                setattr(self.obj, attr_name, self.old_attrs[attr_name])
            else:
                delattr(self.obj, attr_name)

class TestClass:
    def __init__(self):
        self.name = "original_name"
        self.value = 100
        self.status = "active"
    
    def show(self):
        print(f"name: {self.name}, value: {self.value}, status: {self.status}")

obj = TestClass()

print("Before mock:")
obj.show()

with Mock(obj, name="mocked_name", value=999, new_attr="hello"):
    print("\nDuring mock:")
    obj.show()
    print(f"new_attr: {obj.new_attr}")

print("\nAfter mock:")
obj.show()
print(f"has new_attr: {hasattr(obj, 'new_attr')}")