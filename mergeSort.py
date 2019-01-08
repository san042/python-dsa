# MergeSort

datas = [ 12,19,31,4,23]
print("Initial State: ", datas)


def mergeSort(datas):
    if len(datas) > 1:
        mid = len(datas) //2
        #breaking by left from offset:mid position
        data_left = datas[:mid]
        #breaking by right from offset:mid position
        data_right = datas[mid:]

        #TODO recursive call of each parts of the dataset
        mergeSort(data_left)
        mergeSort(data_right)



        #TODO
        i=0 # left array index
        j=0 # right array index
        k=0  # merged array index

        # While both part has values
        while i < len(data_left) and j<len(data_right):
            if data_left[i] < data_right[j]:
                datas[k] = data_left[i]
                i += 1
            else:
                datas[k] = data_right[j]
                j += 1
            k += 1
           
            

        #while left has value
        while i < len(data_left):
            datas[k] = data_left[i]
            i += 1
            k += 1

        #while right has value
        while j < len(data_right):
            datas[k] = data_right[j]
            j += 1
            k += 1

mergeSort(datas)
print("Resultant state: ", datas)


