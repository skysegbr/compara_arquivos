# Carega arquivo e separa as linha e colunas em  dicionario no formato:
# {Nome;idade;e-mail}
# retorna uma lista contendo: [{Nome;idade;e-mail}]  


# Carga de arqauivo em dicionario em lista 
class Carga:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.email = None
        self.entrada_dic = {}
        self.lista_dic = []

    def carrega(self, path_nome, delimitador):
        try:
            with open(path_nome, 'r') as arquivo:
                for linha in arquivo:
                    self.entrada_dic ={}
                    dados = linha.split(delimitador)
                    self.entrada_dic['nome'] = dados[0].strip('\n')
                    self.entrada_dic['idade'] = dados[1].strip('\n')
                    self.entrada_dic['email'] = dados[2].strip('\n')
                    self.lista_dic.append(self.entrada_dic)
        except Exception as e:
            print("Carga - Erroa ao abrir arquivos ", e)
            return None

        return self.lista_dic