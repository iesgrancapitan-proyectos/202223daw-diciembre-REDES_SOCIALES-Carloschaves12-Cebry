from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

import sys
import os
import json

jobs_file = '../' + os.getenv('JOBS_FILE')
tareas_scripts_file = '../' + os.getenv('JOB_SCRIPT_RELATION_FILE')

def get_tareas_scripts():
    file = open(tareas_scripts_file, 'r') 
    file_content = json.load(file)
    file.close()
    return file_content

def get_tareas():
    file = open(jobs_file, 'r') 
    file_content = json.load(file)
    file.close()
    return file_content

def main():
    if len(sys.argv) != 1:
        print('nombreSript.py')
        exit()
    tareas_scripts = get_tareas_scripts()
    tareas_scripts.append({
        'REESTART_POSTING': 'src/control/startPosting.py'
    })
    
    tareas = get_tareas()
    tareas.append({
        'time': 'now + 1 minute',
        'script': 'REESTART_POSTING'
    })

    for tarea in tareas:
        command = 'echo "python3 '+ tareas_scripts[tarea['script']]
        if tarea.get('account') != None:
            command += ' ' + tarea['account']
            
        command += '" | at ' + tarea['time']
        
        print (command)
        os.system(command)
if __name__ == '__main__':
    main()