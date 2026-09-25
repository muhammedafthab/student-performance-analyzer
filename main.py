


# Function to get valid marks
def get_valid_marks(subject):
    while True:
        try:
            marks = float(input("Enter " + subject + " marks: "))

            if marks < 0 or marks > 100:
                print("Invalid marks! Enter a value between 0 and 100.")
            else:
                return marks

        except ValueError:
            print("Invalid input! Please enter a number.")
def get_performance(marks):
    if marks >= 90:
        return "Excellent"
    elif marks >= 80:
        return "Very Good"
    elif marks >= 70:
        return "Good"
    elif marks >= 60:
        return "Average"
    else:
        return "Needs Improvement"            

print("==============================")
print("   STUDENT PERFORMANCE REPORT")
print("==============================")
# Student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")


# Enter marks
dsa = get_valid_marks("DSA")
oop = get_valid_marks("OOP")
maths = get_valid_marks("Maths")
dsa_performance = get_performance(dsa)
oop_performance = get_performance(oop)
maths_performance = get_performance(maths)
if dsa >= oop and dsa >= maths:
    highest_subject = "DSA"
    highest_marks = dsa

elif oop >= dsa and oop >= maths:
    highest_subject = "OOP"
    highest_marks = oop

else:
    highest_subject = "Maths"
    highest_marks = maths
if dsa <= oop and dsa <= maths:
    lowest_subject = "DSA"
    lowest_marks = dsa

elif oop <= dsa and oop <= maths:
    lowest_subject = "OOP"
    lowest_marks = oop

else:
    lowest_subject = "Maths"
    lowest_marks = maths

# Calculate average
average = (dsa + oop + maths) / 3
total=dsa+oop+maths



# Grade and performance
if average >= 90:
    grade = "A+"
    performance = "Excellent"

elif average >= 80:
    grade = "A"
    performance = "Very Good"

elif average >= 70:
    grade = "B"
    performance = "Good"

elif average >= 60:
    grade = "C"
    performance = "Average"

else:
    grade = "D"
    performance = "Needs Improvement"
if average>=40:
   status="pass"
else:
    status="fail"
summary = name + " scored an average of " + str(round(average, 2)) + " marks and achieved Grade " + grade + "."

# Display result
print()
print("====================================")
print("        STUDENT RESULT")
print("====================================")

print("Student Name :", name)
print("Roll Number  :", roll_no)

print()
print("----------- SUBJECTS ---------------")
print("DSA   :", dsa)
print("       Performance :", dsa_performance)

print("OOP   :", oop)
print("       Performance :", oop_performance)

print("Maths :", maths)
print("       Performance :", maths_performance)

print()
print("----------- OVERALL ----------------")
print("Total Marks :", total)
print("Average     :", round(average, 2))
print("Grade       :", grade)
print("Performance :", performance)
print("Status      :", status)
print("Highest Subject :", highest_subject)
print("Highest Marks   :", highest_marks)
print("Lowest Subject  :", lowest_subject)
print("Lowest Marks    :", lowest_marks)

print("====================================")
print()
print("----------- SUMMARY ----------------")
print("Summary:", summary)