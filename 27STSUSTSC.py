# Enter your code here. Read input from STDIN. Print output to STDOUT
# Input from stdin
averageX, averageY = [float(num) for num in input().split(" ")]

# Cost
CostX = 160 + 40*(averageX + averageX**2)
CostY = 128 + 40*(averageY + averageY**2)

print(round(CostX,1))
print(round(CostY,1))