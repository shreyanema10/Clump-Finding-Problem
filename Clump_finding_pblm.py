def kmerlst(string, k, L, t):
    Nu = {'A': 0, 'T': 1, 'G': 2, 'C': 3}
    Nuinv = {0:'A', 1:'T', 2:'G', 3:'C'}
    lst = []
    for l in range(len(string)-L+1):
        h = {}
        kmer = 0
        dna = string[l:l+k]
        for x,i in enumerate(dna):
            kmer += pow(4,k-x-1)*Nu[i] 
        h[kmer] = 1
        for i in range(L-k):
            kmer = (kmer - Nu[string[l+i]]*pow(4,k-1))*4 + Nu[string[l+i+k]]
            
            if kmer in h.keys():
                h[kmer] += 1
            else:
                h[kmer] = 1
        
        
        for j in h.keys():
            if h[j]>=t:
                num = [0 for i in range(k)]
                n = j
                i = k-1
                while n!=0:
                    num[i] = n%4
                    n = (n-n%4)/4
                    i-=1
                km = ''
                for i in num:
                    km+= Nuinv[i]
                if km not in lst:
                    lst.append(km)
                     
                
    return lst


s = str(input())
klt = list(map(int,input().rstrip().split()))
k = klt[0]
L = klt[1]
t = klt[2]

lst = kmerlst(s, k, L, t)
for i in sorted(lst):
    print(i, end = '\t')

            