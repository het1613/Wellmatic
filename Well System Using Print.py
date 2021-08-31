from math import pi, log

def wellDistance():
    global pump_x, pump_y, current_x, current_y, well_num, k, d, s, t, q
    distance=((pump_x-current_x)**2+(pump_y-current_y)**2)**0.5
    calc1=(-0.5772)-(log(((distance**2)*s)/(4*k*d*t)))
    calc2=q/(4*pi*k*d)
    drawdown=calc1*calc2
    print('{:<10}{:<10.1f}{:<10.1f}{:<23.1f}{:.2f}'.format(well_num, current_x, current_y, distance, drawdown))
    well_num+=1

x_wells = int(input('Enter number of x wells: '))
y_wells = int(input('Enter number of y wells: '))

x_distance = eval(input('\nEnter distance between x wells: '))
y_distance = eval(input('Enter distance between y wells: '))

print('\nDefault Values For Drawdown:')
print('Well flow rate in m^3/s (q value): 0.007')
print('Aquifer permeability in m/s (k value): 0.0006')
print('Original aquifer saturated thickness in m (D value): 16')
print('Aquifer storage coefficient (S value): 0.001')
print('Time since pumping began in s (t value): 86400\n')

q=eval(input('Enter well flow rate in m^3/s (q value): '))
k=eval(input('Enter aquifer permeability in m/s (k value): '))
d=eval(input('Enter original aquifer saturated thickness in m (D value): '))
s=eval(input('Enter aquifer storage coefficient (S value): '))
t=eval(input('Enter time since pumping began in s (t value): '))

max_y = (y_wells-1)*y_distance
max_x = (x_wells-1)*x_distance

pump_x=max_x/2
pump_y=max_y/2

current_x=0
current_y=0
well_num=1

print('\nPump X Coordinate: {}m'.format(pump_x))
print('Pump Y Coordinate: {}m'.format(pump_y))

print('\n{:<10}{:<10}{:<10}{:<23}{}'.format('Well #', 'X (m)', 'Y (m)', 'Radial Distance (m)', 'Drawdown (m)'))

#side 1
for well in range(y_wells-1):
    wellDistance()
    current_y+=y_distance

#side 2
for well in range(x_wells-1):
    wellDistance()
    current_x+=x_distance

#side 3
for well in range(y_wells-1):
    wellDistance()
    current_y-=y_distance

#side 4
for well in range(x_wells-1):
    wellDistance()
    current_x-=x_distance

well_1=y_wells
well_2=y_wells+1
well_3=y_wells+x_wells-1
well_4=well_num-1

print('\nDrawdown Information: ')
print('Well flow rate in m^3/s (q value): {}'.format(q))
print('Aquifer permeability in m/s (k value): {}'.format(k))
print('Original aquifer saturated thickness in m (D value): {}'.format(d))
print('Aquifer storage coefficient (S value): {}'.format(s))
print('Time since pumping began in s (t value): {}\n'.format(t))

print('DRAWING PLAN:\n')

print(' '*6, end='')
for i in range(x_wells-2):
    print('{:<3}'.format(well_2), end='')
    well_2+=1
print()

print('{:<3}'.format(well_1), end='')
well_1-=1

for i in range(x_wells):
    print('{:<3}'.format('*'), end='')
print(well_3)
well_3+=1

for i in range(y_wells-2):
    print('{:<3}'.format(well_1)+'*'+' '*(3*(x_wells-1)-1)+'*  '+str(well_3))
    well_1-=1
    well_3+=1

print('{:<3}'.format(well_1), end='')
well_1-=1

for i in range(x_wells):
    print('{:<3}'.format('*'), end='')
print(well_3)

print(' '*6, end='')
for i in range(x_wells-2):
    print('{:<3}'.format(well_4), end='')
    well_4-=1

print('\n')
