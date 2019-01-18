def main():
    beginSet = [int(i) for i in input("Enter a set: ").split()]
    subMax = float('-inf')
    subCurr = float('-inf')
    subSpec = 0
    subBegin = 0
    subEnd = 0
    currPos = 0
    maxBegin = 0
    maxEnd = 0
    #Loop over the entire set
    for x in beginSet:
        #If speculative additions would be larger than the current subset
        #value, then there is no reason to ever add the current subset, so
        #get rid of it.
        if subSpec + subCurr + x < x:
            if subCurr > subMax:
                subMax = subCurr
                maxBegin = subBegin
                maxEnd = subEnd
            subCurr = x
            subSpec = 0
            subBegin = currPos
            subEnd = currPos
        else:
            #Check if x is greater than zero
             if x >= 0:
                #If adding x and all speculative adds are helpful,
                #then add them to the current subarray
                if subSpec + subCurr + x > subCurr:
                    subCurr = subCurr + x + subSpec
                    subEnd = currPos
                    subSpec = 0
                #Otherwise, speculatively add x
                else:
                    subSpec = subSpec + x
            #If x is negative, speculatively add it.
             else:
                subSpec = subSpec + x
        #See if there is a new max
        if subCurr > subMax:
            subMax = subCurr
            maxBegin = subBegin
            maxEnd = subEnd
        #Increment current position
        currPos = currPos + 1
    print("Total value: ", subMax)
    print("Starting index: ", maxBegin)
    print("Ending index: ", maxEnd)
main()
