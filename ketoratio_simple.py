# keto macro percentage calculator.

#import math 


#def round_up(n, decimals=0):
#	multiplier = 10 ** decimals
#	return math.ceil(n * multiplier) / multiplier 
	

print("------- E N T E R   M A C R O S ----------- " )

f = int(input("grams of fat: "))
p = int(input("grams of protein: "))	
c = int(input("grams of carbs: "))

# per gram of: fat - 9 cal, protein - 4 cal, carbs - 4 cal	
s = [f * 9.00, p * 4.00, c * 4.00]

macrosSum = sum(s)	 # sum of calories
print("total calories: ", macrosSum)
divide = 100.00 / macrosSum   # decimals number to divide into
multTotcal = macrosSum * divide # to check if it comes to a 100% 
print("is this 100%?> ", multTotcal)
print("your total calories: ", macrosSum)
ratio = s[0] * divide, s[1] * divide, s[2] * divide

print("your ratio percentage: ", ratio)







