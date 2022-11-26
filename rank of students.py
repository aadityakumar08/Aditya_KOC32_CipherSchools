N=int(input("Enter total no of students in a class:"))
n=[]
m=[]
u=[]
for i in range(N):
      name=input("Enter Name:")
      n.append(name)
      marks=int(input("Enter marks of %s:"%(name)))
      m.append(marks)
      updated_marks=int(input("Enter updated marks of a %s:"%(name)))
      u.append(updated_marks)
dict1=dict(zip(n,m))
dict2=dict(zip(n,u))
j=max(u)
l=sorted(m)
h=l[::-1]
for c,z in dict2.items():
      if z==j:
        for q,w in dict1.items():
            if c==q:
                r=h.index(w)+1
                v=r-1
                if v==0:
                      print("Name:",c," Rank increased:",1)
                else:  
                      print("Name:",c,"Rank increased:",v)

