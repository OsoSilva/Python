#!/bin/python
# -*- encoding: utf-8 -*-

class AFD(object):
    """Clase que genera los 5 elementos de una AFD, a partir
    de un archivo proporcionado por el usuario."""
    #Variables usadas durante la lectura del Automata
    flag = False        #Bandera que indica comentarios
    sigmaFlag = False   #Bandera que indica definicion del alfabeto
    endFlag = False     #Bandera que indica final de una definicion
    stateFlag = False   #Bandera que inidica inicio de la definicion de un estado
    currentState = ""   #Guarda el estado actual

    #Elementos del Automata Finito Deterministico
    @property
    def sigma(self):
        """Regresa el Alfabeto"""
        return self.__sigma
    @property
    def initialS(self):
        """Regresa el nombre del estado inicial"""
        return self.__initial
    @property
    def finalSts(self):
        """Regresa el conjunto de estados finales"""
        return self.__final
    @property
    def delta(self):
        """Regresa la f de trancision"""
        return self.__transition
    @property
    def states(self):
        """Regresa todos los estados del automata"""
        return self.__states

    #Variables que se usaran durante la ejecucion del Automata

    #Metodos privados
    
    def __init__(self,myFile):
        """Constructor: Requiere de un archivo fuente"""
        super(AFD, self).__init__()
	#Archivo de donde se leera el AFD
        self.myFile = myFile
        self.nStates = 0        #Numero de estados
        self.__sigma = []       #Alfabeto
        self.__initial = ""     #Estado inicial
        self.__final = []       #Estados finales
        self.__states = []      #Todos los estados
        self.__transition = {}  #F de transicion
        self.string =  ""

    def __alphabet(self,sigma):
        """Metodo privado que asigna el alfabeto (sigma)"""
        self.__sigma += sigma

    def __comments(self,l):
        """Metodo que analiza los comentarios"""
        #Si encontramos un comentario simple, no hace nada
        if (l[0]=="#"):
            pass
        elif(l[0]==":-"):
            #Si hay un comentario que abre se enciende la
            #bandera de comentarios
            self.flag = True
        elif(l[0]=="-:"):
            #Si hay comentario que cierra, se apaga la
            #bandera de comentarios
            self.flag = False
        elif self.flag:
            pass

    def __state(self,l):
        #print l
        if len(l)!=1 and l[0]=="state":
            self.__states.append(l[1])
            self.currentState = l[1]
        elif l[0]=="set":
            if l[1]=="initial":
                self.__initial = self.currentState
            elif l[1]=="final":
                self.__final.append(self.currentState)
        elif l[0]=="goto":
            #print l[1],l[2]
            self.__transition[(self.currentState,l[2])] = l[1]
            
    def __parser(self,l):
        """Funcion que analiza el automata desde el archivo,
            recibe una lista con las instrucciones a analizar (l)"""
        #Si no son comentarios se analiza la "instruccion"
        if (l[0]=="end"):
            #Si hay un cierre de definicion, prendemos la bandera
            self.endFlag = True
            if(self.stateFlag):
                self.stateFlag = False
            if(self.sigmaFlag):
                self.sigmaFlag = False
            #print "END"
        elif self.sigmaFlag:
            #Si esta encendida la bandera del alfabeto
            #se guarda el alfabeto
            if(not self.endFlag):
                #Si no esta encedida la bandera de fin de definicion
                #guarda el alfabeto
                self.__alphabet(l)
            else:
                #Apagamos la bandera del alfabeto
                self.sigmaFlag = False
                pass
        elif self.stateFlag:
            #Si esta encendida la bandera de estados, analizamos
            #lo que hay dentro
            self.__state(l)
        elif(l[0]=="state"):
            self.nStates+=1
            #print "Estado encontrado: "+str(l[1])
            #Apagamos la bandera de END
            self.endFlag = False
            #Prendemos bandera de Estados
            self.stateFlag = True 
            #Hacer algo con los estados
            self.__state(l)
        elif(l[0]=="alphabet"):
            #print "Alfabeto"
            self.sigmaFlag = True
            #Apagamos la bandera de END
            self.endFlag = False

    #Metodos publicos
            
    def status(self):
        """Muestra como esta asignado el Automata"""
        print "Existen "+str(self.nStates)+" estados"
        print "Alfabeto: " + str(self.sigma)
        print "Estado inicial: "+str(self.initialS)
        print "Estados finales: "+str(self.finalSts)
        print "Estados: "+str(self.states)
        print "Funcion: "
        print "Estado | Valor | Estado siguiente "
        print ""
        for state,value in self.delta:
            print state,"\t",value,"\t",self.delta[(state,value)]

    def readAFD(self):
        """Se analiza el archivo (parser)"""
        #Abrimos el archivo
        f = open(self.myFile,'r')
        #Leemos las lineas
        lines = f.readlines()
        for line in lines:
            line.strip()    #Eliminamos los espacios en blanco
            line.strip("\r\n")#Eliminamos los retornos de linea
            l = line.split() #Separamos la linea
            if (len(l)!=0):
                if (l[0]==":-" or l[0]=="#" or self.flag):
                    #Si hay un comentario o esta encendida la bandera
                    #de comentarios
                    self.__comments(l)
                else:
                    #Si no es comentario se analiza la definicion de
                    #estado o alfabeto
                    self.__parser(l)

    def readString(self,string):
        """Metodo que almacena la cadena a analizar"""
        self.string = string

    def isCorrect(self):
        """Regresa true si la cadena es valida, en caso contrario +
            False"""
        if self.cState in self.finalSts:
            return True
        return False

    def mv(self):
        """Metodo que mueve al automata en los estados"""
        self.cState = self.initialS    #Estado actual
        for char in self.string:
            for element in self.delta:
                #print self.cState
                if (self.cState == element[0]) and (char == element[1]):
                    self.cState = self.delta[(self.cState,char)]
                    break
                
    def verify(self):
        """Verifica si un automata es correcto"""
        self.mv()
        return self.isCorrect()


def main():
    flag = True
    #Cargar el automata
    #a = AFD('ejemplo.zafd')
    f = raw_input("Nombre del archivo: ")
    while flag:
        try:
            a = AFD(f)
            #Leemos el Automata
            a.readAFD()
            #Mostramos el Automata
            a.status()
            #Ingresamos una Cadena
            a.readString(raw_input("Ingrese una cadena> "))
            if a.verify():
                print "[+] Cadena aceptada"
            else:
                print "[-] Cadena no aceptada"
            flag = raw_input("Ingresar otra cadena[?] S/N: ")
            if(flag.lower()!="s"):
                flag = not True
                print "!Bye ;)!"
        except:
            print "[!] Archivo '",str(f),"' no encontrado"
            flag =  not flag


if __name__=="__main__":
    main()
