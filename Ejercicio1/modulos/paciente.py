
from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

# Riesgo y Descripción
niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']

# Probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self, turno: int, hora):
        
        n = len(nombres)    # Variable auxiliar para asignar el nombre y apellido
        
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__turno = turno
        self.__hora = hora      # Hora de ingreso del Paciente a la Sala de espera
        


    # Métodos Mágicos   

    def __lt__(self, other):
        '''
        Cuando se comparan los Pacientes primero realiza la 
        comparación del riesgo, y si éste es igual, compara 
        el turno del Paciente.

        Parameters
        ----------
        other : class
            Paciente a comparar con el actual.

        Returns
        -------
        bool
            Si el Paciente actual tiene un riesgo más elevado
            que el otro, retorna True.
            Si ambos Pacientes tienen el mismo riesgo, pero
            el actual tiene un turno anterior, retorna True.

        '''
        if self.__riesgo == other.__riesgo:
            return self.__turno < other.__turno
        
        return self.__riesgo < other.__riesgo
    
    
    def __str__(self):
        '''
        Concatena toda la información del Paciente en un
        string y lo retorna.

        Returns
        -------
        cad : str
            String con el Nombre y Apellido del paciente, 
            y su información de ingreso a la sala de espera.

        '''
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        cad += ' - Turno: ' + str(self.__turno)
        cad += ' - ' + str(self.__hora)
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
            Retorna una descripción del nivel de Riesgo del Paciente.

        '''
        return self.__descripcion
    
    @property
    def turno(self):
        '''
        Getter de Turno.

        Returns
        -------
        int
            Retorna el número de Turno del Paciente.

        '''
        return self.__turno
    
    @property
    def hora_ingreso(self):
        '''
        Getter de Hora de Ingreso.

        Returns
        -------
        str
            String de la hora de ingreso del Paciente a la 
            Sala de Espera.

        '''
        return self.__hora