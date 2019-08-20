def monta_dicionario(caminho=None):
    with open(caminho, "r") as anexo:
        dic = {}
        for linha in  anexo.readlines()[1:]:
            nomes = linha.split(";")
            dic['nome'] = nomes[0]
            dic['idade'] = nomes[1]
            dic['email'] = nomes[2]

    return dic

if __name__ == '__main__':
    dic = monta_dicionario('./f1.txt')
    print(dic)