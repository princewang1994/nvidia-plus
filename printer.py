from terminaltables import AsciiTable, SingleTable


class Printer(object):

    def __init__(self, table, table_style=AsciiTable):

        self.table = table

        self.gpu_table = [gpu_line.to_table() for gpu_line in table.gpu_lines]
        self.gpu_table = table_style(table.gpu_head + self.gpu_table)

        self.usage_table = [usage_line.to_table() for usage_line in table.usage_lines]
        self.usage_table = table_style(table.usage_head + self.usage_table)

        self.config_gpu_table()
        self.config_usage_table()

    def config_gpu_table(self):
        self.gpu_table.justify_columns = {
            0: 'left', 1: 'center', 2: 'center',
            3: 'center', 4: 'right'
        }
        self.gpu_table.title = 'NVIDIA-PLUS'
        self.gpu_table.inner_row_border = True

    def config_usage_table(self):
        self.usage_table.justify_columns = {
            0: 'left', 1: 'right', 2: 'center',
            3: 'center', 4: 'left', 5: 'right'
        }
        self.usage_table.padding_left = 2

    def to_table(self):

        return self.gpu_table.table, self.usage_table.table




        #gpu_table.padding_left = 4


        return gpu_table.table, usage_table.table