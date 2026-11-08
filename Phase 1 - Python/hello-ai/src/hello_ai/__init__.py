
print("top-level line runs, __name__ =", __name__)
def greet(name: str) -> str:
    return f"Hello, {name}!"


def main():
    print(greet("Alex"))
    for i in range(1, 4):
        print(f"Lesson {i}: Welcome to the AI course!")

if __name__ == '__main__':
    main()