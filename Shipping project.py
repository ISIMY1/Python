
weight = float(input("Enter the weight of your package: "))

##Ground shipping 
ground_cost = ""
flat_charge = 20
premium_ground_shiping = 125

if weight <= 2:
  ground_cost = 1.5 * weight + flat_charge
elif weight >= 2 and weight <= 6:
  ground_cost = 3.00 * weight + flat_charge
elif weight >= 6 and weight <=10:
  ground_cost = weight * 4.00 + flat_charge
else: 
  ground_cost = weight * 4.75 + flat_charge

##Drone Shipping 
drone_cost = ""

if weight <= 2:
  drone_cost = 4.5 * weight 
elif weight >= 2 and weight <= 6:
  drone_cost = 9.00 * weight 
elif weight >= 6 and weight <=10:
  drone_cost = weight * 12.00 
else: 
  drone_cost = weight * 14.25

print("Ground cost = $", ground_cost)

print("Ground cost with premium = $", ground_cost + premium_ground_shiping)

print("Drone cost = $", drone_cost)