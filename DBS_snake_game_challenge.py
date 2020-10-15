class Node:
    def __init__(self, position):
        self.position = position
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = self.head

    def print_(self):
        p = self.head
        while p:
            print(p.position, end="")
            p = p.next

    def append_head(self, node):
        self.head.prev = node
        node.next = self.head
        self.head = node

    def remove_tail(self):
        self.tail = self.tail.prev
        self.tail.next = None
        
    def contain(self, node):
        p = self.head
        while p.next: # stop before tail, don't check tail
            if node.position == p.position: # eat itself
                return True
            p = p.next
        return False 
    
    
def main():
    m = int(input()) # number of command
    for i in range(m):
        y = input()
        y = y.split(' ')
        array = y[1]
        n = int(y[0])
        direction = 0 # 0 UP, 1 LEFT, 2 RIGHT, 3 DOWN
        x = 0
        y = 0
        head = Node([x,y])
        snake = LinkedList(head)
        alive = True
        step_num = 0
        for i in range(n):
            step = array[i]
            if step == 'F'or step == 'E': 
                if direction == 0 :
                    current_node = snake.head # snake head
                    new_node = Node([current_node.position[0] ,current_node.position[1] + 1]) # move up
                    direction = 0 # head direction
                    step_num += 1
                    
                    if snake.contain(new_node): # exclude tail
                        print(step_num)
                        alive = False
                        break
                    else:
                        snake.append_head(new_node) # update snake position
                        if step != 'E':  # if no eat apple, delete tail
                            snake.remove_tail()
                    
                elif direction == 1:
                    current_node = snake.head # snake head
                    new_node = Node([current_node.position[0] - 1,current_node.position[1]]) # move up
                    direction = 1 # head direction
                    step_num += 1
                    
                    if snake.contain(new_node): # exclude tail
                        print(step_num)
                        alive = False
                        break
                    else:
                        snake.append_head(new_node) # update snake position
                        if step != 'E':  # if no eat apple, delete tail
                            snake.remove_tail()
                    
                elif direction == 2:
                    current_node = snake.head # snake head
                    new_node = Node([current_node.position[0] + 1 ,current_node.position[1]]) # move up
                    direction = 2 # head direction
                    step_num += 1
                    
                    if snake.contain(new_node): # exclude tail
                        print(step_num)
                        alive = False
                        break
                    else:
                        snake.append_head(new_node) # update snake position
                        if step != 'E':  # if no eat apple, delete tail
                            snake.remove_tail()

                elif direction == 3: 
                    current_node = snake.head # snake head
                    new_node = Node([current_node.position[0] ,current_node.position[1] - 1]) # move up
                    direction = 3 # head direction
                    step_num += 1
                    
                    if snake.contain(new_node): # exclude tail
                        print(step_num)
                        alive = False
                        break
                    else:
                        snake.append_head(new_node) # update snake position
                        if step != 'E':  # if no eat apple, delete tail
                            snake.remove_tail()
                    
            elif step == 'L': 
                if direction == 0:
                    current_node = snake.head # snake head
                    new_node = Node([current_node.position[0] - 1 ,current_node.position[1]]) # move up
                    direction = 1 # head direction
                    step_num += 1
                    
                    if snake.contain(new_node): # exclude tail
                        print(step_num)
                        alive = False
                        break
                    else:
                        snake.append_head(new_node) # update snake position
                        snake.remove_tail()

                elif direction == 1:
                    current_node = snake.head # snake head
                    new_node = Node([current_node.position[0] ,current_node.position[1] - 1]) # move up
                    direction = 3 # head direction
                    step_num += 1
                    
                    if snake.contain(new_node): # exclude tail
                        print(step_num)
                        alive = False
                        break
                    else:
                        snake.append_head(new_node) # update snake position
                        snake.remove_tail()
    
                elif direction == 2:
                    current_node = snake.head # snake head
                    new_node = Node([current_node.position[0] ,current_node.position[1] + 1]) # move up
                    direction = 0 # head direction
                    step_num += 1
                    
                    if snake.contain(new_node): # exclude tail
                        print(step_num)
                        print(new_node.position)
                        alive = False
                        break
                    else:
                        snake.append_head(new_node) # update snake position
                        snake.remove_tail()
                    
                elif direction == 3:
                    current_node = snake.head # snake head
                    new_node = Node([current_node.position[0] + 1,current_node.position[1]]) # move up
                    direction = 2 # head direction
                    step_num += 1
                    
                    if snake.contain(new_node): # exclude tail
                        print(step_num)
                        alive = False
                        break
                    else:
                        snake.append_head(new_node) # update snake position
                        snake.remove_tail()
                    
            elif step == 'R':
                if direction == 0:
                    current_node = snake.head # snake head
                    new_node = Node([current_node.position[0] + 1 ,current_node.position[1]]) # move up
                    direction = 2 # head direction
                    step_num += 1
                    
                    if snake.contain(new_node): # exclude tail
                        print(step_num)
                        alive = False
                        break
                    else:
                        snake.append_head(new_node) # update snake position
                        snake.remove_tail()
            
                elif direction == 1:
                    current_node = snake.head # snake head
                    new_node = Node([current_node.position[0] ,current_node.position[1] + 1]) # move up
                    direction = 0 # head direction
                    step_num += 1
                    
                    if snake.contain(new_node): # exclude tail
                        print(step_num)
                        alive = False
                        break
                    else:
                        snake.append_head(new_node) # update snake position
                        snake.remove_tail()
                    
                elif direction == 2:
                    current_node = snake.head # snake head
                    new_node = Node([current_node.position[0] ,current_node.position[1] - 1]) # move up
                    direction = 3 # head direction
                    step_num += 1
                    
                    if snake.contain(new_node): # exclude tail
                        print(step_num)
                        alive = False
                        break
                    else:
                        snake.append_head(new_node) # update snake position
                        snake.remove_tail()
                    
                elif direction == 3:
                    current_node = snake.head # snake head
                    new_node = Node([current_node.position[0] - 1 ,current_node.position[1]]) # move up
                    direction = 1 # head direction
                    step_num += 1
                    
                    if snake.contain(new_node): # exclude tail
                        print(step_num)
                        alive = False
                        break
                    else:
                        snake.append_head(new_node) # update snake position
                        snake.remove_tail()
        if alive and n == step_num:
            #snake.print_()
            print("YES")


if __name__ == '__main__':
    main()

