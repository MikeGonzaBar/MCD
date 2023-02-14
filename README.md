# MCD

This code implements the Euclidean Algorithm to find the Greatest Common Divisor (GCD) of two integer numbers.

## Function Signature
  
    def mcd(num1: int, num2: int) -> int:

## Inputs

- __num1__: an integer number to calculate the GCD.
- __num2__ : an integer number to calculate the GCD.

## Outputs

- __int__: The GCD of the input numbers.

## Algorithm

1. Define the biggest number as __bigNumber__ and the smallest number as __minNumber__.
2. Repeat the following until __minNumber__ is equal to zero:
    1. Calculate the maximum number of __minNumber__ that can be subtracted from __bigNumber__ using integer division.
    2. Calculate the remainder __tempNum__ by subtracting i *__minNumber__ from __bigNumber__.
    3. Print the equation __bigNumber__ = i* __minNumber__ + __tempNum__.
    4. Set __bigNumber__ to __minNumber__ and __minNumber__ to __tempNum__.
3. Return __bigNumber__ as the GCD of the input numbers.

## Example Usage

    print(mcd(1547,560))

Output:

    560 = 2 *154 + 98
    154 = 1* 98 + 56
    98 = 1 *56 + 42
    56 = 1* 42 + 14
    42 = 3 * 14 + 0
    14
