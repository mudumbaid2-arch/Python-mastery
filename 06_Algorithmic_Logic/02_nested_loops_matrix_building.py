


        
            





### Exercise 4
for rows in range(1,11):
    for columns in range(1,11):
        if  rows*columns%3==0:
            print(rows*columns, end=" ")
        else:
            print("*", end = " ")


    print()




### Exercise 5
flag = False
for floor in range(1,9):
    for level in range(1,5):
        if floor ==1:
            flag = True
            print(f"the {floor}st floor is the lobby area")
            
        elif floor ==7 and level!=4:
            flag = True
            print(f"the rest of the {floor}th floor is lock due to security purposes accept level 4")

        else:
            flag=True
            print(f"the {floor}th floor  is open to everyone and require and a level 1 security clearance")
            
print()



### Exercise 6
for student in range(1,6):
    for test in range(1,4):
        score = int(input(f"enter your score for the {student} student , and {test} test"))
        if score<=50:
            print("You Have FAILED")
        elif score>=90:
            print("You have acheived an Aplus congrats")
        elif score>=50 and score<90:
            print(f"Work harder and get a better score next time mr:{student}")
        


        if test==3:
            
            print("Next student please come forward to collect your results")


### Exercise 7
a=0
user_input = int(input("enter the number of rows and columns you would like(r,c)"))
for rows in range(1,user_input+1):
    for columns in range(1,user_input+1):
        if rows==1:
            print("*" , end = " ")
        
        elif rows == user_input:
            print("*" , end = " ")

   



        if rows>1 and rows<user_input:
            if columns ==1 or columns==user_input:
                a=user_input*2-3
                print("*", end = " " *a)
    print()



### classic two sum excercise

array = [1,2,3,6,8,90]
target = int(input("enter a number"))
for i in range(0,len(array)):
    for j in range(0,len(array)):
        if i==j:
            continue
        if i+j==target:
            print([i],[j],"target has been acquired")
        

        
print()


### palindromic substring

        









    




        

        


        

       



        

    

        
                
            








