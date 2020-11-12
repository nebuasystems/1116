#4. 구구단 이중 for~in
cnt1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for w in cnt1:
    for r in cnt2:
        rst = w * r
        print(f'{r} × {w} = {rst} ', end='')
    print('')