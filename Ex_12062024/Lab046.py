#program to calculate and display the grades based on the score

#Multiple conditions if elif else

# step1 Logic building
# Input -score data type int

score= int(input("Enter the score\n"))
#Output - String (A,B,C,D) str


#Step 2
#write a rough logice and convert it into real one

#score >=90 - <=100, A
#score >=80 - <=89, A
#score >=70 - <=79, A
#score >=60 - <=69, A
#score >=50 - <=59, A

if score >=90 and score <=100:
    print("Grade is A")
elif score >=80 and score <=89:
    print("Grade is B")
elif score >=70 and score <=79:
    print("Grade is C")
elif score >=60 and score <=69:
    print("Grade is D")
elif score >=0 and score <=59:
    print("Grade is F")
else:
    print("Invalid score")

#if 90<= score <=100:

# we can use loops within loops
# else is not always mandatory


