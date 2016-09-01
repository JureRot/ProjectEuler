import math, itertools, collections


def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def get_factors(n):
    factors = set()
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            factors.add(i)
            factors.add(n//i)
    return factors


def get_number_length(n):
    ls = {"0":0, "1":3, "2":3, "3":5, "4":4, "5":4, "6":3, "7":5, "8":5, "9":4, "10":3, "11":6, "12":6, "13":8, "14":8, "15":7, "16":7, "17":9, "18":8, "19":8, "1_":4, "2_":6, "3_":6, "4_":5, "5_":5, "6_":5, "7_":7, "8_":6, "9_":6, "00":7, "_":3, "000":8}
    return ls[n]

def day_of_week(year, month, day):
    """
    w = (d+floor(2.6*m-0.2)+y+floor(y/4)+floor(c/4)-2*c) mod 7
 
    Y = year - 1 for January or February
    Y = year for other months
    d = day (1 to 31)
    m = shifted month (March = 1, February = 12)
    y = last two digits of Y
    c = first two digits of Y
    w = day of week (Sunday=0, Monday=1, Tuesday=2, Wednesday=3, Thursday=4, Friday=5, Saturday=6)
    """

    d = day
    m = (month - 3)%12 + 1
    if m > 10:
        Y = year - 1
    else:
        Y = year
    y = Y%100
    c = (Y -(Y%100))/100

    w = (d + math.floor(2.6 * m -0.2) + y + math.floor(y/4) + math.floor(c/4) -2*c)%7

    return int(w)  

def sum_factors(n):
    if n == 1:
        return 1
    x = get_factors(n)
    x.remove(n)
    return sum(x)

def value_of_word(s):
    sum = 0
    for i in s:
        sum += ord(i)-64
    return sum

def Euler_quad_prime_formula(a, b):
    i = 0
    n = 0
    while True:
        if is_prime(n**2 + a*n + b):
            i += 1
            n += 1
        else:
            break
    return i

def is_palindrom(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False



def problem1():
    sum = 0
    for i in range(1000):
        if i%3 == 0 or i%5 == 0:
            sum += i
    return sum

def problem2():
    sum = 2
    a = 1
    b = 2
    c = a + b
    while c <= 4000000:
        if c%2 == 0:
            sum += c
        a = b
        b = c
        c = a + b
    return sum

"""This function works by finding successive factors of its input.
The first factor it finds will necessarily be prime. After a prime
factor is found, it is divided out of the original number and the
process continues. By the time we've divided them all out (leaving 1,
or the current factor (i)) we've got the last (largest) one.

def problem3():
    n = 600851475143
    for i in range(2,100000):
        while n % i == 0:
            n //= i
            #print("Yay, %d is a factor, now we should test %d" % (i, n))
            if n == 1 or n == i: 
                return i"""

def problem3(): # easier to understad and simpler than the one before it
    n = 600851475143
    for i in reversed(range(1, int(math.sqrt(n)))):
        if n%i == 0:
            if is_prime(i):
                return i

def problem4():
    largest = 0
    for i in reversed(range(900, 1000)):
        for j in reversed(range(900, 1000)):
            if str(i*j) == str(i*j)[::-1]:
                if i*j > largest:
                    largest = i*j
    return largest

def problem5():
    answer = 20
    while True:
        if answer%1 == 0 and answer%2 == 0 and answer%3 == 0 and answer%4 == 0 and answer%5 == 0 and answer%6 == 0 and answer%7 == 0 and answer%8 == 0 and answer%9 == 0 and answer%10 == 0 and answer%11== 0 and answer%12 == 0 and answer%13 == 0 and answer%14 == 0 and answer%15 == 0 and answer%16 == 0 and answer%17 == 0 and answer%18 == 0 and answer%19 == 0 and answer%20 == 0:
            return answer
        answer += 20

def problem6():
    a = 0
    for i in range(1, 101):
        a += i
    a = a**2
    b = 0
    for j in range(1, 101):
        b += j**2
    return a - b

def problem7():
    i = 0
    n = 0
    p = 0
    while True:
        if is_prime(n):
            i += 1
            p = n
        n += 1
        if i == 10001:
            return p

def problem8():
    biggest = 0
    n = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    for i in range(len(str(n))-12):
        if int(n[i])*int(n[i+1])*int(n[i+2])*int(n[i+3])*int(n[i+4])*int(n[i+5])*int(n[i+6])*int(n[i+7])*int(n[i+8])*int(n[i+9])*int(n[i+10])*int(n[i+11])*int(n[i+12]) > biggest:
            biggest = int(n[i])*int(n[i+1])*int(n[i+2])*int(n[i+3])*int(n[i+4])*int(n[i+5])*int(n[i+6])*int(n[i+7])*int(n[i+8])*int(n[i+9])*int(n[i+10])*int(n[i+11])*int(n[i+12])
    return biggest

def problem9():
    for a in range(500):
        for b in range(500):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == 1000:
                #print(a, b, c)
                return a*b*c

def problem10():
    sum = 0
    for i in range(2000000):
        if is_prime(i):
            sum += i
    return sum

def problem11_setup():
    ls = []
    n = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
    n = n.split()
    for i in range(20):
        ls.append([int(n[x]) for x in range(len(n)) if x >= (0+i*20) and x < (20+i*20)])
    print(ls)

def problem11():
    biggest = 0
    one=two=three=four = 0
    ls = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8], [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0], [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65], [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91], [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80], [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50], [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70], [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21], [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72], [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95], [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92], [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57], [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58], [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40], [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66], [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69], [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36], [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16], [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54], [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
    #horizontal
    for i in range(20):
        for j in range(17):
            if (ls[i][j] * ls[i][j+1] * ls[i][j+2] * ls[i][j+3]) > biggest:
                biggest = ls[i][j] * ls[i][j+1] * ls[i][j+2] * ls[i][j+3]
                one, two, three, four = ls[i][j], ls[i][j+1], ls[i][j+2], ls[i][j+3]
    #print(biggest, one, two, three, four)
    #vertical
    for i in range(20):
        for j in range(17):
            if (ls[j][i] * ls[j+1][i] * ls[j+2][i] * ls[j+3][i]) > biggest:
                biggest = ls[j][i] * ls[j+1][i] * ls[j+2][i] * ls[j+3][i]
                one, two, three, four = (ls[j][i], ls[j+1][i], ls[j+2][i], ls[j+3][i])
    #print(biggest, one, two, three, four)
    #back diagonal
    for i in range(17):
        for j in range(17):
            if (ls[i][j] * ls[i+1][j+1] * ls[i+2][j+2] * ls[i+3][j+3]) > biggest:
                biggest = ls[i][j] * ls[i+1][j+1] * ls[i+2][j+2] * ls[i+3][j+3]
                one, tow, three, four = ls[i][j], ls[i+1][j+1], ls[i+2][j+2], ls[i+3][j+3]
    #print(biggest, one, two, three, four)
    #forward diagonal
    for i in range(17):
        for j in range(3, 20):
            if (ls[j][i] * ls[j-1][i+1] * ls[j-2][i+2] * ls[j-3][i+3]) > biggest:
                biggest = ls[j][i] * ls[j-1][i+1] * ls[j-2][i+2] * ls[j-3][i+3]
                one, two, three, four = ls[j][i], ls[j-1][i+1], ls[j-2][i+2], ls[j-3][i+3]
    #print(biggest, one, two, three, four)
    return biggest

def problem12():
    i = 1
    n = 1
    while len(get_factors(n)) < 500:
        i += 1
        n += i
    return n

def problem13():
    sum = 0
    n = [37107287533902102798797998220837590246510135740250,
46376937677490009712648124896970078050417018260538,
74324986199524741059474233309513058123726617309629,
91942213363574161572522430563301811072406154908250,
23067588207539346171171980310421047513778063246676,
89261670696623633820136378418383684178734361726757,
28112879812849979408065481931592621691275889832738,
44274228917432520321923589422876796487670272189318,
47451445736001306439091167216856844588711603153276,
70386486105843025439939619828917593665686757934951,
62176457141856560629502157223196586755079324193331,
64906352462741904929101432445813822663347944758178,
92575867718337217661963751590579239728245598838407,
58203565325359399008402633568948830189458628227828,
80181199384826282014278194139940567587151170094390,
35398664372827112653829987240784473053190104293586,
86515506006295864861532075273371959191420517255829,
71693888707715466499115593487603532921714970056938,
54370070576826684624621495650076471787294438377604,
53282654108756828443191190634694037855217779295145,
36123272525000296071075082563815656710885258350721,
45876576172410976447339110607218265236877223636045,
17423706905851860660448207621209813287860733969412,
81142660418086830619328460811191061556940512689692,
51934325451728388641918047049293215058642563049483,
62467221648435076201727918039944693004732956340691,
15732444386908125794514089057706229429197107928209,
55037687525678773091862540744969844508330393682126,
18336384825330154686196124348767681297534375946515,
80386287592878490201521685554828717201219257766954,
78182833757993103614740356856449095527097864797581,
16726320100436897842553539920931837441497806860984,
48403098129077791799088218795327364475675590848030,
87086987551392711854517078544161852424320693150332,
59959406895756536782107074926966537676326235447210,
69793950679652694742597709739166693763042633987085,
41052684708299085211399427365734116182760315001271,
65378607361501080857009149939512557028198746004375,
35829035317434717326932123578154982629742552737307,
94953759765105305946966067683156574377167401875275,
88902802571733229619176668713819931811048770190271,
25267680276078003013678680992525463401061632866526,
36270218540497705585629946580636237993140746255962,
24074486908231174977792365466257246923322810917141,
91430288197103288597806669760892938638285025333403,
34413065578016127815921815005561868836468420090470,
23053081172816430487623791969842487255036638784583,
11487696932154902810424020138335124462181441773470,
63783299490636259666498587618221225225512486764533,
67720186971698544312419572409913959008952310058822,
95548255300263520781532296796249481641953868218774,
76085327132285723110424803456124867697064507995236,
37774242535411291684276865538926205024910326572967,
23701913275725675285653248258265463092207058596522,
29798860272258331913126375147341994889534765745501,
18495701454879288984856827726077713721403798879715,
38298203783031473527721580348144513491373226651381,
34829543829199918180278916522431027392251122869539,
40957953066405232632538044100059654939159879593635,
29746152185502371307642255121183693803580388584903,
41698116222072977186158236678424689157993532961922,
62467957194401269043877107275048102390895523597457,
23189706772547915061505504953922979530901129967519,
86188088225875314529584099251203829009407770775672,
11306739708304724483816533873502340845647058077308,
82959174767140363198008187129011875491310547126581,
97623331044818386269515456334926366572897563400500,
42846280183517070527831839425882145521227251250327,
55121603546981200581762165212827652751691296897789,
32238195734329339946437501907836945765883352399886,
75506164965184775180738168837861091527357929701337,
62177842752192623401942399639168044983993173312731,
32924185707147349566916674687634660915035914677504,
99518671430235219628894890102423325116913619626622,
73267460800591547471830798392868535206946944540724,
76841822524674417161514036427982273348055556214818,
97142617910342598647204516893989422179826088076852,
87783646182799346313767754307809363333018982642090,
10848802521674670883215120185883543223812876952786,
71329612474782464538636993009049310363619763878039,
62184073572399794223406235393808339651327408011116,
66627891981488087797941876876144230030984490851411,
60661826293682836764744779239180335110989069790714,
85786944089552990653640447425576083659976645795096,
66024396409905389607120198219976047599490197230297,
64913982680032973156037120041377903785566085089252,
16730939319872750275468906903707539413042652315011,
94809377245048795150954100921645863754710598436791,
78639167021187492431995700641917969777599028300699,
15368713711936614952811305876380278410754449733078,
40789923115535562561142322423255033685442488917353,
44889911501440648020369068063960672322193204149535,
41503128880339536053299340368006977710650566631954,
81234880673210146739058568557934581403627822703280,
82616570773948327592232845941706525094512325230608,
22918802058777319719839450180888072429661980811197,
77158542502016545090413245809786882778948721859617,
72107838435069186155435662884062257473692284509516,
20849603980134001723930671666823555245252804609722,
53503534226472524250874054075591789781264330331690,]
    for i in range(len(n)):
        sum += n[i]
    return sum

def problem14():
    n_max = 1
    i_best = 1
    for j in range(1, 1000000):
        n_temp = 1
        i = j
        while i != 1:
            if i%2 == 0:
                i = i//2
            else:
                i = 3*i +1
            n_temp += 1
        if n_temp > n_max:
            n_max = n_temp
            i_best = j
    return i_best

def problem15():
    n = 20
    return (math.factorial(n*2)) // (math.factorial(n) * math.factorial(n))

def problem16():
    sum = 0
    n= str(2**1000)
    for i in n:
        sum += int(i)
    return sum

def problem17():
    sum = 0
    for i in range(1, 1001):
        n = str(i)
        if len(n) == 1:
            sum += get_number_length(n)
            #print(n)
        elif len(n) == 2:
            if n[0] == "1":
                sum += get_number_length(n)
                #print(n)
            else:
                sum += get_number_length(n[0]+"_")
                #print(n[0]+"_")
                sum += get_number_length(n[1])
                #print(n[1])
        elif len(n) == 3:
            sum += get_number_length(n[0])
            #print(n[0])
            sum += get_number_length("00")
            #print("00")
            if (n[1] == "0" and n[2] != "0"):
                sum += get_number_length("_")
                #print("_")
                sum += get_number_length(n[-1])
                #print(n[-1])
            elif (n[1] != "0"):
                if n[1] == "1":
                    sum += get_number_length("_")
                    #print("_")
                    sum += get_number_length(n[1:])
                    #print(n[1:])
                else:
                    sum += get_number_length("_")
                    #print("_")
                    sum += get_number_length(n[1]+"_")
                    #print(n[1]+"_")
                    sum += get_number_length(n[2])
                    #print(n[2])
        elif len(n) == 4:
            sum += get_number_length("1")
            #print("1")
            sum += get_number_length("000")
            #print("000")
    return sum

def problem18():
    biggest = 0
    ls =[[75,],
[95, 64,],
[17, 47, 82,],
[18, 35, 87, 10,],
[20, 4, 82, 47, 65,],
[19, 1, 23, 75, 3, 34,],
[88, 2, 77, 73, 7, 63, 67,],
[99, 65, 4, 28, 6, 16, 70, 92,],
[41, 41, 26, 56, 83, 40, 80, 70, 33,],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29,],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23,],]
    while len(ls) > 1:
        slast = len(ls)-2
        last = slast + 1
        for i in range(len(ls[slast])):
            ls[slast][i] = ls[slast][i] + max(ls[last][i], ls[last][i+1])
        del ls[last]
    return ls[0][0]  
    
