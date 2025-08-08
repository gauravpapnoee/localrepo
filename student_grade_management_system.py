# this is a system used to find student grade.
# grade system is defined as :- A   -->  greater than 90%
#                                B   -->  between 80-90 %
#                               C    --> between  70-80 %
#                               D    --> between  60-70 %
#                               E    --> between  50-60 %
# enter the marks out of 100.

count = int(input("enter the number of subjects you have"))
total_marks = 0
i = 0
# taking input of marks
while i<count:
    marks = int(input(f"enter marks of {i+1} subject"))
    total_marks += marks
    i+=1 

percentage = total_marks/count
if percentage>90:
    print("you have got grade A")
elif percentage>80 and percentage<90:
    print("you have got grade B")
elif percentage>70 and percentage<80:
    print("you have got grade C")
elif percentage>60 and percentage<70:
    print("you have got grade D")
elif percentage>50 and percentage<60:
    print("you have got grade E")




