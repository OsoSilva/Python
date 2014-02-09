# def verifica(self):
#     edoActual = self.inicial
#     for caracter in self.cadena:
#         for elemento in self.fTransicion:
#             if (edoActual == elemento[0]) and (caracter == elemento[1]):
#                 edoActual = self.fTransicion[(edoActual,caracter)]
#                 print edoActual
#                 break
#     if edoActual in self.aceptacion:
#         return True
#     return False

class Automata(object):
    """Verifica si un numero binario es multiplo de 5"""
    #Atributos:
    estados     = {'0','01','10','11','100'}
    alfabeto    = {'0','1'}
    inicial     = '0'
    aceptacion  = {'0'}
    fTransicion = { ('0','0')   :   '0',
                    ('0','1')   :   '1',
                    ('1','0')   :   '10',
                    ('1','1')   :   '11',
                    ('10','0')  :   '100',
                    ('10','1')  :   '0',
                    ('11','0')  :   '1',
                    ('11','1')  :   '10',
                    ('100','0') :   '11',
                    ('100','1') :   '100'}
    edoActual = inicial

    def __init__(self, cadena):
        super(Automata, self).__init__()
        self.cadena = cadena

    def esValida(self):
        if self.edoActual in self.aceptacion:
            return True
        return False

    def mover(self):
        for caracter in self.cadena:
            for elemento in self.fTransicion:
                if (self.edoActual == elemento[0]) and (caracter == elemento[1]):
                    self.edoActual = self.fTransicion[(self.edoActual,caracter)]
                    #print self.edoActual
                    break
                
    def verifica(self):
        self.mover()
        return self.esValida()

a = Automata(raw_input("Cadena> "))
if a.verifica():
    print "Cadena aceptada"
else:
    print "Cadena no aceptada"
        