def problem19():
    sum = 0
    for i in range(1901, 2000 + 1):
        for j in range(1, 13):
            if day_of_week(i, j, 1) == 0:
                sum += 1
    return sum

def problem20():
    sum = 0
    n = str(math.factorial(100))
    for i in n:
        sum += int(i)
    return sum

def problem21():
    amicables = set()
    for i in range(2,10000):
        j = sum_factors(i)
        if sum_factors(j) == i and i != j:
            amicables.add(i)
            amicables.add(j)
    return sum(amicables)

def problem22():
    sum = 0
    f  = open("names.txt", "r")
    n = f.read()
    f.close()
    n = n.replace('"', "").split(",")
    n.sort()
    for i in range(len(n)):
        sum += (i+1) * value_of_word(n[i])
    return sum

def problem23():
    allsums = (28123*(28123+1))//2
    allabus = set()
    #allnums = list(range(1,28123))
    abundants = set()
    for i in range(1,28123+1):
        if sum_factors(i) > i:
            abundants.add(i)
    abundants = list(abundants)
    for i in abundants:
        for j in abundants[abundants.index(i):]:
            if i+j > 28123:
                break
            allabus.add(i+j)
    return allsums - sum(allabus)

def problem24():
    perm =[]
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    x = itertools.permutations(digits)
    for i in x:
        perm.append("".join(i))
    perm.sort()
    return perm[999999]

