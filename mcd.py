def mcd(num1: int, num2: int) -> int:
    bigNumber = max(num1, num2)
    minNumber = min(num1, num2)
    while minNumber != 0:
        i = bigNumber // minNumber
        tempNum = bigNumber - i*minNumber
        print(f'{bigNumber} = {i} * {minNumber} + {tempNum}')
        bigNumber, minNumber = minNumber, tempNum
    return bigNumber


print(mcd(1547, 560))
