class Personaje:
    def __init__(self, nombre, nivel=1, experiencia=0): ## el nombre lo define el usuario, la experiencia parte en 0 y nivel 1
        self.nombre = nombre
        self.nivel = nivel
        self.experiencia = experiencia

    @property  ##permite consultar el estado
    def estado(self):
        return f"El nombre es: {self.nombre}, su nivel es: {self.nivel} y su experiencia es: {self.experiencia}"

    @estado.setter ##permite reasignar experiencias positivas o negativas ya que en fx de estas subes o bajas de nivel
    def estado(self,exp): ##Positiva: suma y sube nivel cada vez que supere múltiplos de 100; Negativa: resta y baja nivel si la experiencia queda negativa
        total_exp = self.experiencia + exp

        while total_exp >= 100: ##para subir de experiencias
            self.nivel += 1
            total_exp -= 100
        
        while total_exp < 0 and self.nivel > 1: ## para bajar de experiencias
            self.nivel -=1
            total_exp += 100

        if self.nivel == 1 and total_exp < 0:
            total_exp = 0

        self.experiencia = total_exp 
               
    def __lt__(self, orco): ##sobrecarga para método menor que
        return self.nivel < orco.nivel
    
    def __gt__(self, orco): ##sobrecarga para método mayor que
        return self.nivel > orco.nivel
    
    def __eq__(self, orco): ##sobrecarga para método igual que
        return self.nivel == orco.nivel

    ##Si el jugador es menor al orco, tiene un 33% de probabilidades de ganar.
    ##Si el jugador es mayor al orco, tiene un 66% de probabilidades de ganar.
    ##Si el jugador es igual al orco, tiene un 50% de probabilidades de ganar.

##por lo tanto para calcular la probabilidad es

    def probabilidad(self, orco):
        if self > orco:
            return 0.66
        elif self < orco:
            return 0.33
        else:
            return 0.5
    @staticmethod
    def dialogo(probabilidad):
        return int(input(f"""
¡Oh no!, ¡Ha aparecido un Orco!
Con tu nivel actual, tienes {probabilidad *100:.1f}% de probabilidades de ganarle al Orco.
Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.
¿Qué deseas hacer?
1. Atacar
2. Huir: """))