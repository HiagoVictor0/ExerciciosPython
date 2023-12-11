import math 

an = float(input('Digite o angulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tang = math.tan(math.radians(an))

print('O seno do angulo {} é {:.2f}'.format(an, sen))
print('O cosseno do angulo {} é {:.2f}'.format(an, cos))
print('O tangente do angulo {} é {:.2f}'.format(an, tang))
