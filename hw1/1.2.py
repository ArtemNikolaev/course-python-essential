# seconds to hh:mm:ss
# 15,820 - 04:23:40

ss = int(input('Введите количество секунд: '))

hh = ss // (60 * 60)
ss %= (60 * 60)

if hh == 0:
    hh = '00'
elif hh < 10:
    hh = '0' + str(hh)
else:
    hh = str(hh)

mm = ss // 60
ss %= 60

if mm == 0:
    mm = '00'
elif mm < 10:
    mm = '0' + str(mm)
else:
    mm = str(mm)

if ss == 0:
    ss = '00'
elif ss < 10:
    ss = '0' + str(ss)
else:
    ss = str(ss)


print(hh + ':' + mm + ':' + ss)