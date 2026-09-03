#Ant Colony Optimization
R1 = 30
R2 = 30
Total = R1 + R2
P1 = R1/Total
P2 = R2/Total
Percentage_1 = P1 * 100
Percentage_2 = P2 * 100
print(f"Path 1 Probability:{Percentage_1}%")
print(f"Path 2 Probability:{Percentage_2}%")
if Percentage_1 >= Percentage_2:
  print("Most ants follow Path 1")
  print(f"Path 1 has the higher chance:{Percentage_1}%")
else:
  print("Most ants follow Path 2")
  print(f"Path 2 has the higher chance:{Percentage_2}%")

Output:
Path 1 Probability:50.0%
Path 2 Probability:50.0%
Most ants follow Path 1
Path 1 has the higher chance:50.0%
