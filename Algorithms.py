class Algorithms:
    def __init__(self) -> None:
        pass
    
    def SelectionSort(Arr):
        for i in range(len(Arr)-1):
            minimum = i
            for j in range(i+1, len(Arr)):
                if Arr[j] < Arr[minimum]:
                    minimum = j
            if minimum != i:
                Arr[minimum], Arr[i] = Arr[i], Arr[minimum]
        return Arr

    def InsertionSort(Arr):
        for i in range(len(Arr)):
            key = Arr[i]
            j = i-1
            while j >= 0 and Arr[j]>key:
                Arr[j+1] = Arr[j]
                j = j-1
            Arr[j+1] = key
        return Arr

    def Merge(Arr, l, r, m):
        n1 = l
        n2 = m+1
        A = []
        
        while n1 <=m and n2 <= r:
            if Arr[n1] < Arr[n2]:
                A.append(Arr[n1])
                n1 += 1
            else:
                A.append(Arr[n2])
                n2 += 1
        while n1 <= m:
            A.append(Arr[n1])
            n1 += 1
        while n2 <= r:
            A.append(Arr[n2])
            n2 += 1
        for i in range(l, r+1):
            Arr[i] = A[i-l]

    def MergeSort(self, Arr, l, r):
        if r > l:
            m = (l+r)//2
            self.MergeSort(Arr, l, m)
            self.MergeSort(Arr, m+1, r)
            self.Merge(Arr, l, r, m)

    def BubbleSort(Arr):
        for i in range(len(Arr)-1):

            for j in range(len(Arr)-1):
                if Arr[j] > Arr[j+1]:
                    Arr[j],Arr[j+1] = Arr[j+1], Arr[j]
        return Arr

    def CountingSort(Arr):
        k = int(max(Arr)) - int(min(Arr)) + 1
        count = [0 for i in range(k)]
        output  = [0 for i in range(len(Arr))]

        for i in range(0, len(Arr)):
            count[Arr[i]-int(min(Arr))] += 1

        for i in range(1, len(count)):
            count[i] += count[i-1]

        for i in range(len(Arr)-1,-1,-1):
            output[count[Arr[i]-int(min(Arr))]-1] = Arr[i]
            count[Arr[i]-int(min(Arr))] -= 1

        return output

    def CountingSortWithExp(Arr, exponential):
        count = [0 for i in range(10)]
        output  = [0 for i in range(len(Arr))]

        for i in range(0, len(Arr)):
            rad = Arr[i] // exponential
            count[rad % 10] += 1

        for i in range(1, 10):
            count[i] += count[i-1]

        i = len(Arr)-1
        while i>= 0:
            rad = Arr[i] // exponential
            output[count[rad%10]-1] = Arr[i]
            count[rad % 10] -= 1
            i -= 1

        for n in range(len(Arr)):
            Arr[n] = output[n]

    def RadixSort(self, Arr):
        maximum = max(Arr)
        exponential = 1
        while maximum/exponential>0:
            self.CountingSortWithExp(Arr, exponential)
            exponential *= 10

    def BucketSort(self, Arr, n):
        A = [[] for i in range(n)]
            
        for j in Arr:
            b = int(n * j)
            A[b].append(j)
        
        for i in range(n):
            A[i] = self.InsertionSort(A[i])
            
        m = 0
        for n in range(n):
            for o in range(len(A[n])):
                Arr[m] = A[n][o]
                m += 1
        return Arr

