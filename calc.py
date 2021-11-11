class Calc :

    def addition (self, num1, num2) :
        
        return str(num1 + num2)

    def subtraction (self, num1, num2) :
        
        return str(num1 - num2)

    def multiplication (self, num1, num2) :

        return str(num1 * num2) 

    def division (self, num1, num2) :

        try :
            return str(num1 / num2)

        except :
            return 'can not divide by 0'


    def opration (self, num1, num2, op) :
        if op == '+' :

            return self.addition(num1, num2)

        elif op == '-' :

            return self.subtraction(num1, num2)

        elif op == '*' :

            return self.multiplication(num1, num2)

        elif op == '/' :

            return self.division(num1, num2)


