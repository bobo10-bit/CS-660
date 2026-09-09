def example_1():
    x = "outer"
    
    def inner(value):
        #Simulate a dynamic scope by using the value passed to the inner function
        print(f"Inner sees: {value}")
    
    inner(x)
    print(f"Outer has: {x}")

def example_2():
    x = 10
    
    def middle():
        x = 20
        
        # Simulate dynamic scoping by passing the current x value to the inner function.
        def inner(value):
            print(f"Inner sees: {value}")
        
        inner(x)
        print(f"Middle has: {x}")
    
    middle()
    print(f"Outer has: {x}")

def example_3():
    # Changed the count back to an int from a string to fix the mismatch
    count = 0
    
    def increment(value):
        # Removed nonlocal count so the function uses the value passed into it instead of the outer variable.
        value += 1
        return value
    
    def get_counter(value):
         # Pass the value from the caller instead of using the enclosing scope.
        def counter():
            return increment(value)
        return counter
    # pass count into the function to simulate a dynamic scope lookup.
    my_counter = get_counter(count)
    print(my_counter())
    print(my_counter())
    print(count)

def example_4():
    name = "global"
    
    def outer(name):
        name = "outer"
        
        def inner(value):
            #simulate dynamic scoping by passing the outer name value to the inner function.
            # name = "inner"
            print(f"Inner: {value}")
        
        # pass the outer variable into the inner function instead of using the local scope.
        inner(name)
        print(f"Outer: {name}")
    
    # pass the global name into the outer function.
    outer(name)
    print(f"Global: {name}")

if __name__ == "__main__":
    print("Example 1:")
    example_1()
    
    print("\nExample 2:")
    example_2()
    
    print("\nExample 3:")
    example_3()
    
    print("\nExample 4:")
    example_4()