import re

def validar_rut(rut):
    # Eliminar espacios en blanco y convertir todo a minúsculas para asegurar que no haya errores
    rut = rut.strip().lower()

    # Expresión regular para validar el formato del RUT (8 dígitos seguidos de un guion y un dígito verificador)
    rut_pattern = re.compile(r'^\d{7,8}-[0-9kK]$')
    if not rut_pattern.match(rut):
        return False

    # Separar el cuerpo del RUT y el dígito verificador
    rut_cuerpo, dv = rut.split('-')

    # Calcular el dígito verificador
    total = 0
    factor = 2
    for digit in reversed(rut_cuerpo):
        total += int(digit) * factor
        factor = 9 if factor == 2 else factor - 1

    # Calcular el dígito verificador de acuerdo al total
    resto = total % 11
    calculo_dv = 11 - resto
    if calculo_dv == 11:
        calculo_dv = '0'
    elif calculo_dv == 10:
        calculo_dv = 'k'

    # Comparar el dígito verificador calculado con el ingresado
    return dv == str(calculo_dv)