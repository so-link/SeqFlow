import calendar, math
import os

def check_path(path, is_create=True):
	dir, file = os.path.split(path)
	check_dir(dir, is_create)

def check_dir(dir, is_create = False):
	if dir==".": return True
	fe = os.path.exists(dir)
	if is_create and not fe:
		os.makedirs(dir)
	return fe

def sigmoid(x):
	return 1.0/(1.0+math.exp(-x))

def arcsigmoid(x):
	return -math.log(1.0/x-1)

def movingAvg(seq, k):
	if len(seq)<k: return []
	res=[]
	for i in range(len(seq)-k+1):
		res.append(sum(seq[i:i+k])/k)
	return res

def scaleAvg(seq, k):
	if len(seq)<k: return []
	res=[]
	for i in range(len(seq)//k):
		res.append(sum(seq[i*k:i*k+k])/k)
	return res

def scaleAvgN(seq):
	res=[]
	n=len(seq[0])
	k=len(seq)
	for i in range(n):
		s=0.0
		for j in range(k):
			s+=seq[j][i]
		res.append(s/k)
	return res

if __name__ == "__main__":
	# check_dir("./a/a/a", True)
	extract_path("afds/asdf/fa.h5")