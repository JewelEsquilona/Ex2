#1

def operations(a, b):

    print("Addition:", a + b)

    print("Subtraction:", a - b)

    print("Multiplication:", a * b)

    print("Division:", a / b if b != 0 else "Undefined (division by zero)")

    print("Modulus:", a % b if b != 0 else "Undefined (division by zero)")

    print("Exponent:", a ** b)


def modulus_of_complex(complex_number):

    return (complex_number.real**2 + complex_number.imag**2) ** 0.5

 

int1, int2 = 10, 5

float1, float2 = 10.5, 2.5

complex1, complex2 = 1 + 2j, 2 + 3j


print("Integer:")

operations(int1, int2)


print("\nFloat:")

operations(float1, float2)


print("\nComplex Numbers:")

print("Addition:", complex1 + complex2)

print("Subtraction:", complex1 - complex2)

print("Multiplication:", complex1 * complex2)

print("Division:", complex1 / complex2 if complex2 != 0 else "Undefined (division by zero)")

print("Modulus of first complex number:", modulus_of_complex(complex1))

print("Modulus of second complex number:", modulus_of_complex(complex2))

print("Exponent:", complex1 ** 2)


#2

numwith = 25_000_000

numwithout = 25000000


print(numwith)

print(numwithout)


#3

int_var = 10

float_var = 10.5

complex_var = 1 + 2j


print(type(int_var))

print(type(float_var))

print(type(complex_var))