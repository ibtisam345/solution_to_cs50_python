def main():
    bill = dollars_to_float("How much was the bill? ")
    tip_percentage = percent_to_float("What percentage would you like to tip? ")

    tip = bill * tip_percentage 

    print(f"Leave ${tip:.2f}")

def dollars_to_float(prompt):
    dollar = float(input(prompt).strip().replace("$", ""))
    return dollar

def percent_to_float(prompt):
    percent = float(input(prompt).replace("%", "").strip())
    return percent / 100

main()
    

