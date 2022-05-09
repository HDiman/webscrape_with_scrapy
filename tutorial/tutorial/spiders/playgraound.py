
# list_items = [i for i in range(100)]
# print(list_items)


def outer_function():
    print("Outer")

    def nested_function():
        print("Inner")

    return nested_function

inner_function = outer_function()
inner_function()

