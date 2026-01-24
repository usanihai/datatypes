# # "  Guys, once you awake: practice on below scenario:
# """
#     Scenario: A university checks two datasets: GPA and SAT scores to determine admission.
#     Inputs: Student's GPA (0.0 to 4.0) and SAT Score (400 to 1600).
#     Rules:
#     Automatic Admission: GPA \ge 3.8 AND SAT \ge 1400.
#     Probationary Admission: GPA \ge 3.0 AND SAT \ge 1100.
#     Rejected: Anything lower than the criteria above.
#     Output: Print "Admitted", "Probation", or "Not Eligible"""


# GPA = float(input("Enter GPA scores: "))
# SAT = int(input("Enter SAT scores: "))
#
# if 4.0 <= GPA >=3.8 and 1600 <= SAT >= 1400:
#    print ("Admitted")
#
# elif 3.0 > GPA < 3.8 and 1100 > SAT < 1400:
#     print("Probationary3. Admission")
#
# else:
#     print("Not admitted or eligible")


"""Scenario: An automated system decides whether to turn on the AC or Heater based on the Current Temperature and Humidity Level.
Inputs: Temperature (Celsius) and Humidity percentage.
Rules:
If Temperature > 30°C:
If Humidity > 70%, print "Turn on AC and Dehumidifier".
Otherwise, print "Turn on AC".
If Temperature < 15°C, print "Turn on Heater".
Otherwise, print "System Idle".   """

Temp = int(input("Enter Temperature: "))
Humidity = int(input("Enter Humidity: "))
if Temp > 30 and Humidity > 70:
    print("Turn on AC and Dehumidifier")
elif Temp < 15 and Humidity < 60:
    print("Turn on Heater")
else:
    print("System Idle")


















  
  
