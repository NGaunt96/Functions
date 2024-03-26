import math

hexVal = {"0" : 0,
          "1" : 1,
          "2" : 2,
          "3" : 3,
          "4" : 4,
          "5" : 5,
          "6" : 6,
          "7" : 7,
          "8" : 8,
          "9" : 9,
          "A" : 10,
          "B" : 11,
          "C" : 12,
          "D" : 13,
          "E" : 14,
          "F" : 15
          }

hex_keys = list(hexVal.keys())
hex_vals = list(hexVal.values())

##-----Functions-----##
#A File containing useful functions to be imported and used for other projects.#
##-----reverseString-----##
##Returns a the reverse of a given string.
def reverseString(string):
    newString = ''
    for i in range(len(string)-1,-1,-1):
        newString += string[i]

    return newString

##-----isPrime-----##
##Returns true if a given number, n, is prime
def isPrime(n):
    factors = findFactors(n)
    if len(factors) == 2:
        return True
    else:
        return False

##-----findFactorsOld-----##
##Version one of the findFactors function
def findFactorsOld(n):
    factors = []
    for i in range(1,round(n/2) + 1):
        if n % i == 0 and i not in factors:
            factors.append(i)
            if int(n/i) not in factors:
                factors.append(int(n/i))
    factors.sort()
        
    return factors

##------findFactors-----##
##Much faster and more efficient way to calculate factors
def findFactors(n):
    factors = []
    for i in range(1,round(math.sqrt(n)+ 1)):
        if n % i == 0:
            factors.append(i)
            if int(n/i) not in factors:
                factors.append(int(n/i))
    factors.sort()
        
    return factors

##-----findVowels-----##
##Returns a string showing how many
##vowels there are in a given string
def findVowels(string):
    vowelDict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for i in range(len(string)):
        for j in vowelDict:
            if string[i] == j:
                vowelDict[j] += 1

    out = 'there are %r a\'s, %r e\'s, %r i\'s, %r o\'s, and %r u\'s.' % (vowelDict['a'], vowelDict['e'], vowelDict['i'], vowelDict['o'], vowelDict['u']) 
    
    return out

##------findLeapDays-----##
##Returns the number of leap days between Jan 1st of the start year
##and jan 1st of the end year
def findLeapDays(start, end):
    count = 0
    for i in range(start, end-1):
        if i % 100 != 0:
            if i % 4 == 0:
                count += 1
        elif i % 900 == 200 or i % 900 == 600:
            count += 1
    return count

##-----additivePersistence-----##
##Returns the number of times the digits of a number, n, can be added
##together until the sum has one digit
def addPers(num):
    count = 0
    while len(str(num)) > 1:
        total = 0
        stringNum = str(num)
        for i in stringNum:
            total += int(i)
        num = total
        count += 1
            
    return count

##-----Factorial-----##
##Returns the factorial of a number, n
def factorial(n):
    total = 1
    while n:
        total *= n
        n -= 1

    return total

##-----removeDuplicates-----##
##Returns a sorted list with no duplicates, given a list.
def removeDuplicates(l):
    l.sort()
    lDict = dict()
    for i in l:
        lDict[i] = 0
    while len(l) > len(lDict):
        for i in l:
            count = 0
            for j in l:
                if i == j:
                    count += 1
            if count > 1:
                l.remove(i)    
    
    return l

##-----removeX-----##
##Returns a sorted list with all of a given value removed
def removeX(l, n):
    l.sort()
    while n in l:
        for i in l:
            if i == n:
                l.remove(i)

    return l

##-----checkLength-----##
##Returns true if a list given, l is the same length as a given number, n
def checkLength(l, n):
    if len(l) == n:
        return True
    else:
        return False

##-----denaryToBinary-----##
def denaryToBinary(n):
    power = int(math.floor(math.log(int(n), 2)))
    ans = ""
    while power > -1:
        if n >= 2**power:
            ans += "1"
            n = n - 2**power
        else:
            ans += "0"

        power -= 1
    return ans


##-----binaryToDenary-----##
def binaryToDenary(n):
    ans = 0
    count = len(str(n))-1
    for num in str(n):
        ans += int(num) * 2**count
        count -= 1
    return ans

##-----hexToDenary-----##
#Takes input of a string in Hex.
def hexToDenary(n):
    ans = 0
    count = len(n)-1
    for num in n:
        ans += int(hexVal[num]) * 16**count
        count -= 1
    return ans

##-----denaryToHex-----##
#Returns a string of Hex.
def denaryToHex(n):
    ans = ""
    b = str(denaryToBinary(n))
    while len(b)%4 > 0:
        b = "0"+b
    chars = [(b[i:i+4]) for i in range(0, len(b), 4)]
    for i in chars:
        pos = hex_vals.index(binaryToDenary(i))
        ans += hex_keys[pos]
    return ans















    
