# HEART-DISEASE-PREDICTOR

A simple command-line Python program that estimates a person's risk of heart disease based on basic health inputs. Built as a capstone project for the Fundamentals of AI and ML course.

---

## What It Does

The program asks the user a series of health-related questions and uses a rule-based scoring system to estimate their heart disease risk level. It outputs one of four risk categories: **Low**, **Moderate**, **High**, or **Very High**, along with a breakdown of which factors contributed to the score.

---

## How to Run

### Requirements
- Python 3.x (no extra libraries needed)

### Steps

1. Clone or download this repository:
   ```
   git clone https://github.com/your-username/heart-disease-risk-predictor
   cd heart-disease-risk-predictor
   ```

2. Run the program:
   ```
   python heart_disease_predictor.py
   ```

3. Answer the questions when prompted. That's it!

---

## Questions Asked

The program collects the following inputs:

| Input | Options |
|---|---|
| Age | Number (1–120) |
| Gender | male / female |
| Blood pressure | normal / elevated / high |
| Cholesterol level | normal / borderline / high |
| Smoking status | yes / no |
| Diabetes | yes / no |
| Regular exercise | yes / no |
| Family history of heart disease | yes / no |
| BMI category | underweight / normal / overweight / obese |

---

## How the Risk Score Works

Each factor is assigned a point value based on how strongly it is linked to heart disease risk (based on widely known medical guidelines):

| Factor | Points |
|---|---|
| Age 65+ | +3 |
| Age 55–64 | +2 |
| Age 45–54 | +1 |
| Male over 45 / Female over 55 | +1 |
| High blood pressure | +3 |
| Elevated blood pressure | +1 |
| High cholesterol | +3 |
| Borderline cholesterol | +1 |
| Smoker | +3 |
| Diabetes | +2 |
| Family history | +2 |
| Obese BMI | +2 |
| Overweight BMI | +1 |
| Regular exercise | –1 (protective) |

**Risk levels (out of 18):**
- 0–3 → Low
- 4–7 → Moderate
- 8–12 → High
- 13+ → Very High

---

## Sample Output

```
==================================================
           YOUR RESULTS
==================================================

Risk factors considered:
  - Age 45-54 (+1)
  - High blood pressure (+3)
  - Smoker (+3)
  - Family history of heart disease (+2)
  - Regular exercise (-1, protective)

Your total risk score: 8 / 18

RISK LEVEL: HIGH

Your risk of heart disease appears to be HIGH.
Please consult a doctor soon. Lifestyle changes
like quitting smoking, eating better, and exercising
can make a big difference.
```

---

## Disclaimer

This tool is for **educational purposes only**. It is not a medical device and does not provide a clinical diagnosis. Always consult a qualified doctor for actual medical advice.

---

## Project Structure


heart-disease-risk-predictor/
│
├── heart_disease_predictor.py   # Main program
├── README.md                    # This file
└── Project_Report.docx          # Full project report




## Author

Made by Saurav Singh | Fundamentals of AI and ML | VIT
