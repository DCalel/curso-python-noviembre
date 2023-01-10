# Pruebas automatizadas de tipo unitarias y funcionales
class Calculadora():
    def sumar(self, num1, num2):
        if type(num1) not in [int, float]:
            return "Esto no es un número"
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

# Happy path
# Prueba Unitaria Usando Pytest
def test_calculator_adds_two_numbers():
    # Arrange - Prepararse
    calculadora = Calculadora()

    # Act
    respuesta = calculadora.sumar(5, 3)

    # Assert
    assert respuesta == 8

# Edge case
def test_sumar_fails_if_first_param_is_not_a_number():
    calculadora = Calculadora()
    respuesta = calculadora.sumar("abc", 3)
    assert respuesta == "Esto no es un número"

# TDD - Test Driven Development
def test_calculator_resta_two_numbers():
    calculadora = Calculadora()

    resultado = calculadora.restar(9, 5)

    assert resultado == 4

    resultado = calculadora.restar(10, 3)

    assert resultado == 7