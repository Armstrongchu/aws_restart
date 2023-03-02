"""list=[1,2,3,4,5,6,7,8]
print(list[7])
print(list[8:1:-1])
print(list[7])
print(list[-1:999:1])
print(list[10])
"""

bInsulin="fvnqhlcgshlvealylvcgergffytpkt"

aInsulin="giveqcctsicslyqlenycn"
insulin = aInsulin + bInsulin

aaCountInsulin = {x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']}
print(aaCountInsulin)

"""for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']:
    print(insulin.upper().count(x))
    aaCountInsulin = {x: float(insulin.upper().count(x))}"""

lstAlist = []
lstAlist = [insulin.upper().count(x) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']]
tupBtuple = (insulin.upper().count(x) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y'])
print(lstBlist)
