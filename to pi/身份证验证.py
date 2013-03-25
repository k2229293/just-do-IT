# -*- coding=utf-8 -*-
def jiaquan(n):
	w=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
	s=0
	for i in range(17):
		s+=n[i]*w[i]
	return s

def yanzheng(sfz):
	n=[]
	for i in sfz[:-1]:
		n.append(int(i))
	s=jiaquan(n)
	y=s%11
	zidian={0:'1',1:'0',2:'X',3:'9',4:'8',5:'7',6:'6',7:'5',8:'4',9:'3',10:'2'}
	last=zidian[y]
	if last==sfz[-1]:
		return [True,0]
	else:
		return [False,sfz[:-1]+last]

if __name__=='__main__':
	ip=raw_input("请输入18身份证号码：")
	if len(ip)<>18:
		print '非18位身份证号码'
	else:
		pd=yanzheng(ip)
		if pd[0]:
			print '身份证正确'
		elif not pd[0]:
			print '身份证错误,正确身份证号码:'+pd[1]




