import glob
import csv

# 0이라 써있는 걸 4로 바꿔주는 거임. 이미 4이면 노필요.

paths = glob.glob('data/simulations/*.txt')
for i, txt in enumerate(paths):
    with open(txt, 'r') as f:
        data = list(csv.reader(f))[0]
    data[0] = '4'
    with open(txt, 'w') as f:
        csv.writer(f, delimiter=' ').writerow(data)
    if i % 100 == 0: print(f'{(i+1)/len(paths):7.3%} done!')
