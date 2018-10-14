import random, sys

class BigInteger(object):
    
    def __init__(self, num):
        
        self.num = num
        self.mul_table = {}
        
    def __repr__(self):

        return self.num

    def __add__(self, other):
        
        self_start, other_start = len(self.num)-1, len(other.num)-1
        result_sum, Sum, Carry = "", 0, 0

        while self_start >= 0 and other_start >= 0:

            Sum = int(self.num[self_start]) + int(other.num[other_start]) + Carry
            Carry = int(Sum / 10)
            Sum %= 10
            result_sum = str(Sum) + result_sum
            self_start -= 1
            other_start -= 1

        if self_start >= 0 or other_start >= 0:
            
            remain_num, remain_start = None, -1
            if self_start >= 0:
                remain_num = self.num
                remain_start = self_start
            else:
                remain_num = other.num
                remain_start = other_start

            while remain_start >= 0:
                Sum = int(remain_num[remain_start]) + Carry
                Carry = int(Sum / 10)
                Sum %= 10
                result_sum = str(Sum) + result_sum
                remain_start -= 1

        result_sum = '1' + result_sum if Carry else result_sum 

        return BigInteger(result_sum)  


    def times_n(self, A, order):

        if order in self.mul_table:
            return self.mul_table[order]

        result = BigInteger('0')
        for _ in range(order):
            result += A

        self.mul_table[order] = result

        return result


    def times_10n(self, A, _10_order):

        return BigInteger(A.num+'0'*_10_order) if A.num != '0' else A


    def __mul__(self, other):

        order, result_mul = 0, BigInteger('0')
        if len(other.num) > len(self.num):
            based = other
            multiplyer = self
        else:
            based = self
            multiplyer = other 

        for i in range(len(multiplyer.num))[::-1]:
            result_mul += self.times_10n(self.times_n(based, int(multiplyer.num[i])), order) 
            order += 1
        return result_mul




def test_class():

    for _ in range(1000):

        rand_num1 = random.randint(0, sys.maxsize)
        rand_num2 = random.randint(0, sys.maxsize)
        object1 = BigInteger(str(rand_num1))
        object2 = BigInteger(str(rand_num2))
        sum_object = object1 * object2
        if sum_object.num != str(rand_num1 * rand_num2):
            print('Case Fail! {} + {}'.format(rand_num1, rand_num2))
            sys.exit()
    print('Pass!')



if __name__ == '__main__':
    
    test_class()






