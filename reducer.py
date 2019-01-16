import sys

def reducer():

    # set variables
    salesTotal = 0
    lastStore = None

    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        if len(data) != 2:
            continue
        # this next line is called 'multiple assignment' in Python
        currentStore, currentSale = data

        # it's the point where we are moving from one store to the next store
        if lastStore and lastStore != currentStore:
            print "{0} {1}".format(lastStore, salesTotal)

            # reset total sales
            salesTotal = 0
        
        # set the last store to the current store we are working on
        lastStore = currentStore
        salesTotal += float(currentSale)

    if lastStore != None:
        print "{0} {1}".format(lastStore, salesTotal)
        
test_text = """Vancouver\t12.34
Vancouver\t99.07
Vancouver\t42.23
Toronto\t93.45
Toronto\t111.23"""

# This function allows you to test the mapper with the provided test string
if __name__ == "__main__":
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)
	reducer()
	sys.stdin = sys.__stdin__