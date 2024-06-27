class Term:

    def __init__(self, coeff, power) -> None:
        self.coefficient = coeff
        self.power = power

class Polynomial:

    def __init__(self) -> None:
        self.terms = []

    def addTerm(self, coeff, power):
        term = Term(coeff, power)
        self.terms.append(term)

    def getDegree(self):
        degree = 0
        for term in self.terms:

            degree = max(degree, term.power)

        return degree
    
    def getCoefficient(self, power):
        for term in self.terms:
            if power == term.power:
                return term.coefficient
        return "Coefficient not found"

    def evauluate(self, value):
        result = 0
        for term in self.terms:
            result += term.coefficient * ((value) ** term.power)
        return result
  
    def __add__(self, other):
        result = ''
        result = []
        for i in range(len(self.terms)):
            for term in other.terms:
                t = self.terms[i]
                if t.power == term.power:
                    pass

    # def derivative(self):
    #     self.der = []
    #     for term in self.terms:
            
    #         d = f'{term.coefficient * term.power}x^{term.power-1}'

    def setCoefficient(self, newCoefficient, power):
        for i in range(len(self.terms)):
            term = self.terms[i]
            if term.power == power:
                term.coefficient = newCoefficient
        return "Set"

    def clear(self):
        for i in range(len(self.terms)):
            term = self.terms[i]
            term.coefficient = 0
        return "Cleared"
    
    def derivative(self):
        new_terms=[]
        for i in range(len(self.terms)):
            z=self.terms[i].coefficient*self.terms[i].power
            powerr=self.terms[i].power-1

            new=Term(z,powerr)
            new_terms.append(new)
    
    def __str__(self) -> str:
        s = ''
        for i in range(len(self.terms)):
            term = self.terms[i]
            if term.power == 0:
                s += str(term.coefficient)
            elif term.power == 1:
                s += f'{term.coefficient}x'
            elif i == len(self.terms)-1:
                s += f'{term.coefficient}x^{term.power} '
            else:
                s += f'{term.coefficient}x^{term.power} + ' 
        return s
    
p1 = Polynomial()
p1.addTerm(4, 5)
p1.addTerm(7, 3)
p1.addTerm(-1, 2)
p1.addTerm(9, 0)
print("p1", p1)
p2 = Polynomial()
p2.addTerm(6,4)
p2.addTerm(3,2)
p2.addTerm(2,1)
print(p2)

print(p2.getDegree())
print(p2.getCoefficient(2))
print(p2.evauluate(1))
print(p1.__add__(p2))
print(p1.derivative())