larg=float(input('Digite a largura da parede: '))
alt=float(input('Digite a altura da parede '))

area= larg*alt
tinta= area/2

print('A área da parede é de {:.2f} m² serão nescessários {:.2f} L de tinta'.format (area, tinta))