def problem25():
    a, b = 1, 1
    c = a+b
    i = 3
    while len(str(c)) < 1000:
        a = b
        b = c
        c = a+b
        i += 1
    return i

def problem26():
    longest = 1
    biggest = 1
    for i in range(1, 1001):
        n = 1 #numerator
        d = i #denominator
        r = n%d #reaminder
        x = []
        while True:
            while n < d:
                n = n*10
            if n > d:
                r = n%d
                n = r*10
            if r != 0:
                if r in x:
                    if r != 0:
                        if len(x[x.index(r):]) > longest:
                            longest = len(x[x.index(r):])
                            biggest = i
                    break
                else:
                    x.append(r)
            else:
                break
    return(biggest)

def problem27():
    best = 0
    best_a = 0
    best_b = 0
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            if Euler_quad_prime_formula(a, b) > best:
                best = Euler_quad_prime_formula(a, b)
                best_a = a
                best_b = b
                #print(best, best_a, best_b)
    return best_a*best_b

def problem28():
    sum = 0
    x = list(range(1, 1001**2 +1))
    n = 2
    i = 0
    end = True
    while end:
        for k in range(4):
            sum += x[i]
            if i+n < len(x):
                i += n
            else:
                end = False
                break
        n += 2
    return sum

def problem29():
    unique = set()
    for i in range(2, 101):
        for j in range(2, 101):
            unique.add(i**j)
    return len(unique)

