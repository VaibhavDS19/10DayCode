# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input())
st1 = []
st2 = []
for i in range(q):
    queries = list(map(int, input().split()))
    a = queries[0]
    if a==1:
        c = queries[1]
        st1.append(c)
    if a==2:
        if st2:
            st2.pop(0)
            if not st2:
                for i in st1:
                    st2.append(i)
                st1.clear()
        else:
            for i in st1:
                st2.append(i)
            st1.clear()
            st2.pop(0)

    if a==3:
        if not st2:
            print(st1[0])
        else:
            print(st2[0])
            
