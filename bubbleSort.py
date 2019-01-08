# Bubble sort

def bubbleSort(dataset):
    # TODO
    for i in range(len(dataset) -1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                t = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = t
                #(dataset[j], dataset[j+1]) = (dataset[j+1], dataset[j])
    print("Curret state: ", dataset)

def main():
    list1=[6,67,20,18]
    print("Initial state: ", list1)
    bubbleSort(list1)
    print("Result: ", list1)

if __name__=="__main__":
    main()
