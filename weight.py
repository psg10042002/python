weight = float(input('enter a weight:'))
units = input('L(lbs) or K(kilos):')
if units.upper()=='L':
    cweight = 0.45*weight
    print('weight in kilos is',cweight)
elif units.upper()=='K':
    cweight = 2.2*weight
    print('weight in lbs is',cweight)
else:
    print('incorrect')
    
