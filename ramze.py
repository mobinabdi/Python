def jam_argham(ramz_digist):
    sum = 0
    for k in ramz_digist:
        sum= ramz_digist[k] + sum


def ramz_is_ok(ramz_digist):
    if ramz_digist['panj'] + ramz_digist['se'] == 14 and \
 ramz_digist['yek'] == ramz_digist['do'] * 2 - 1 and \
       ramz_digist['chahar'] == ramz_digist['do'] + 1 and \
       ramz_digist['do'] + ramz_digist['se'] == 10:
            if jam_argham(ramz_digist):
                return  True

for ramz in range(0,100000):
    this_ramz = str(ramz).zfill(5)
    ramz_digist = {}
    ramz_digist['yek'] = int(this_ramz[0])
    ramz_digist['do'] = int(this_ramz[1])
    ramz_digist['se'] = int(this_ramz[2])
    ramz_digist['chahar'] = int(this_ramz[3])
    ramz_digist['panj'] = int(this_ramz[4])
    if ramz_is_ok(ramz_digist):
        print(ramz)