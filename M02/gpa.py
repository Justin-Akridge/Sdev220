#Justin Akridge
#gpa.py
#Program sees whether person has made the deans list or honor roll
#last_name and first_name store students full name
#gpa stores the students gpa

def honor_roll():
    last_name = input("Enter last name or ZZZ to quit: ")
    while last_name != "ZZZ":
        first_name = input("Enter first name: ")
        gpa = float(input("Enter gpa: "))
        if gpa >= 3.25 and gpa < 3.5:
            print(f"{first_name} {last_name} has made the honor roll!")
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the deans list!")
        else:
            print(f"{first_name} {last_name} did not make the deans list or honor roll")
        last_name = input("Enter last name or ZZZ to quit: ")
            
honor_roll()