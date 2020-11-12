#4. 구구단 이중 for~in

for w in range(1,10):
    for r in range(1,10):
        rst = w * r
        #print(f'{r} × {w} = {rst}', end='')
        s = f'{r} × {w} = {rst}'

        print(s.ljust(15), end='')
    print('')