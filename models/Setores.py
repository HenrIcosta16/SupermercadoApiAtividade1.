class Setores():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    
    def toJson(self):
        return {"id": self.id, "nome": self.nome}