import sys

def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        # what if there are not exactly 6 fields in that line?
        if len(data) != 6:
            continue
        
        store = data[2]
        cost = data[4]
        
        # Now print out the data that will be passed to the reducer
        print "{0} {1}".format(store, cost)
        
test_text = """2013-10-09\t13:22\tToronto\tFood\t99.95\tVisa
2013-10-09\t13:22\tVancouver\tMusic\t9.50\tMasterCard
2013-10-09 13:22:59 I/O Error
^d8x28orz28zoijzu1z1zp1OHH3du3ixwcz114<f
1\t2\t3"""

# This function allows you to test the mapper with the provided test string
if __name__ == "__main__":
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)
	mapper()
	sys.stdin = sys.__stdin__