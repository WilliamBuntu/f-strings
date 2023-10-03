def assrt():
    number = 5
    assert f"Square: {number*number}" == 'Square: 25'

task_ids = [1, 2, 3]
task_names = ['Do homework', 'Laundry', 'Pay bills']
task_agencies = [5, 3, 4]

# for i in range(3):
#     print(f'{task_ids[i]:^12} {task_names[i]:^12} {task_agencies[i]:^12}')


def create_foramtted_records(fmt):
    
    for i in range(3):
        task_id = task_ids[i] 
        name = task_names[i]
        urgency = task_agencies[i]
        
        print(f'{task_id:{fmt}} {name:{fmt}} {urgency:{fmt}}')
    
    large_prime_number = 1000000007
    decimal_number = 344
    sci_number = 0.00000000412733
    pct_number = 0.179323
    
    print(f'Use comma: {large_prime_number:,d}')  
    print(f'Two digits: {decimal_number:x}') 
    print(f'Sci notation: {sci_number:.2e}') 
    print(f'Percentage: {pct_number:.2%}')
create_foramtted_records('^15')