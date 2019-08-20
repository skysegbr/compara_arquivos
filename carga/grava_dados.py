# Grava lista de dicionario no formato:
# [{Nome;idade;e-mail}]

import xlsxwriter


class GravaDados:
    # Grava os dados em arquivo XLSX
    def grava_dados(self, lista, path_nome, cabecalho):
        workbook = xlsxwriter.Workbook(path_nome)
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:A', 20)
        bold = workbook.add_format({'bold': True})
        for col, t in enumerate(cabecalho):
            worksheet.write(0, col, t, bold)
            col += 1


        for idx, val in enumerate(lista):
            worksheet.write(idx + 1, 0, val['nome'])
            worksheet.write(idx + 1, 1, val['idade'])
            worksheet.write(idx + 1, 2, val['email'])

        workbook.close()