# mix slag and S
slag = [48.4, 18, 1, 0, 0, 0]
S = [98, 91, 60, 42, 19, 10]
# 细度模数
Mx = (S[1] + S[2] + S[3] + S[4] + S[0] - 5 * S[5]) / (100 - S[5])
print(Mx)
for i in range(1, 100):
    A0 = (i * slag[0] + (100 - i) * S[0]) / 100
    A1 = (i * slag[1] + (100 - i) * S[1]) / 100
    A2 = (i * slag[2] + (100 - i) * S[2]) / 100
    A3 = (i * slag[3] + (100 - i) * S[3]) / 100
    A4 = (i * slag[4] + (100 - i) * S[4]) / 100
    A5 = (i * slag[5] + (100 - i) * S[5]) / 100
    # II区级配判断
    if 100 >= A0 >= 92 and 92 >= A1 >= 70 and 70 >= A2 >= 41 \
            and 50 >= A3 >= 10 and 25 >= A4 >= 0 and 10 >= A5 >= 0:
        print(i)
        t = [A0, A1, A2, A3, A4, A5]
        print(t)
