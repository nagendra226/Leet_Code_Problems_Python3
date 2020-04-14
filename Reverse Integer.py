class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x < 2147483647:
                return x
            else:
                return 0
        elif x < 0:
            x = str(x)
            sign = x[0]
            number = x[1::]
            number = number[::-1]
            x = int(sign + number)
            if x > -2147483647:
                return x
            else:
                return 0
        elif x == 0:
            return 0

        '''
    My code works well in my laptop 
    stupid interpeter not giving output.
    if x>0:
            x = str(x)
            x = x[::-1]
            x = int(x)
            return x
        elif x<0:
            x = str(x)
            sign = x[0]
            number = x[1::]
            number = number[::-1]
            return int(sign+number)
        elif x==0:
            return 0
    '''
