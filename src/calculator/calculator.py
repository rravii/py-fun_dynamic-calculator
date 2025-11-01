# Mapping single-digit numbers in multiple languages
NUMBER_WORDS = {
    # English
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    # German
    "null": 0, "eins": 1, "zwei": 2, "drei": 3, "vier": 4,
    "fünf": 5, "sechs": 6, "sieben": 7, "acht": 8, "neun": 9,
    # Spanish
    "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4,
    "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
    # Russian
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4,
    "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
    # Chinese
    "零": 0, "一": 1, "二": 2, "三": 3, "四": 4,
    "五": 5, "六": 6, "七": 7, "八": 8, "九": 9
}

# Roman numerals
ROMAN_NUMERALS = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
    "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10
}

# Helper function to parse numbers
def parse_number(x):
    if isinstance(x, (int, float)):
        return x
    x = str(x).strip()  # <-- remove leading/trailing spaces
    try:
         # check if integer
        if '.' not in x and 'e' not in x and 'E' not in x:
            return int(x)
        else:
            return float(x)
    except ValueError:
        pass
    x_lower = str(x).lower()
    if x_lower in NUMBER_WORDS:
        return NUMBER_WORDS[x_lower]
    if x in ROMAN_NUMERALS:
        return ROMAN_NUMERALS[x]
    raise ValueError(f"Cannot parse '{x}' as a number")

# Calculator class
class Calculator:
    def add(self, a, b):
        return parse_number(a) + parse_number(b)

    def sub(self, a, b):
        return parse_number(a) - parse_number(b)

    def mul(self, a, b):
        return parse_number(a) * parse_number(b)

    def div(self, a, b):
        b_val = parse_number(b)
        if b_val == 0:
            return "Cannot divide by zero"
        return parse_number(a) / b_val

    def factorize(self, n):
        n = int(parse_number(n))
        factors = []
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1
            if divisor * divisor > n:
                if n > 1:
                    factors.append(n)
                break
        return factors
