class Deque:
    def __init__(self):
        self.items = []

    def push_front(self, x):
        self.items.insert(0, x)

    def push_back(self, x):
        self.items.append(x)

    def pop_front(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def pop_back(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek_front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def peek_back(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def swap_first_last(self):
        if len(self.items) >= 2:
            self.items[0], self.items[-1] = self.items[-1], self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def reverse(self):
        self.items.reverse()

    def contains(self, x):
        return x in self.items

    def clear(self):
        self.items.clear()

    def show(self):
        print("Deque:", self.items if self.items else "[] (empty)")
        if not self.is_empty():
            print(f"   front → {self.items[0]}    back → {self.items[-1]}")
        print()

d = Deque()

print("Double-Ended Queue (Deque) — Interactive Demo\n")

while True:
    d.show()
    print("Menu:")
    print("1  — Add element to front")
    print("2  — Add element to back")
    print("3  — Remove from front")
    print("4  — Remove from back")
    print("5  — View front element")
    print("6  — View back element")
    print("7  — Swap first and last elements")
    print("8  — Reverse the deque")
    print("9  — Check if element exists")
    print("10 — Clear deque")
    print("0  — Exit")
    print("-" * 40)

    choice = input("Enter operation (0-10): ").strip()

    if choice == "1":
        try:
            x = int(input("Enter number: "))
            d.push_front(x)
            print(f"Added {x} to front")
        except ValueError:
            print("Error! Please enter an integer.")

    elif choice == "2":
        try:
            x = int(input("Enter number: "))
            d.push_back(x)
            print(f"Added {x} to back")
        except ValueError:
            print("Error! Please enter an integer.")

    elif choice == "3":
        val = d.pop_front()
        if val is not None:
            print(f"Removed from front: {val}")
        else:
            print("Deque is empty!")

    elif choice == "4":
        val = d.pop_back()
        if val is not None:
            print(f"Removed from back: {val}")
        else:
            print("Deque is empty!")

    elif choice == "5":
        val = d.peek_front()
        if val is not None:
            print(f"Front element: {val}")
        else:
            print("Deque is empty!")

    elif choice == "6":
        val = d.peek_back()
        if val is not None:
            print(f"Back element: {val}")
        else:
            print("Deque is empty!")

    elif choice == "7":
        if d.size() < 2:
            print("Not enough elements to swap!")
        else:
            d.swap_first_last()
            print("First and last elements swapped")

    elif choice == "8":
        d.reverse()
        print("Deque reversed")

    elif choice == "9":
        try:
            x = int(input("Search for number: "))
            if d.contains(x):
                print(f"Yes, {x} is in the deque")
            else:
                print(f"No, {x} is not in the deque")
        except ValueError:
            print("Please enter a number!")

    elif choice == "10":
        d.clear()
        print("Deque cleared")

    elif choice == "0":
        print("Goodbye! Thanks for using the Deque")
        break

    else:
        print("Invalid choice! Please enter a number from 0 to 10")

    print("\n" + "="*60 + "\n")
