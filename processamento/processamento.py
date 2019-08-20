
# Retorna as diferenças e igualdades entre as listas de dicionarios passados
# Formato: [{Nome;idade;e-mail}]


# Intersecção entre listas de dicionarios
class Interseccao:
    def __init__(self):
        self.item1 = None
        self.item2 = None


    def interseccao(self, item1, item2):
        if item1 is not None and item1 is not None:
            self.item1 = item1
            self.item2 = item2
            
        retorno = [x for x in item2 if x in item1] 
        return retorno


# Diferença entre listas de dicionarios
class Diferenca:
    def __init__(self):
        self.item1 = None
        self.item2 = None


    def diferenca(self, item1, item2):
        if item1 is not None and item1 is not None:
            self.item1 = item1
            self.item2 = item2
            
        retorno = [x for x in item2 if x not in item1] 
        return retorno