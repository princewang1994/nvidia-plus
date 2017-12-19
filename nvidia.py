from utils import get_user_from_pid
import terminaltables
import re

gpu_line_re = re.compile(r'\|\s*(\d*)%.*P\d\s*(\d*)W / (\d*)W.*\|\s*(\d*)MiB / (\d*)MiB.*\|\s*(\d*)%.*')
user_line_re = re.compile(r'\|\s*(\d*)\s*(\d*)\s*(\w)\s*(\S*)\s*(\d*)MiB.*')

class GPULine(object):

    def __init__(self, GPU_id, GPU_Fan, use_W, tot_W, use_mem, tot_mem, volatile):
        self.GPU_id = GPU_id
        self.GPU_Fan = int(GPU_Fan)
        self.use_W = int(use_W)
        self.tot_W = int(tot_W)
        self.use_mem = int(use_mem)
        self.tot_mem = int(tot_mem)
        self.volatile = int(volatile)

    def to_table(self):
        return [
            self.GPU_id,
            '%d%%' % self.GPU_Fan,
            '%3dW / %3dW' % (self.use_W, self.tot_W),
            '%5dMiB / %5dMiB' % (self.use_mem, self.tot_mem),
            '%2d%%' % self.volatile,
        ]

class UsageLine(object):

    def __init__(self, GPU_id, pid, type, process_name, mem_usage):
        self.GPU_id = int(GPU_id)
        self.pid = int(pid)
        self.type = type
        self.process_name = process_name
        self.mem_usage = int(mem_usage)

    def crop_cmd(self, cmd):
        if len(cmd) < 10:
            return cmd
        else:
            return cmd.split('/')[-1]

    def to_table(self):

        return [
            self.GPU_id,
            self.pid,
            get_user_from_pid(self.pid),
            self.type,
            self.crop_cmd(self.process_name),
            '%dMiB' % self.mem_usage
        ]

class NvidiaTable(object):

    def __init__(self, cmd_out_lines):

        self.lines = cmd_out_lines
        self.gpu_lines = []
        self.usage_lines = []

        gpu_id = 0
        for line in cmd_out_lines:
            res = re.findall(gpu_line_re, line)
            if res:
                gpu_line = GPULine(gpu_id, *res[0])
                self.gpu_lines.append(gpu_line)
                gpu_id += 1
                continue

            res = re.findall(user_line_re, line)
            if res:
                use_line = UsageLine(*res[0])
                self.usage_lines.append(use_line)

        self.gpu_head = [['GPU\nID', 'GPU\nFan', 'Persistence', 'Memory-Usage', 'Volatile']]
        self.usage_head = [['GPU', 'PID', 'User', 'Type', 'Process', 'Menmory']]

