from .DictionaryNumOper import thousands, numbers_till_hundred, operations
import re

class HumanCalc:
    def convert(self, string): 
        string_normal = self._prepare_string(string) # prepare for split
        split = string_normal.split()
        # check string length
        if len(split) % 2 != 1 or len(split) < 0:
            return 'invalid input'
            # the following code will not be called
            raise TypeError("Please make sure the expression is correct")
        
        expression = []

        try:
            if len(split) != 1:
                for k in range((len(split)-1)//2):
                    expression.append(num_to_text(split[k*2]))
                    expression.append(ope_to_text(split[k*2 + 1]))
                else:
                    expression.append(num_to_text(split[k*2 + 2]))
            else:
                expression.append(num_to_text(split[0]))
        except:
            return 'invalid input'
            # the following code will not be called
            raise TypeError("Please make sure the expression is correct")

        return ' '.join(expression)
    
    @staticmethod
    def _prepare_string(string):
        ''' normalise the string, remove abundant spaces while adding space when missing,
            prepare to split
                '3243 +3423   - 342= 23'
            to
                '3243 + 3423 - 342 = 23'
        '''
        pattern = r'\s*([\*\+\-\=\/])\s*'
        return re.sub(pattern, r' \g<1> ', string)
    

def ope_to_text(operation):
    return operations[operation]

def num_to_text(number):
    '''the number is separated into blocks 
        3 digits each with names
            5,389,276,538
        block names
            b,mil,tho,
        and 3 digit numbers are being converted to a string
    '''
    number = int(number)
    if number == 0:
        return numbers_till_hundred[0]
    
    split = []
    thousands_it = iter(thousands)
    while number:
        reminder = number % 10**3
        thousands_block = next(thousands_it)
        if reminder == 0:
            number = (number - 0) / 10**3
            # there was a huge bug: unreachable code, continue was before number change
            continue # we don't mention anything if 3 digit block is missing
        if reminder == 1:
            # we get rid of 's' at the end
            split.insert(0, (_3digit_to_text(reminder), thousands_block[:-1]))
            number = (number - 1) / 10**3
            continue
        # general case
        split.insert(0, (_3digit_to_text(reminder), thousands_block))
        number = (number - reminder) / 10**3

    return ' '.join([item for tupl in split for item in tupl if item != ''])

def _3digit_to_text(number):
    txtnum = []
    number = int(number)
    if number == 0:
        return numbers_till_hundred[0]
    
    hundreds = number // 100
    if hundreds:
        if hundreds == 1:
            txtnum.extend([numbers_till_hundred[hundreds], numbers_till_hundred[100]])
        else:
            txtnum.extend([numbers_till_hundred[hundreds], numbers_till_hundred[100] + 's'])

    tens_ones = number - hundreds * 100

    if not tens_ones:
        # if tens_ones is 0 we write nothing
        pass
    elif tens_ones in numbers_till_hundred:
        txtnum.append(numbers_till_hundred[tens_ones])
    else:
        ones = tens_ones % 10
        tens = tens_ones - ones
        txtnum.append(numbers_till_hundred[tens] + '-' + numbers_till_hundred[ones])
    
    return ' '.join(txtnum)

