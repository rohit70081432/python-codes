class Example:
    def greet(self, **kwargs):
        name = kwargs.get('name')
        age = kwargs.get('age')
        if age:
            print(f"Hello, {name}. You are {age} years old.")
        else:
            print(f"Hello, {name}")