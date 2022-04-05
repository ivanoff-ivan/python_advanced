def list_manipulator(*args):
    numbers = [int(x) for x in args[0]]
    add_or_remove = args[1]
    beginning_or_end = args[2]
    if len(args) >= 4:
        other_parameters = args[3:len(args)]
        other_parameters = [int(x) for x in other_parameters]
    
    if add_or_remove == "add":
        if beginning_or_end == "beginning":
            for parameter in reversed(other_parameters):
                numbers.insert(0, parameter)
            return numbers
        elif beginning_or_end == "end":
            for parameter in other_parameters:
                numbers.append(parameter)
            return numbers
    elif add_or_remove == "remove":
        if beginning_or_end == "beginning":
            if len(args) == 4:
                n = int(args[3])
                for _ in range(n):
                    numbers.pop(0)
                return numbers
            else:
                numbers.pop(0)
                return numbers
        elif beginning_or_end == "end":
            if len(args) == 4:
                n = int(args[3])
                for i in range(n):
                    numbers.pop()
                return numbers
            else:
                numbers.pop()
                return numbers
    
        
print(list_manipulator([1,2,3], "remove", "end"))                   
print(list_manipulator([1,2,3], "remove", "beginning"))             
print(list_manipulator([1,2,3], "add", "beginning", 20))            
print(list_manipulator([1,2,3], "add", "end", 30))                  
print(list_manipulator([1,2,3], "remove", "end", 2))                
print(list_manipulator([1,2,3], "remove", "beginning", 2))          
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))    
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))          	[1, 2]
[2, 3]
[20, 1, 2, 3]
[1, 2, 3, 30]
[1]
[3]
[20, 30, 40, 1, 2, 3]
[1, 2, 3, 30, 40, 50]
