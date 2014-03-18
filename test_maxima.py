# Tests para la función find_maxima

from maxima import find_maxima


def test1():
    lista = [1, 2, 3, 2, 4, 1]
    resultado_esperado = [2, 4]
    resultado = find_maxima(lista)
    assert resultado == resultado_esperado


def test2():
    lista = [1, 2, 1, 2, 3]
    resultado_esperado = [1, 4]
    resultado = find_maxima(lista)
    assert resultado == resultado_esperado


test1()
test2()
