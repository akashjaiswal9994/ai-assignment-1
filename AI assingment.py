q1=[1,1,1,1,0,0,0,0]
q2=[1,0,1,0,1,0,1,0]
q3=[1,1,0,0,1,1,0,0]
print(" Is every human good grader ? ")

for i in q1:
   for j in q2:
      for k in q3:
         z=i and j or k
if z==0:
 print("False")
else:
   pass
         
      
      
