from stack import Stack

def move_items(n, source_stack, medium_stack, final_stack):

    def log():
        print("source_stack:", source_stack)
        print("medium_stack:", medium_stack)
        print("final_stack:", final_stack)
        print()

    if n == 1:
        final_stack.push(source_stack.pop())
        log()
    else:
        move_items(n-1, source_stack, final_stack, medium_stack)
        final_stack.push(source_stack.pop())
        move_items(n-1, medium_stack, source_stack, final_stack)
        log()

if __name__ == "__main__":

    while True:

        user_input = input("\nEnter a disc amount or 'q' to quit: ").strip()

        if user_input.lower() == "q":
            print("Exit by user command.")
            break

        try:
            n = int(user_input)

        except ValueError:
            print("Please enter an integer value.")
            continue

        if n < 1:
            print("Value too small")
            continue

        source_stack = Stack(*list(range(n, 0, -1)))
        medium_stack = Stack()
        final_stack = Stack()

        move_items(n, source_stack, medium_stack, final_stack)

    print("Exiting...")
