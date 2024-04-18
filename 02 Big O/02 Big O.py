# This O(n)
def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

    return None

# This O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    return None

# This is O(n) -> constant time
# The most efficient Big O
def add_items(n):
    return n + n 





if __name__ == "__main__":
    print_items(5)