def problem30():
    sum = 0
    for i in range(2, 1000000):
        temp_sum = 0
        for j in str(i):
            temp_sum += int(j)**5
        if temp_sum == i:
            sum += i
    return sum

def problem31():
    all_combos = [1] + [0]*200
    coins = [1, 2, 5, 10, 20, 50, 100, 200,]
    for i in coins:
        for j in range(i, 201):
            all_combos[j] += all_combos[j-i]
            #print(all_combos)
    return all_combos[-1]

def problem32():
    wanted = "123456789"
    all_pandigital = set()
    for i in range(10000):
        factors = list(sorted(get_factors(i)))
        if len(factors)%2 == 0:
            factors = factors[:len(factors)//2]
        else:
            factors = factors[:len(factors)//2+1]
        for j in factors:
            x = "".join(sorted(str(i) + str(j) + str(i//j)))
            if len(x) == 9:
                if x == wanted:
                    all_pandigital.add(i)
    return sum(all_pandigital)

def problem33():
    instances = []
    for i in range(1, 101):
        a = str(i)
        for j in range(1, i):
            b = str(j)
            for x in b:
                for y in a:
                    if x == y and x != "0":#print(str(j)+"/"+str(i), str(j).replace("x", "")+"/"+str(i).replace("x", ""))
                        small_a = a.replace(x, "")
                        small_b = b.replace(x, "")
                        try:
                            if (int(b)/int(a)) == (int(small_b)/int(small_a)):
                                #print(b+"/"+a, small_b+"/"+small_a)
                                instances.append((int(small_b), int(small_a),))
                        except ValueError: # for empty string
                            pass
                        except ZeroDivisionError: #for tens and hundreds
                            pass
    all_b = 1
    all_a = 1
    for i in instances:
        all_b *= i[0]
        all_a *= i[1]
    return str(all_b)+"/"+str(all_a)

def problem34():
    sum = 0
    for i in range(3, 100000):
        temp_sum = 0
        for j in str(i):
            temp_sum += math.factorial(int(j))
        if temp_sum == i:
            sum += i
    return sum

def problem35():
    sum = 0
    for i in range(1000000):
        a = str(i)
        all_primes = True
        for j in range(len(a)):
            if not is_prime(int(a[j:]+a[:j])):
                all_primes = False
                break
        if all_primes:
            sum += 1
    return sum

def problem36():
    sum = 0
    for i in range(1000000):
        if is_palindrom(i) and is_palindrom(bin(i)[2:]):
            sum += i
    return sum

def problem37():
    sum = 0
    for i in range(10, 1000000):
        a = str(i)
        if is_prime(i):
            all_primes = True
            for j in range(1, len(a)):
                if not is_prime(int(a[j:])) or not is_prime(int(a[:j])):
                    all_primes = False
                    break
            if all_primes:
                sum += i
    return sum

def problem38():
    wanted = "123456789"
    biggest = 0
    for i in range(1, 10000):
        x = ""
        for j in range(1, 10000000000): #it can to toward infinity, it will be interupted
            if len(x + str(i*j)) <= 9:
                x += str(i*j)
            else:
                break
        if "".join(sorted(x)) == wanted:
            if int(x) > biggest:
                biggest = int(x)
    return biggest

def problem39(): #VERY VERY SLOW (~250sec)
    best = 0
    biggest = 0
    for i in reversed(range(1, 1001)):
        combos = 0
        for a in range(1, i):
            for b in range(1, i-a):
                c = i-a-b
                if a**2 + b**2 == c**2:
                    combos += 1
        if math.ceil(combos/2) > biggest:
            biggest = math.ceil(combos/2)
            best = i
    return best

def problem40():
    x = ""
    for i in range(1000000):
        x += str(i)
    return int(x[1]) * int(x[10]) * int(x[100]) * int(x[1000]) * int(x[10000]) * int(x[100000] * int(x[1000000]))

def problem41():
    biggest = 0
    for i in range(1, 10):
        x = itertools.permutations(range(1,i+1))
        for j in x:
            y = int("".join(str(a) for a in j))
            if is_prime(y):
                if y > biggest:
                    biggest = y
    return biggest

def problem42():
    sum = 0
    triangles = set()
    for n in range(1, 100):
        triangles.add(1/2*n*(n+1))
    f = open("words.txt", "r")
    x = f.read()
    f.close()
    x = x.replace('"', "").split(",")
    for i in x:
        if value_of_word(i) in triangles:
            sum += 1
    return sum

def problem43():
    sum = 0
    ls = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
    x = itertools.permutations(ls)
    for i in x:
        y = "".join(i)
        if y[0] != "0":
            if int(y[1:4])%2 == 0 and int(y[2:5])%3 == 0 and int(y[3:6])%5 == 0 and int(y[4:7])%7 == 0 and int(y[5:8])%11 == 0 and int(y[6:9])%13 == 0 and int(y[7:10])%17 == 0:
                sum += int(y)
    return sum

def problem44(): #a+b=c; b+c=d; d-c=b, 2c-d=a
    pentagons = set()
    n = 0
    while True:
        n += 1
        x = n*(3*n-1)/2
        pentagons.add(x)
        for i in pentagons:
            #print(x, i, x-i, x-2*i)
            if x-i in pentagons and x-2*i in pentagons:
                return x-2*i

def problem45(): #every hexagon is also a triangle (every second triangle is a hexangle)
    hexagons = set()
    n = 1
    while True:
        hexagons.add(n*(2*n-1))
        pentagon = n*(3*n-1)/2
        if pentagon in hexagons and n >165:
            return pentagon
        n += 1

"""def problem46(): # WORKS VERY SLOW (~8min)
    primes = set()
    for i in range(2, 10000):
        if is_prime(i):
            primes.add(i)
        elif i%2 == 1:
            found = False
            for j in range(1, i):
                if j in primes:
                    for k in range(1, i-j):
                        if j + 2*(k**2) == i:
                            print(i, j, k)
                            found = True
                            break
                if found:
                    break
            if not found:
                return i"""

def problem46(): #PROBI RAZUMET
    n = 5
    f = 1
    primes = set()
     
    while True:
        if all(n % p for p in primes):
            primes.add(n)
            print(n)
        else:
            if not any((n-2*i*i) in primes for i in range(1, n)):
                break
        n += 3-f
        f = -f

    return n
def get_prime_factors(n, prime_factors):
    if not is_prime(n):
        a = max(i for i in get_factors(n) if is_prime(i))
        prime_factors.append(a)
        get_prime_factors(n//a, prime_factors)
    else:
        prime_factors.append(n)
        return prime_factors


def problem47():
    i = 2
    while True:
        pf = []
        get_prime_factors(i, pf)
        if len(set(pf)) == 4:
            pf2 = []
            get_prime_factors(i+1, pf2)
            if len(set(pf2)) == 4:
                pf3 = []
                get_prime_factors(i+2, pf3)
                if len(set(pf3)) == 4:
                    pf4 = []
                    get_prime_factors(i+3, pf4)
                    if len(set(pf4)) == 4:
                        return i
        i += 1

def problem48():
    sum = 0
    for i in range(1, 1001):
        sum += i**i
    return str(sum)[-10:]

def problem49():
    answer = ""
    ds = collections.defaultdict(list)
    for i in range(1000, 10000):
        if is_prime(i):
            x = [a for a in str(i)]
            ds["".join(sorted(x))].append(i)
    for k, v in ds.items():
        rv = v[::-1]
        for a in rv:
            for b in rv[rv.index(a)+1:]:
                if b - (a-b) in rv and k != "1478":
                    answer += str(b-(a-b)) + str(b) + str(a)
    return answer

def problem50():
    longest = 0
    biggest = 0
    primes = [i for i in range(1, 1000001) if is_prime(i)]
    prime_sums = [0] #sum of all primes up to n
    for p in primes:
        prime_sums.append(prime_sums[-1] + p)
        if prime_sums[-1] >= 1000000:
            break
    #to check all posibilites, we check for every n and the difference between n and m(<n) [n-m]. with that we check if we start from number other than 2 (n-m -> sum of all primes from m to n (sum of all from 1 to n minus sum of all from 1 to m))
    for i in range(len(prime_sums)):
        for j in range(len(prime_sums)-1, 0, -1): #same as outer loop, but reversed
            n = prime_sums[j] - prime_sums[i] #n -> sum of all primes from i to j
            if j-i > longest and is_prime(n): #j-i -> number of consecutive primes (not the value of sum, but the number of elements)
                longest = j-i
                biggest = n
    return biggest

def problem51():
    print("problem51")

print(problem51())
