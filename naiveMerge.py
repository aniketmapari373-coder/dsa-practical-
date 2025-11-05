def naiveSearch(text, pat):
    for i in range(len(text)-len(pat)+1):
        if text[i:i+len(pat)] == pat:
            print("Found at index", i)

def mergeSort(a):
    if len(a) > 1:
        mid = len(a)//2
        L, R = a[:mid], a[mid:]
        mergeSort(L); mergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            a[k] = L[i] if L[i]<R[j] else R[j]
            if L[i]<R[j]: i+=1
            else: j+=1
            k+=1
        while i<len(L): a[k]=L[i]; i+=1; k+=1
        while j<len(R): a[k]=R[j]; j+=1; k+=1

# ---- Main ----
text="AABAACAADAABAABA"; pattern="AABA"
naiveSearch(text, pattern)

arr=[9,3,7,1,5]
mergeSort(arr)
print("Sorted:", arr)
