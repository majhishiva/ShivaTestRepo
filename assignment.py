#percentage
#dis
#first



marks = input ("enter the marks obtained")
marks = int(marks)


if (marks > 100 or marks < 0):
    division = "invalid"
    

elif marks >=80:
    division = "distinction"
    
    
elif marks >=60:
    division = "first"
    
    
elif marks >=40:
    division = "second"
    
    
else:
    division = "failed"
    
print ("\nYour division is: " + division)
    