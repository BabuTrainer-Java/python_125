eid=int(input("Enter   Eid"))
ename=input("Enter  Ename")
esal=int(input("Enter  a Sal"))
deptno=int(input("Enter  deptno"))
comm=int(input("Enter  a  comm"))
if esal>15000  and deptno==1  and  comm!=0:
    esal=esal+5000
    print(eid,":::",ename,"  ",esal,"   ",deptno,"  ",comm)
else:
    print("the Person   is  the  not  Eligable  for  incre")
