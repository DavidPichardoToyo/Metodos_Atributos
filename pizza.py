from ingredientes import ingredientes

class Pizza:

    # atributos de clase
    precio = 10000
    tamaño = "Familiar"

    # Requerimiento punto 2
    @staticmethod
    def validar(elemento:str, valores:list[str]):
        return True if elemento in valores else False

        # Requerimiento punto 3
    def realizar_pedido(self):
        self.proteina = input("Elige una proteina (Carne / Pollo / Carne Vegetal) : ").lower()
        self.vegetal1 = input("Elige un vegetal (tomate / aceituna / champiñones) : ").lower()
        self.vegetal2 = input("Elige otro vegetal (tomate / aceituna / champiñones) :").lower()
        self.masa = input("Elige tipo de masa (tradicional / delgada) :").lower()

        ingredientes_vegetales = [self.vegetal1, self.vegetal2]

        valido_proteina = Pizza.validar(self.proteina, ingredientes["proteinas"])
        valido_vegetal1 = Pizza.validar(self.vegetal1, ingredientes["vegetales"])
        valido_vegetal2 = Pizza.validar(self.vegetal2, ingredientes["vegetales"])
        valido_masa = Pizza.validar(self.masa, ingredientes["masa"])

        self.valida = valido_proteina and valido_vegetal1 and valido_vegetal2 and valido_masa

        print("Resumen del pedido : ")
        print("Proteína :", self.proteina)
        print("Vegetales :", ingredientes_vegetales)
        print("Masa : ", self.masa)
        print("¿Es una pizza válida? : ", self.valida)