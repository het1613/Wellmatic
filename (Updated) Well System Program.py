from csv import writer
from math import pi, log

def wellDistance():
    global pump_x, pump_y, current_x, current_y, well_num, T, s, t, q, total_drawdown, total_flow

    new_q=q

    distance=((pump_x-current_x)**2+(pump_y-current_y)**2)**0.5
    calc1=(-0.5772)-(log(((distance**2)*s)/(4*T*t)))
    calc2=new_q/(4*pi*T)
    drawdown=calc1*calc2
    total_drawdown+=drawdown
    total_flow.append(new_q)
    csvwriter.writerow([well_num, '{:.1f}'.format(current_x), '{:.1f}'.format(current_y), '{:.6f}'.format(new_q), '{:.1f}'.format(distance), '{:.2f}'.format(drawdown)])
    well_num+=1

name=input('Enter project name: ')

x_wells = int(input('\nEnter number of x wells: '))
y_wells = int(input('Enter number of y wells: '))

x_distance = eval(input('\nEnter distance between x wells (m): '))
y_distance = eval(input('Enter distance between y wells (m): '))

print('\nDefault Values For Drawdown:')
print('Well flow rate in m^3/s (q value): 0.007')
print('Transitivity in m^2/s (T value): 0.0096')
print('Aquifer storage coefficient (S value): 0.001')
print('Time since pumping began in s (t value): 864000\n')

q=float(input('Enter well flow rate in m^3/s (q value): '))
T=float(input('Enter transitivity value in m^2/s (T value): '))
s=float(input('Enter aquifer storage coefficient (S value): '))
t=float(input('Enter time since pumping began in s (t value): '))

total_drawdown=0
total_flow=[]

max_y = (y_wells-1)*y_distance
max_x = (x_wells-1)*x_distance

pump_x=max_x/2
pump_y=max_y/2

current_x=0
current_y=0
well_num=1

csv_file=open("Well Systems.csv", "w", newline= '')
csvwriter = writer(csv_file)

csvwriter.writerow(['Project: '+name])
csvwriter.writerow(['Pump X Coordinate: {}m'.format(pump_x)])
csvwriter.writerow(['Pump Y Coordinate: {}m'.format(pump_y)])

csvwriter.writerow(['Well #', 'X (m)', 'Y (m)', 'Well Flow Rate (m^3/s)', 'Radial Distance (m)', 'Drawdown (m)'])

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

csvwriter.writerow(['', '', '', 'Total Flow Rate: {:.3f}m^3/s OR {:.3f}L/s'.format(sum(total_flow), sum(total_flow)*1000), '', 'Total Drawdown: {:.2f}m'.format(total_drawdown)])
csv_file.close()

txt_file= open('Well Systems Drawing.txt', 'w')

well_1=y_wells
well_2=y_wells+1
well_3=y_wells+x_wells-1
well_4=well_num-1

txt_file.write('Project: '+name)
txt_file.write('\n\nDrawdown Information:\n')
txt_file.write('Well flow rate in m^3/s (q value): {}\n'.format(q))
txt_file.write('Transitivity (T value): {}\n'.format(T))
txt_file.write('Aquifer storage coefficient (S value): {}\n'.format(s))
txt_file.write('Time since pumping began in s (t value): {}\n'.format(t))

txt_file.write('\nDRAWING PLAN:\n\n')

txt_file.write(' '*6)
for i in range(x_wells-2):
    txt_file.write('{:<3}'.format(well_2))
    well_2+=1
txt_file.write('\n')

txt_file.write('{:<3}'.format(well_1))
well_1-=1

for i in range(x_wells):
    txt_file.write('{:<3}'.format('*'))
txt_file.write(str(well_3)+'\n')
well_3+=1

for i in range(y_wells-2):
    txt_file.write('{:<3}'.format(well_1)+'*'+' '*(3*(x_wells-1)-1)+'*  '+str(well_3)+'\n')
    well_1-=1
    well_3+=1

txt_file.write('{:<3}'.format(well_1))
well_1-=1

for i in range(x_wells):
    txt_file.write('{:<3}'.format('*'))
txt_file.write(str(well_3)+'\n')

txt_file.write(' '*6)
for i in range(x_wells-2):
    txt_file.write('{:<3}'.format(well_4))
    well_4-=1

txt_file.close()
