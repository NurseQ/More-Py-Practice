def countDog(st):
    count = 0
    for x in st.lower().split():
        if x == 'dog':
           count += 1
    return count

print(countDog('Dog is dog but dog is dog'))

seq = ['soup','dog','salad','cat','great']
newSeq = []
def remove(mylist):
    for x in mylist:
        if x[0] == 's':
            newSeq.append(x)
    return newSeq

print(remove(seq))

print(list(filter(lambda x: x[0] == 's', newSeq)))

