def validate_age(age):
    
    if not isinstance(age, (int, float)):
        return "invalid"
    if age < 0 or age > 150:
        return "invalid"
    if age < 18:
        return "minor"
    elif age < 65:
        return "adult"
    else:
        return "senior"
        
x = 10
y = 20
z = 30
if x < y and y < z:
    print("Increasing sequence")
