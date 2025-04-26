from stack import Stack



def move_items(n):
    source_stack = Stack(*list(range(n))[::-1])
    stacks = [Stack() for _ in range(n - 2)]
    final_stack = Stack()
    tries = n * 3

    def log():
        print("source_stack:", source_stack)
        print("stacks:", stacks)
        print("final_stack:", final_stack)

    def get_from_source():
        if source_stack.empty():
            return False
        
        el = source_stack.peek()

        if(0 == sum(len(stack) for stack in stacks)):
            for stack in stacks:
                if(final_stack.empty() or final_stack.peek() > el):
                    final_stack.push(el)
                    source_stack.pop()
                    return True

        for stack in stacks:
            if(stack.empty() or stack.peek() > el):
                stack.push(el)
                source_stack.pop()
                return True
            
        for stack in stacks:
            if(final_stack.empty() or final_stack.peek() > el):
                final_stack.push(el)
                source_stack.pop()
                return True
            
        return False
    
    def get_from_stack():
        for stack in stacks:
            if(not stack.empty()):
                el = stack.peek()
                if source_stack.empty():
                    source_stack.push(stack.pop())
    
        for stack in reversed(stacks):
            if(not stack.empty()):
                el = stack.peek()
                if(final_stack.empty() or final_stack.peek() > el):
                    final_stack.push(stack.pop())
                    return True
        return False

    def get_from_final():
        if(not final_stack.empty()):
            el = final_stack.peek()
            for stack in stacks:
                if(stack.empty() or stack.peek() > el):
                    stack.push(final_stack.pop())
                    return True
            if(source_stack.empty() or source_stack.peek() > el):
                source_stack.push(final_stack.pop())
                return True

    while not len(final_stack) == n and tries > 1:
        log()

        if not get_from_source():
            if not get_from_stack():
                get_from_final()
            tries -= 1

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
        if n < 0:
            print("Value too small")
            continue

        move_items(n)

    print("Exiting...")


