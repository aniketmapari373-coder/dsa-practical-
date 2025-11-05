def naive (pat, text):
    pos=[]
    for i in range(len(text)-len(pat)+1):
        j=0
        while j<len(pat) and text[i+j]==pat[j]:
            j+=1
        if j==len(pat):
            pos.append(i)
    return pos
text=input("enter the text: " )
pat=input("enter pattern to search: ")
res=naive(pat,text)
if res:
    print(" pattern found at index: ", res)
else:
    print(" pattern not found")
    
