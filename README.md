# Descrição

Este repositório tem como objetivo realizar uma análise exploratória detalhada dos dados das empresas ativas na cidade de Recife, verificando possíveis inconsistências ou duplicações nos registros. É importante observar que o campo **"nome fantasia"** não é obrigatório.

## Pontos de Análise

1. **Verificação de Dados Duplicados**
   - Identificar registros duplicados, especialmente nos campos críticos como **CNPJ**, **razão social**, ou **localização**.

2. **Consistência dos Dados**
   - Avaliar a integridade e consistência dos campos, incluindo:
     - Formatos válidos de **CNPJ**.
     - Validação de datas.
     - Preenchimento de campos obrigatórios.

3. **Status das Empresas**
   - Analisar o número total de empresas **ativas** e **inativas**, verificando a consistência do status e dos campos relacionados.

4. **Datas de Abertura e Fechamento**
   - Verificar a coerência das informações:
     - Empresas inativas devem apresentar uma data de fechamento válida.
     - Empresas ativas não devem possuir o campo "data de fechamento" preenchido.

5. **Localização**
   - Explorar as informações de localização, como **bairro**, para identificar registros ausentes ou inconsistentes.

## Ferramentas Utilizadas

A análise será realizada utilizando:
- **Python**: Linguagem principal para análise de dados.
- **Bibliotecas**:
  - **Pandas** e **NumPy** para manipulação e análise de dados.
  - **Matplotlib** (ou similares) para visualização gráfica dos resultados.
- **Jupyter Notebook**: Ambiente interativo para desenvolvimento e documentação do processo de análise.

## Objetivo Final

Fornecer insights úteis para garantir a qualidade dos dados e auxiliar na tomada de decisões estratégicas relacionadas às empresas ativas na cidade de Recife.
