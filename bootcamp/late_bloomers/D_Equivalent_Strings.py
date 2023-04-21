st1 = input()
st2 = input()

while len(st1) >=1 and len(st2) >= 1:
    if st1 == st2:
        print("YES")
        break
    else:
        st1[:len(st1) // 2] == st2[:len(st2) // 2]