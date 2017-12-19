from __future__ import print_function
from nvidia import NvidiaTable
from printer import Printer
import re
import os
from nvidia import GPULine, UsageLine

gpu_line_re = re.compile(r'\|\s*(\d*)%.*P\d\s*(\d*)W / (\d*)W.*\|\s*(\d*)MiB / (\d*)MiB.*\|\s*(\d*)%.*')
user_line_re = re.compile(r'\|\s*(\d*)\s*(\d*)\s*(\w)\s*(\S*)\s*(\d*)MiB.*')

if __name__ == '__main__':

    #cmd = os.popen('/usr/bin/nvidia-smi')
    # Get Nvidia-smi Output
    #cmd_out = cmd.readlines()
    #cmd_out = [line.strip() for line in cmd_out]

    with open('sample.txt', 'r') as f:
        cmd_out = f.readlines()
        table = NvidiaTable(cmd_out)
        printer = Printer(table)
        t1, t2 = printer.to_table()
        print(t1)
        print(t2)

