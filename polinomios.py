class Polinomio:
    """Clase Polinomio"""
    def __init__(self,pol=[]):
        """Constructor: Recibe una lista como parametros,
        la cual sera el polinomio. La posicion 0 corresponde al grado
        cero y la ultima posicion al grado enesimo"""
        pol.reverse() #Invertimos la lista
        self.pol = pol

    def __str__(self):
        """Muestra el polinomio actual"""
        p = ""
        for i in range(len(self.pol)-1,-1,-1):
            if (self.pol[i]>0) and (i==len(self.pol)-1):
                p+= str(self.pol[i])+"x^"+str(i)
            elif (i==0) and (self.pol[i]>0):
                p+= "+"+str(self.pol[i])
            elif (i==0) and (self.pol[i]<0):
                p+= str(self.pol[i])
            elif (self.pol[i]>0):
                p+= "+"+str(self.pol[i])+"x^"+str(i)
            else:
                p += str(self.pol[i])+"x^"+str(i)
        return p

    def igualA(self,polinomio):
        """Recibe como parametro otro polinomio, y
        lo compara con el actual, si es igual regresa
        un valor de True, si son diferentes regresa el valor
        de False"""
        #Si son del mismo grado, podrian ser iguales
        if (self.grado==polinomio.grado):
            bandera = True  #Se supone que son iguales, hasta que
                            #se demuestre lo contrario
            for a,b in zip(self.pol,polinomio.coeficientes):
                #Si a es distinto que b, no son iguales
                if a!=b:
                    return False
                elif a==b:
                    bandera = True
            return bandera
                    
        else:
            return False

    @property
    def coeficientes(self):
        return self.pol

    @property
    def grado(self):
        """Regresa el grado de el polinomio"""
        return len(self.pol)-1
        
        
        
p = Polinomio([-3,2,3,4])
print "Polinomio A ingresado: "
print p
print "Grado:",p.grado
print "Coeficientes:",p.coeficientes
q = Polinomio([-3,2,3,0])
print " "
print "Polinomio B ingresado: "
print q
print "Grado:",q.grado
print "Coeficientes:",q.coeficientes
print "Iguales[?]:",p.igualA(q)
