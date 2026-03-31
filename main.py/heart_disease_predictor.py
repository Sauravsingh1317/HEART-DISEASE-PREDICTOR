# Heart Disease Risk Predictor
# A simple program to check heart disease risk based on some health factors
# Made for: Fundamentals of AI and ML - Course Project

print("=" * 50)
print("   HEART DISEASE RISK PREDICTOR")
print("=" * 50)
print()
print("This program will ask you some health-related questions")
print("and give you an estimate of your heart disease risk.")
print()
print("NOTE: This is NOT a medical diagnosis. Please consult")
print("a doctor for actual medical advice.")
print()

# ------- collect user inputs -------

# Age
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 1 or age > 120:
            print("Please enter a valid age between 1 and 120.")
        else:
            break
    except ValueError:
        print("Please enter a number.")

# Gender
while True:
    gender = input("Enter your gender (male/female): ").strip().lower()
    if gender in ["male", "female"]:
        break
    print("Please enter 'male' or 'female'.")

# Blood pressure
print()
print("Blood pressure categories:")
print("  normal   = less than 120/80")
print("  elevated = 120-129 / less than 80")
print("  high     = 130/80 or above")
while True:
    bp = input("Enter your blood pressure category (normal/elevated/high): ").strip().lower()
    if bp in ["normal", "elevated", "high"]:
        break
    print("Please enter 'normal', 'elevated', or 'high'.")

# Cholesterol
print()
print("Cholesterol levels (mg/dL):")
print("  normal = below 200")
print("  borderline = 200-239")
print("  high = 240 or above")
while True:
    cholesterol = input("Enter your cholesterol level (normal/borderline/high): ").strip().lower()
    if cholesterol in ["normal", "borderline", "high"]:
        break
    print("Please enter 'normal', 'borderline', or 'high'.")

# Smoking
while True:
    smoking = input("\nDo you smoke? (yes/no): ").strip().lower()
    if smoking in ["yes", "no"]:
        break
    print("Please enter 'yes' or 'no'.")

# Diabetes
while True:
    diabetes = input("Do you have diabetes? (yes/no): ").strip().lower()
    if diabetes in ["yes", "no"]:
        break
    print("Please enter 'yes' or 'no'.")

# Exercise
while True:
    exercise = input("Do you exercise regularly? (yes/no): ").strip().lower()
    if exercise in ["yes", "no"]:
        break
    print("Please enter 'yes' or 'no'.")

# Family history
while True:
    family_history = input("Does anyone in your family have heart disease? (yes/no): ").strip().lower()
    if family_history in ["yes", "no"]:
        break
    print("Please enter 'yes' or 'no'.")

# BMI
print()
print("BMI categories:")
print("  underweight = below 18.5")
print("  normal      = 18.5 to 24.9")
print("  overweight  = 25 to 29.9")
print("  obese       = 30 or above")
while True:
    bmi_category = input("Enter your BMI category (underweight/normal/overweight/obese): ").strip().lower()
    if bmi_category in ["underweight", "normal", "overweight", "obese"]:
        break
    print("Please enter 'underweight', 'normal', 'overweight', or 'obese'.")


# ------- calculate risk score -------
# Each factor adds points to the risk score
# Higher score = higher risk

risk_score = 0
risk_factors = []  # keep track of what's contributing to risk

# Age scoring
if age >= 65:
    risk_score += 3
    risk_factors.append("Age 65 or older (+3)")
elif age >= 55:
    risk_score += 2
    risk_factors.append("Age 55-64 (+2)")
elif age >= 45:
    risk_score += 1
    risk_factors.append("Age 45-54 (+1)")

# Gender (men have higher risk at younger ages)
if gender == "male" and age >= 45:
    risk_score += 1
    risk_factors.append("Male over 45 (+1)")
elif gender == "female" and age >= 55:
    risk_score += 1
    risk_factors.append("Female over 55 (+1)")

# Blood pressure
if bp == "high":
    risk_score += 3
    risk_factors.append("High blood pressure (+3)")
elif bp == "elevated":
    risk_score += 1
    risk_factors.append("Elevated blood pressure (+1)")

# Cholesterol
if cholesterol == "high":
    risk_score += 3
    risk_factors.append("High cholesterol (+3)")
elif cholesterol == "borderline":
    risk_score += 1
    risk_factors.append("Borderline cholesterol (+1)")

# Smoking
if smoking == "yes":
    risk_score += 3
    risk_factors.append("Smoker (+3)")

# Diabetes
if diabetes == "yes":
    risk_score += 2
    risk_factors.append("Diabetes (+2)")

# Exercise (protective factor - reduces risk)
if exercise == "yes":
    risk_score -= 1
    risk_factors.append("Regular exercise (-1, protective)")

# Family history
if family_history == "yes":
    risk_score += 2
    risk_factors.append("Family history of heart disease (+2)")

# BMI
if bmi_category == "obese":
    risk_score += 2
    risk_factors.append("Obese BMI (+2)")
elif bmi_category == "overweight":
    risk_score += 1
    risk_factors.append("Overweight BMI (+1)")
elif bmi_category == "underweight":
    risk_score += 1
    risk_factors.append("Underweight BMI (+1)")

# Make sure score doesn't go below 0
if risk_score < 0:
    risk_score = 0


# ------- show results -------

print()
print("=" * 50)
print("           YOUR RESULTS")
print("=" * 50)

print("\nRisk factors considered:")
if risk_factors:
    for factor in risk_factors:
        print("  -", factor)
else:
    print("  - No significant risk factors found")

print(f"\nYour total risk score: {risk_score} / 18")

# Determine risk level
print()
if risk_score <= 3:
    print("RISK LEVEL: LOW")
    print()
    print("Your risk of heart disease appears to be LOW.")
    print("Keep up the healthy habits! Regular checkups are")
    print("still important even if your risk is low.")
elif risk_score <= 7:
    print("RISK LEVEL: MODERATE")
    print()
    print("Your risk of heart disease appears to be MODERATE.")
    print("Consider making some lifestyle changes and talking")
    print("to your doctor about your heart health.")
elif risk_score <= 12:
    print("RISK LEVEL: HIGH")
    print()
    print("Your risk of heart disease appears to be HIGH.")
    print("Please consult a doctor soon. Lifestyle changes")
    print("like quitting smoking, eating better, and exercising")
    print("can make a big difference.")
else:
    print("RISK LEVEL: VERY HIGH")
    print()
    print("Your risk of heart disease appears to be VERY HIGH.")
    print("Please see a doctor as soon as possible.")
    print("Do not ignore these warning signs.")

# General tips
print()
print("-" * 50)
print("General Tips to Reduce Heart Disease Risk:")
print("  1. Exercise at least 30 minutes a day")
print("  2. Eat less salt, sugar, and saturated fat")
print("  3. Quit smoking if you smoke")
print("  4. Maintain a healthy weight")
print("  5. Manage stress")
print("  6. Get regular checkups")
print("-" * 50)
print()
print("Remember: This tool is for educational purposes only.")
print("Always consult a qualified doctor for medical advice.")
print()
print("Thank you for using the Heart Disease Risk Predictor!")
