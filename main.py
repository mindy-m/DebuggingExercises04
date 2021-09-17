# Fix the logic errors in the code to correctly report a student's letter grade!

output = "The student's score of {0}% is a(n) '{1}'."

score_percent = 93.5

if score_percent > 90:
  letter_grade = 'O'
elif score_percent > 70:
  letter_grade = 'A'
elif score_percent > 80:
  letter_grade = 'E'
elif score_percent <= 60:
  letter_grade = 'P'
else:
  letter_grade = 'T'

print(output.format(score_percent, letter_grade))