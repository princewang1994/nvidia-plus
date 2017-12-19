import os
import re
import psutil
import terminaltables

from utils import get_user_from_pid

cmd = os.popen('/usr/bin/nvidia-smi')
pattern = re.compile('\s*')
gpu_line_re = re.compile('|')

# Get Nvidia-smi Output
cmd_out = cmd.readlines()
cmd_out = [line.strip() for line in cmd_out]

# Fine Middle Blank Line
for i, line in enumerate(cmd_out):
    if line == '':
        break

# Get gpu_status and gpu_usage
gpu_status = cmd_out[:i]
usage = cmd_out[i+5:-1]

usage = [line.replace('|', ' ').strip() for line in usage]
usage = [pattern.split(line) for line in usage]
[line.insert(2, get_user_from_pid(line[1])) for line in usage]

# Add Table Data
head = [['GPU', 'PID', 'User', 'Type', 'Process name', 'GPU Menmory']]
table_data = head + usage

# Print Table
table = terminaltables.AsciiTable(table_data)
table.padding_left = 4

for line in gpu_status:
    print line
print table.table
