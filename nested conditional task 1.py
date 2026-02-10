#Take input for the student that he can attend the exam or not
medical_cause=input("did you have a medical cause Y or N: ")

#Take input for the attendence
atten = int(input("Enter the attendence of the student: "))

#checking the user input, predicting poutput accordingly
if medical_cause == "Y": #checking the condition 1
    print("You are alllowed to take a leave")
else:
    if atten>=75: #checking ifor condition 2
        print("Allowed to take a leave")
    else:
        print("Sorry not allowed to take leave")