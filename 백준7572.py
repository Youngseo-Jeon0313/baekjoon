'''
circle을 얼마나 도는가 각자!
'''

twelve = 'ABCDEFGHIJKL'
ten = '0123456789'
idx = int(input()) - 2013
print(twelve[(idx+5)%12] +ten[(idx-1)%10])