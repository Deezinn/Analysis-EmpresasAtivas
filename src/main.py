import pandas as pd
from empresasAtivas import ExtractExcelEmpresasAtivas

class Main:
    def __init__(self):
        self.empresasAtivasExcel = ExtractExcelEmpresasAtivas()

    def initMain(self):
        self.empresasAtivasExcel.loadAllMethods(self.empresasAtivasExcel)

if __name__ == "__main__":
    main = Main()
    main.initMain()
