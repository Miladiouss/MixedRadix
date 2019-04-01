class MixedRadix():
    def __init__(self, value = None, radix = None, digits = None, overflowMethod = 'relaxed', maxRadixLength = 8):
        '''
        value:
            value of number represented as int
        radix:
            a list of radixes (bases) in the traditional increasing direction (right to left)
            if an int is fed, a constant list of length maxRadixLength will be used instead
        digits:
            list of int digits corresponding to radix
        overflowMethod:
            'relaxed': Only as many digits as the length of radix will be computed
            'modular': value will be (value % maxVal)
            'warning': the relaxed method will be imployed while a warning will be printed if value exceeds maxVal
            'halt'   : an error message will be asserted
        maxRadixLength:
            Maximum length of a constant redix
            
        List properties:
            vlaue: See above
            radix: See above
            radixR: Reversed radix
            digits: See above
            digitsR: Reversed digits
            placeValues: list of place values corresponding to each radix
            maxVal: Maximum value that can be represented given the radix
        '''
        self.__val    = value
        if isinstance(radix, int):
            self.__radix  = maxRadixLength * [radix]
        else:
            self.__radix  = radix
        self.__digits = digits
        self.overflowMethod = overflowMethod
    
    
    @property
    def value(self):
        return self.__val
    
    
    @value.setter
    def value(self, intValue):
        assert isinstance(intValue, int), "val must be initiated as int"
        ofm = self.overflowMethod
        
        if ofm is 'relaxed':
            self.__val = intValue
            
        elif ofm is 'modular':
            self.__val = intValue % self.maxVal
            self.numLoops = intValue // self.maxVal
            
        elif ofm is 'warning':
            self.__val = intValue
            if intValue >= self.maxVal:
                print("Warning: value >= maxVal")
                
        elif ofm is 'halt':
            assert intValue < self.maxVal
            
        else:
            raise ValueError("overflowMethod must be: 'relaxed', 'modular', 'warning', 'halt' but '{}' was given".format(ofm))

            
    @property
    def radix(self):
        '''A list of radixes or bases in traditional direction'''
        return self.__radix
    
    
    @radix.setter
    def radix(self, radix):
        '''A list of radixes or bases in traditional direction'''
        assert radix is not None, "radix has not been initiated"
        assert all(isinstance(elem, int) for elem in radix), "radix must be initiated with a list of int's"
        self.__radix = radix
    
    
    @property
    def radixR(self):
        '''A list of radixes or bases in opposite of traditional direction'''
        return self.radix[::-1]
    
    
    @radixR.setter
    def radixR(self, reversedRadix):
        self.radix = reversedRadix[::-1]
        
        
    @property
    def digits(self):
        return self.__computeDigits(abs(self.value), self.radix)
    
    
    @digits.setter
    def digits(self, digits):
        assert len(digits) <= len(self.radix), "Length of digits must be <= length of radix ({} !<= {})".format(len(digits), len(self.radix))
        self.__digits = digits
        self.value = self.__computeValue(digits, self.placeValues)
        
        
    @property
    def digitsR(self):
        return self.digits[::-1]
    
    
    @digitsR.setter
    def digitsR(self, digitsR):
        self.digits = digitsR[::-1]
        
        
    @property
    def sign(self):
        sign = lambda x: x and (1, -1)[x < 0]
        return sign(self.value)
    
    
    @property
    def strSign(self):
        val = self.value
        sign = ' '
        if val > 0:
            sign = '+'
        elif val < 0:
            sign = '-'
            
        return sign
    
    
    @property
    def placeValues(self):
        return self.__computeRadixProduct(self.radix)[1:]
    
    
    @property
    def maxVal(self):
        return self.__computeRadixProduct(self.radix)[0]

    # Operators
    def __add__(self, other):
        val1 = self.value
        radix = self.radix
        if isinstance(other, int):
            val2 = other
        elif isinstance(other, MixRadix):
            val2 = other.value
        
        output = MixRadix(val1 + val2, radix)
        
        return output

    
    def __radd__(self, other):
        return self.__add__(other)

    
    def __sub__(self, other):
        val1 = self.value
        radix = self.radix
        if isinstance(other, int):
            val2 = other
        elif isinstance(other, MixRadix):
            val2 = other.value
        
        output = MixRadix(val1 - val2, radix)
        
        return output
    
    
    def __rsub__(self, other):
        return __sub__(other)
    
    def __mul__(self, other):
        val1 = self.value
        radix = self.radix
        if isinstance(other, int):
            val2 = other
        elif isinstance(other, MixRadix):
            val2 = other.value
        
        output = MixRadix(val1 * val2, radix)
        
        return output
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    
    def __iadd__(self, other):
        val1 = self.value
        radix = self.radix
        if isinstance(other, int):
            val2 = other
        elif isinstance(other, MixRadix):
            val2 = other.value
                
        self.value = val1 + val2
        return self
        
    
    def __repr__(self):
        return self.strSign + str(abs(self.value))
    
    
    def __str__(self):
        return self.__repr__()
    
    
    # Where actual computation happens
    def __computeDigits(self, val, radix):
        assert isinstance(val, int), 'val is not an integer'
        digitsR = []
        radixR  = radix[::-1]
        for i, r in enumerate(radixR):
            digitsR.append(val %  r)
            val = val // r
        return digitsR[::-1]
    
    
    def __computeValue(self, digits, placeValues):
        val = 0
        for i, d in enumerate(digits):
            val += digits[i] * placeValues[i]
        return val
    
    
    def __computeRadixProduct(self, radix):
        pvR = [1]
        radixR = radix[::-1]
        for r in radixR:
            pvR.append(r * pvR[-1])
        return pvR[::-1]
    
if __name__ is '__main__':
    a = MixRadix(-5, [2, 1, 3, 2])
    print('Radix        : {}'.format(a.radix))
    print('Place Values : {}'.format(a.placeValues))
    print('maxVal       : {}'.format(a.maxVal))
    print()
    print('value          digits')
    for i in range(21):
        print('{:7} :  {}{}'.format(str(a), a.strSign, a.digits))
        a += 1
