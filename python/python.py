# # Pop remover o ultimo elemento
# minha_lista[1,2,3,4,5]

# remover_ultimo_elemento = minha_lista.pop()

# print(remover_ultimo_elemento)

# # Add

# Orientação Objetos
# Criando classe
# O self é o que? o servir é ultilizado para se referir ao objeto dessa classe, ou seja, utilizado para chamar objeto --> só ultilizar atributos e métodos
# class CuboMagico():
#     # Método construtor
#     def __init__(self, cores, lados):
#         # Está definido um atribundo como chamar esse construtor --> O atribudos cores recebem o valor que estar passando como agrumento do construtor
#         self.cores = cores
#         self.lados = lados

#     # O mpetodo get retornar o valor do atribundo, enquanto os set alterar eles
#     # Métodos get e set cores
#     def get_cores(self):
#         return self.cores
#     def set_cores(self, cores):
#         self.cores = cores
#     # Métodos get e set lados
#     def get_lados(self):
#         return self.lados
#     def set_lados(self, lados):
#         self.lados = lados
    
# # Lista
# lista_de_cores = ['vermelho', 'azul,', 'rosa', 'verde', 'amarelho']
#     #Criando uma estância da classe 
# porco = CuboMagico(lista_de_cores, 6)
# # 
# print(porco.get_cores())

# Como alterar essa cores
# print(porco.set_cores(['marrom', 'cinza', 'preto', 'bege', 'gelo', 'roxo']))
# # Chamando set cores
# print(porco.get_cores())

class Animal():

    def __init__(self, pelo, especie, olhos, patas):
        self.pelo = pelo
        self.especie = especie
        self.olhos = olhos
        self.patas = patas

    def get_all(self):
        print("Esse animal tem {}, tem {} olhos e tem {} patas.".format(self.especie, self.olhos, self.patas))
porco = Animal(True, "Suína", 2,4)