# # criar uma receita
# class Receita_de_Bolo():

#     def __init__(self, ovos, mantega, leite, massa):
#         self.ovos = ovos
#         self.mantega = mantega
#         self.leite = leite
#         self.massa = massa
        
#     def get_ovos(self):
#         return self.ovos

#     def set_ovos(self, ovos):
#         self.ovos = ovos
    
#     def get_mantega(self):
#         return self.mantega
    
#     def set_mantega(self, mantega):
#         self.mantega = mantega

#     def get_leite(self):
#         return self.leite

#     def set_leite(self, leite):
#         self.leite = leite

#     def get_massa(self):
#         return self.massa

#     def set_massa(self, massa):
#         self.massa = massa

# lista_de_Sabores = ['Chocolante', 'Morango', 'Laranja', 'Cenora']
    
# sabores = Receita_de_Bolo (lista_de_Sabores, 6,1,2)
 
# print(sabores.get_massa())


# class Bolo_de_Chocolante(Receita_de_Bolo):

#     def __init__(self, forno, temperatura):     
#         self.forno = forno
#         self.temperatura = temperatura

#     def __init__(self, ovos, mantega, leite, massa, recheio):
#         self.ovos = ovos
#         self.mantega = mantega
#         self.leite = leite
#         self.massa = massa
#         self.recheio = recheio

#     def get_recheio(self):
#         print(self.recheio)

# choco = Bolo_de_Chocolante(1,2,3,4,'Chocolante')

# choco.get_recheio()


class Bolo_de_Laranja():

    def __init__(self, ovos, mantega, leite, massa, recheio):
        self.ovos = ovos
        self.mantega = mantega
        self.leite = leite
        self.massa = massa
        self.recheio = recheio


    def get_all(self):
        print("Esse bolo tem {} ovos,{} colheres mantega, {} copos de leite, para massa:{} recheio de {}".format(
            self.ovos, self.mantega, self.leite,  self.massa, self.recheio))


laranjinha = Bolo_de_Laranja(2, 2, 2, 'ovos, mantega e leite','laranja')

laranjinha.get_all()
