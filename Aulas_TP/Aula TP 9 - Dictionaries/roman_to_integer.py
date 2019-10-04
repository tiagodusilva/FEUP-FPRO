def roman_to_integer(astring):
    roman = {" ": 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    astring += " "
    result = 0
    for i in range(len(astring) - 1):
        if roman[astring[i + 1]] > roman[astring[i]]:
            result -= roman[astring[i]]
        else:
            result += roman[astring[i]]
    return result


#print(roman_to_integer('LXXXIV'))
#print(roman_to_integer('XLIII'))
#print(roman_to_integer('MMMCMXCIX'))
