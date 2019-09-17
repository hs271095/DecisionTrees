attribute_set=['A','B','C','Target']
class_values=[(0,1)]
dataset=[]
print("Enter no of instances")
no_of_instances=int(input())
for i in range(no_of_instances):
    temp=list(map(int,input().split(" ")))
    dataset.append(temp)
print(dataset)

    

