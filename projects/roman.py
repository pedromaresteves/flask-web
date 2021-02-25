def convert_to_roman(num):
    result = {'value': '', 'validInput': False}
    resultMaker = ''
    poops = {
    "M":1000,
    "CM":900,
    "D":500,
    "CD":400,
    "C":100,
    "XC":90,
    "L":50,
    "XL":40,
    "X":10,
    "IX":9,
    "V":5,
    "IV":4,
    "I":1
    }
    try:
        if num <= 0:
            return result
        for item in poops:
            while(num >= poops[item]):
                result['value'] += item
                num = num - poops[item]
    except:
        return result
    result['validInput'] = True
    return result