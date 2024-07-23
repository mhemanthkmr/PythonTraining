while True :
    print("""
        Please select your options below :
            1) Calculate BMI 
            2) Exit
    """)
    choice = int(input("Enter your Choices : "))
    if(choice == 1) :
        print("")
        name = input("Enter your name : ")
        weight = float(input("Please enter weight in (KG) : "))
        height = float(input("Please enter height in (CM) : "))
        heightMeter = height / 100
        bmi = weight / heightMeter ** 2
        if(bmi < 18.4) :
            bmiIndex = "Under Weight"
            print(f"{name} Under Weight")
        elif (bmi > 18.4 and bmi < 24.9) :
            bmiIndex = "Normal"
            print(f"{name} Normal")
        elif (bmi > 24.9 and bmi < 39.9) :
            bmiIndex = 'Over Weight'
            print(f"{name} Over Weight")
        else :
            bmiIndex = 'Obese'
            print(f"{name} Obese")
        
        # query = f"Insert into persons_bmi (name,weight,height,bmiIndex) values ({name},{weight},{height},{bmiIndex})"
        # executeQuery(query)
    elif (choice == 2) :
        print("Program Successfully Executed")
        break
    else :
        print("Invalid Choices")

while True:
    print("Heloo World")