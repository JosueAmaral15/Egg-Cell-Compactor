#-*- coding:utf-8 -*-
from math import ceil
class EPIConverter:
    OR = 'v'
    AND = '&'
    INVERT = False
    @staticmethod
    def define_letters_for_integers (n):
        ## We want to turn numbers into strings, and the goal is that we can have variables instead of numbers.
        ## As the numbers will become variables, we have to have a bijective function, that is, in which each number corresponds to a string.
        ## For example:
        ##
        ##    0 : A;
        ##    1 : B;
        ##    9 : J;
        ##    25 : Z;
        ##    26 : AA;
        ##    27 : AB;
        ##    
        ## And so on.
        try:
            n = int (n) ## The number must be an unsigned integer.
            next_value = ceil((n+1)/26) ## We will divide the number until we have all the data.
            current = n % 26 ## This is the first letter of our string.
            string = chr(65 +current) ## Assigning the first letter to the string variable.
            n = next_value ## n variable gets value next_value
            count = 0
            while n > 1: ## Until n variable gets a value equal to or less than one, we will continue processing.
                next_value = ceil((n+1)/26)
                current = (n-2) % 26 ## The next letter will be unraveled
                string = chr(65 +current) + string
                n = next_value
                count+=1
            return string
        except:
            return ''

    @staticmethod
    def get_data():
        data = input("EPI Converter\n\nEnter here the EPI with miniterms separated by commas ('011111-1', '10011-0'...): ")
        return list(map(lambda x: x.strip(), data.replace("'","").split(',')))

    @classmethod
    def convert_EPI(cls, EPI):
        expression = str()
        first = True
        for i in EPI:
            count = 0
            mini_expression = str()
            first_letter = True
            for j in i[::-1] if cls.INVERT else i:
                if j == '1' or j == '0':
                    letter = cls.define_letters_for_integers(count)
                    if j == '0':
                        letter = '~'+letter
                    if not first_letter:
                        mini_expression = '({0}{1}{2})'.format(mini_expression,cls.AND,letter)
                    else:
                        mini_expression = letter
                    if first_letter:
                        first_letter = False
                count+=1
            
            if not first:
                expression = '({0}{1}{2})'.format(expression,cls.OR,mini_expression)
            else:
                expression += mini_expression
            first = False
        return expression
                    
                
       
    @staticmethod
    def run ():
        EPI = EPIConverter.get_data()
        expression = EPIConverter.convert_EPI(EPI)
        print (expression)
        
EPIConverter.run()