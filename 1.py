alien = {'color': 'green', 'points': 5}
print(alien['color'])
alien['x'] = 0
alien['y'] = 1
print(alien)
witer = {}
witer['xx'] = 11
witer['yy'] = 22
print(witer)
if witer['xx'] == 11:
    witer['yy'] = 11
print(witer)
del witer['xx']
print(witer)  # ##111111
inty = {
    'ddd': 'ssddffgg',
    'ss': 'aassdd',
    'nnn': 'ssddffgg'
    }
for sss, v in inty.items():
    print("\nkkk:" + sss)
for dd in inty.keys():
    print("dd")
for sss in inty.values():
    print("ssss:" + 'sss.title()')
for name in sorted(inty.keys()):
    print(name+" shi vv")
for nam in set(sorted(inty.values())):
    print("\nasDf   "+str(nam))
