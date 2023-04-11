# cook your dish here
t=int(input())
while t!=0:
    n=int(input())
    s=input()
    l=[]
    for i in s:
        if i=='H' or i=='T':
            l.append(i)
    l=''.join(l)
    if len(l)==0:
        print("Valid")
    else:
        k=l.count('HT')
        if len(l)%2==0:
            if k==len(l)//2:
                print("Valid")
            else:
                print("Invalid")
        else:
            if k==len(l)//2+1:
                print("Valid")
            else:
                print("Invalid")
    
    # print(k)
    t-=1
            
            
            
            
            
            
            
            ############CAN BE DONE IN THIS WAY TOO############
            
            
            
 # function to check if a report is valid
def is_valid_report(report):
    # check if the report starts with zero or more '.'
    if report[0] != '.':
        return False
        # check if the report ends with zero or more '.'
    if report[-1] != '.':
        return False
    # split the report into snakes
    snakes = report.split('T')
    # check if each snake is valid
    for snake in snakes:
        # check if the snake starts with 'H'
        if snake[0] != 'H':
            return False
        # check if the snake ends with zero or more '.'
        if snake[-1] != '.':
            return False
        # check if the snake has at least one 'T'
        if 'T' not in snake:
            return False
        # check if there are no 'H's after the first 'T'
        if 'H' in snake[snake.index('T'):]:
            return False
    # if all checks pass, the report is valid
    return True

# read the number of reports
R = int(input())

# process each report
for i in range(R):
    # read the length of the report
    L = int(input())
    # read the report string
    report = input()
    # check if the report is valid and print the result
    if is_valid_report(report):
        print("Valid")
    else:
        print("Invalid")
