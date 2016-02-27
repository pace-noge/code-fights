def proCategorization(pros, preferences):
    kerjaan = []
    orang_kerja = []
    result = []
    pair_pro_pre = dict(zip(pros, preferences))
    for x in preferences:
        for pre in x:
            if pre not in kerjaan:
                kerjaan.append(pre)

    kerjaan = sorted(kerjaan)
    for kerja in kerjaan:
        orang_kerja = []
        orang = []
        orang_kerja.append([kerja])
        for x in pair_pro_pre:
            if orang_kerja[0][0] in pair_pro_pre[x]:
                orang.append(x)
        orang_kerja.append(sorted(orang))
        #print orang_kerja[0][0]
        # print orang_kerja
        # for x in pair_pro_pre:
        #     if [pair_pro_pre[x]] in orang_kerja:

        result.append(orang_kerja)

    return result

pros = ["Jack", "Leon", "Maria"]
preferences = [["Computer repair", "Handyman", "House cleaning"],
               ["Computer lessons", "Computer repair", "Data recovery service"],
               ["Computer lessons", "House cleaning"]]

print proCategorization(pros, preferences)
