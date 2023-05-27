unidades = [
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
]
dezenas = [
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
]
dezenas_dezenas = [
    "vinte",
    "trinta",
    "quarenta",
    "cinquenta",
    "sessenta",
    "setenta",
    "oitenta",
    "noventa",
]
centenas = [
    "cem",
    "cento",
    "duzentos",
    "trezentos",
    "quatrocentos",
    "quinhentos",
    "seiscentos",
    "setecentos",
    "oitocentos",
    "novecentos",
]


def numero_por_extenso(num: int) -> str:
    if num < 0 or num > 999999:
        return "Número inválido"

    if num == 0:
        return "zero"

    extenso = ""

    if num >= 100000:
        if num == 100_000:
            return "cem mil"
        if num % 100000 == 0:
            return extenso + "mil"
        extenso += centenas[num // 100000] + " e "
        num %= 100000

    if num >= 10000:
        if num >= 20000:
            extenso += dezenas_dezenas[num // 10000 - 2] + " "
        else:
            extenso += dezenas[num % 10] + " "
        num %= 10000
        if num == 0:
            extenso += "mil "
        else:
            extenso += "e "

    if num >= 1000:
        if num // 1000 == 1:
            extenso += "mil "
        else:
            extenso += unidades[num // 1000] + " mil "
        num %= 1000

    if num >= 100:
        extenso += centenas[num // 100] + " "
        num %= 100
        if num == 0:
            return extenso
        else:
            extenso += "e "

    if num >= 10:
        if num >= 20:
            extenso += dezenas_dezenas[num // 10 - 2] + " "
        else:
            extenso += dezenas[num % 10] + " "
        num %= 10

    if num > 0:
        if num == 1 and len(extenso) > 0 and extenso[-1] == "e":
            extenso = extenso
            extenso += "um"
        else:
            extenso += unidades[num]

    return extenso


# Exemplos de uso - escreva seu numero aqui
print(numero_por_extenso(0))
print(numero_por_extenso(123))
print(numero_por_extenso(1050))

print(numero_por_extenso(123_456))
print(numero_por_extenso(100_000))
print(numero_por_extenso(200_000))
print(numero_por_extenso(999_999))
