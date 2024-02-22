class Empleado :
    #codigo para determinar la clase del empleado
        ''''-----------------
        #atributos
        -------------------'''
        nombre=""
        apellido=""
        """"-------------------------
        #masculino 1 y femenino 2
        -------------------------"""
        sexo=""
        salario=1000000
        '''''--------------------
        #metodos
        ------------------'''
        def CambiarSalario(self, nuevoSalario):
          #aqui va el codigo del metodo
         return 0
    
        def CambiarEmpleado(self, nNombre, nApellido, nSexo, NsSalario):  
           #aqui va el codigo del nuevo empleado
         return None            
        
        def ConsultarSalario(self):
           #aqui va el codigo del metodo
         return self.salario 

        def ConsultarNombre(self):
         return self.nombre

        def ConsultarApellido(self):
          return self.apellido

        def ConsultarNombreCompleto(self):
          return self.nombre +" "+ self.apellido
        
        def AumentoSalarial(self):
          nSalario = self.salario * 0.05
          nSalario = nSalario + self.salario
          self.salario= nSalario
          return " el nuevo salario es de: "+self.salario