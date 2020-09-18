def main():
    m = int(input()) # number of command
    arrays = []
    for i in range(m):
        y = input()
        y = y.split(' ')
        arrays.append(y[1])
    
    x = 2401 
    y = 2401 #head position starts from [2401][2401], center
    snake = [[x,y]] # right side is head
    step_num = 0
    direction = 'up'
    for array in arrays:
        n = len(array)
        direction = 'up'
        x = 2401 
        y = 2401
        for i in range(n):
            step = array[i]
            if step == 'F'or step == 'E': 
                if direction == 'up' :
                    current_node = snake[-1] # snake head
                    new_node = [current_node[0] ,current_node[1] + 1] # move up
                    direction = 'up' # head direction
                    step_num += 1
                    
                    if new_node in snake: # eat itself
                        print(step_num)
                        break
                    else:
                        snake.append(new_node) # update snake position
                        if step != 'E':  # if no eat apple, delete tail
                            snake.pop(0)
                    
                elif direction == 'left':
                    current_node = snake[-1] # snake head
                    new_node = [current_node[0] - 1,current_node[1]] # move up
                    direction = 'left' # head direction
                    step_num += 1
                    
                    if new_node in snake: # eat itself
                        print(step_num)
                        break
                    else:
                        snake.append(new_node) # update snake position
                        if step != 'E':  # if no eat apple, delete tail
                            snake.pop(0)
                    
                elif direction == 'right':
                    current_node = snake[-1] # snake head
                    new_node = [current_node[0] + 1 ,current_node[1]] # move up
                    direction = 'right' # head direction
                    step_num += 1
                    
                    if new_node in snake: # eat itself
                        print(step_num)
                        break
                    else:
                        snake.append(new_node) # update snake position
                        if step != 'E':  # if no eat apple, delete tail
                            snake.pop(0)
    
                elif direction == 'down': 
                    current_node = snake[-1] # snake head
                    new_node = [current_node[0] ,current_node[1] - 1] # move up
                    direction = 'down' # head direction
                    step_num += 1
                    
                    if new_node in snake: # eat itself
                        print(step_num)
                        break
                    else:
                        snake.append(new_node) # update snake position
                        if step != 'E':  # if no eat apple, delete tail
                            snake.pop(0)  
                    
            elif step == 'L': 
                if direction == 'up':
                    current_node = snake[-1] # snake head
                    new_node = [current_node[0] - 1 ,current_node[1]] # move up
                    direction = 'left' # head direction
                    step_num += 1
                    
                    if new_node in snake: # eat itself
                        print(step_num)
                        break
                    else:
                        snake.append(new_node) # update snake position
                        snake.pop(0)

                elif direction == 'left':
                    current_node = snake[-1] # snake head
                    new_node = [current_node[0] ,current_node[1] - 1] # move up
                    direction = 'right' # head direction
                    step_num += 1
                    
                    if new_node in snake: # eat itself
                        print(step_num)
                        break
                    else:
                        snake.append(new_node) # update snake position
                        snake.pop(0)
    
                elif direction == 'right':
                    current_node = snake[-1] # snake head
                    new_node = [current_node[0] ,current_node[1] + 1] # move up
                    direction = 'up' # head direction
                    step_num += 1
                    
                    if new_node in snake: # eat itself
                        print(step_num)
                        break
                    else:
                        snake.append(new_node) # update snake position
                        snake.pop(0)
                    
                elif direction == 'down':
                    current_node = snake[-1] # snake head
                    new_node = [current_node[0] + 1,current_node[1]] # move up
                    direction = 'right' # head direction
                    step_num += 1
                    
                    if new_node in snake: # eat itself
                        print(step_num)
                        break
                    else:
                        snake.append(new_node) # update snake position
                        snake.pop(0)
                    
            elif step == 'R':
                if direction == 'up':
                    current_node = snake[-1] # snake head
                    new_node = [current_node[0] + 1 ,current_node[1]] # move up
                    direction = 'right' # head direction
                    step_num += 1
                    
                    if new_node in snake: # eat itself
                        print(step_num)
                        break
                    else:
                        snake.append(new_node) # update snake position
                        snake.pop(0)
            
                elif direction == 'left':
                    current_node = snake[-1] # snake head
                    new_node = [current_node[0] ,current_node[1] + 1] # move up
                    direction = 'up' # head direction
                    step_num += 1
                    
                    if new_node in snake: # eat itself
                        print(step_num)
                        break
                    else:
                        snake.append(new_node) # update snake position
                        snake.pop(0)
                    
                elif direction == 'right':
                    current_node = snake[-1] # snake head
                    new_node = [current_node[0] ,current_node[1] - 1] # move up
                    direction = 'down' # head direction
                    step_num += 1
                    
                    if new_node in snake: # eat itself
                        print(step_num)
                        break
                    else:
                        snake.append(new_node) # update snake position
                        snake.pop(0)
                    
                elif direction == 'down':
                    current_node = snake[-1] # snake head
                    new_node = [current_node[0] - 1 ,current_node[1]] # move up
                    direction = 'left' # head direction
                    step_num += 1
                    
                    if new_node in snake: # eat itself
                        print(step_num)
                        break
                    else:
                        snake.append(new_node) # update snake position
                        snake.pop(0)
    if n == step_num:
        print(snake)
        print("YES")
    else:
        print("DEAD")                        


if __name__ == '__main__':
    main()