class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return (self.a + self.b + self.c)

t = Triangulo(3, 4, 5)
print(t.a)
print(t.b)
print(t.c)
print(t.perimetro())
