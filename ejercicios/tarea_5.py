# crear una clase Empleado que reciba nombre, genero, salario: anual, tipo pago {semanal, mensual, quincenal}
# declares tres empleados y calcules de acuerdo a su tipo salario su pago mensual, semanal o quincenal
class Empleado:
    # sugerencia: Crear metodo init primero
    def __init__(self, tipo_pago: str) -> None:
        self.pago_dict = {"mensual": 12, }

        pass
    def calculo_siguiente_pago():
        numero_pagos = self.pago_dict[self.tipo_pago] # 12, 24 y 52
        return self.salario / numero_pagos
        #devolver calculo
        pass

empleado_1 = Empleado("nombre", "genero", "100000", "mensual")
empleado_2 =
empleado_3 =
print(empleado_1.calculo_siguiente_pago())
print(empleado_2.calculo_siguiente_pago())
print(empleado_3.calculo_siguiente_pago())
