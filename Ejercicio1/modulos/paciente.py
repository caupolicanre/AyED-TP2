
from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']

# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self, turno):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__turno = turno


    # Métodos Mágicos   

    def __lt__(self, other):
        if self.__riesgo == other.__riesgo:
            return self.__turno < other.__turno
        return self.__riesgo < other.__riesgo
    
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        cad += ' - Turno: ' + str(self.__turno)
        return cad
        
        
    # Properties
    
    @property
    def nombre(self):
        '''
        Getter de Nombre.

        Returns
        -------
        str
            Retorna el nombre del Paciente.

        '''
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre: str):
        '''
        Setter de Nombre.

        Parameters
        ----------
        nuevoNombre : str
            Nombre que va a reemplazar el antiguo Nombre del Paciente.

        Returns
        -------
        None.

        '''
        self.__nombre = nuevoNombre
    
    @property
    def apellido(self):
        '''
        Getter de Apellido.

        Returns
        -------
        str
            Retorna el apellido del Paciente.

        '''
        return self.__apellido
    
    @apellido.setter
    def apellido(self, nuevoApellido: str):
        '''
        Setter de Apellido.

        Parameters
        ----------
        nuevoApellido : str
            Apellido que va a reemplazar el antiguo Apellido del Paciente.

        Returns
        -------
        None.

        '''
        self.__apellido = nuevoApellido
    
    @property
    def riesgo(self):
        '''
        Getter de Riesgo.

        Returns
        -------
        int
            Retorna el valor de Riesgo del Paciente.

        '''
        return self.__riesgo
    
    @property
    def descripcion_riesgo(self):
        '''
        Getter de la Descripción de Riesgo.

        Returns
        -------
        str
            Retorna una descripción del nivel de Riesgo.

        '''
        return self.__descripcion
    