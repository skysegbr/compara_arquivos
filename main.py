# Busca linhas repetidas e diferentes entre 2 arquivos no formato: 
# Nome;idade;e-mail
# grava os resultados em arquivos 


import itertools
from carga import carga, grava_dados
from processamento import processamento


# Parametrização da carga
a1 = carga.Carga()
a2 = carga.Carga()
g =  grava_dados.GravaDados()
lista1 = a1.carrega('f1.txt', ';')
lista2 = a2.carrega('f2.txt', ';')
       
# Main
if __name__ == "__main__":
   
    interseccao = processamento.Interseccao()

    r_igualdade = interseccao.interseccao(lista1, lista2)
    print(r_igualdade, '\n')

    diferenca = processamento.Diferenca()

    r_diferenca = diferenca.diferenca(lista1, lista2)
    print(r_diferenca)

    cabecalho = ['NOME', 'IDADE', 'E-MAIL']
    

    g.grava_dados(r_igualdade, 'igualdade.xlsx', cabecalho)
    g.grava_dados(r_diferenca, 'diferenca.xlsx', cabecalho)