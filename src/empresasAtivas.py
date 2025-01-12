
import pandas as pd

class ExtractExcelEmpresasAtivas:
    def __init__(self):
        self.dataframe = None

    def extract(self, excel_path):
        try:
            empresasAtivas = pd.read_excel(excel_path, sheet_name=None, engine='openpyxl')
            for excelName, df in empresasAtivas.items():
                # print(f"Planilha: {excelName}")
                # print(df.head(1))
                # print("-" * 50)
                self.dataframe = empresasAtivas
        except Exception as e:
            print(f"Deu algum problema! {e}")

    """
    não é necessário o método 'transform' porque o excel veio transformado da raíz.
    """

    def load(self,path):
        try:
            if self.dataframe:
                for excelName, df in self.dataframe.items():
                    df.to_csv(f"{path}/{excelName}.csv", index=False)
                    print(f"Planilha '{excelName}' salva como {path}")
            else:
                print("Não consegui salvar nenhuma planilha")
        except Exception as e:
            print(f"Deu algum problema: {e}")

    def loadAllMethods(self,object):
        object.extract('/home/deezinn/Documentos/Meus Projetos Pessoais/Analysis-EmpresasAtivas/data/excel original/RECIFE (2531).xlsx')
        object.load('/home/deezinn/Documentos/Meus Projetos Pessoais/Analysis-EmpresasAtivas/data')

