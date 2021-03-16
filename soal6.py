def arithmetic_geometric():
    while True:
        deret = input().split(' ')
        for i in range(len(deret)):
            deret[i] = int(deret[i])

        a = deret[0]
        b = deret[1]
        c = deret[2]

        if deret == [0,0,0]:
            break

        elif c - b == b - a:
            print('Deret Aritmatika')
            u_n = a + (len(deret) * (b-a))
            print('AP:', u_n)

        elif c/b == b/a:
            print('Deret Geometri')
            u_n = a * (b/a)**(len(deret))
            print('GP:', u_n)

        elif (c - b != b - a) and (c/b != b/a):
            print('Deret bukan Aritmatika maupun Geometri')

        print()


arithmetic_geometric()