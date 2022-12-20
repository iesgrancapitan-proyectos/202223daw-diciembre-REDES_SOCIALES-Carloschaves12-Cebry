import os

command = 'atrm $(atq | cut -f1)'

print (command)
os.system(command)