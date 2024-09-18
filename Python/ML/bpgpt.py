def check_bp(systolic, diastolic):
    if systolic < 90 or diastolic < 60:
        print("Low blood pressure!")
    elif systolic > 120 or diastolic > 80:
        print("High blood pressure!")
    else:
        print("Normal blood pressure.")

# Test the function with some sample values
check_bp(80, 90)  # Normal blood pressure
#check_bp(50, 40)  # Low blood pressure!
#check_bp(140, 90)  # High blood pressure!