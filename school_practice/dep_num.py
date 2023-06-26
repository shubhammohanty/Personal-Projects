#a digit each needs to be assigned to three depratments ie the police, fire and sanitation. The digits that can be used are from 1 to 7. But there are certain conditions- 1)each depratment needs to be assigned with a different digit. 2)sum of digits of all three depratments should be 12. 3)the digit assigned to the police should be even. 

for fire in range(1,8):
    for police in range(2,8,2):
        for sanitation in range(1,8):
            if (fire==police or fire==sanitation or police==sanitation or police+fire+sanitation!=12):
                continue 
            else:
                print(fire, police, sanitation)