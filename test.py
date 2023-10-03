def nums():
   
    prime_numbers = [1, 3, 4,]
    for num_i in range(len(prime_numbers)):
        num_pos = num_i + 1
        num = prime_numbers[num_i]
        print("Prime Numbers # " + str(num_pos) + ": " + str(num) )
      

def num_1():
    prime_numbers = [1, 3, 4,]
    for num_pos, num in enumerate(prime_numbers, start = 1):
        print(f"Prime Numbers # {num_pos} : {num}")
        
num_1()