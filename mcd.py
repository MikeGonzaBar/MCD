def mcd(num1: int, num2: int)->int:
  bigNumber = num1 if num1>num2 else num2
  minNumber = num2 if num1>num2 else num1
  while(True):
    i = 1
    while(True):
      i += 1
      if(i*minNumber > bigNumber):
        i-=1
        break
      else:
        continue
    tempNum = bigNumber - (i*minNumber)
    print(f'{bigNumber} = {i} * {minNumber} + {tempNum}')
    bigNumber = minNumber
    minNumber = tempNum
    if(minNumber == 0):
      break
    else:
      continue
  return bigNumber

print(mcd(1547,560))