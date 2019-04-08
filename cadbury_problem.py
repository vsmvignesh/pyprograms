#!/usr/bin/python
import sys

def create_combination(l1,l2,b1,b2):
    tot_count=0
    for l in range(l1,l2+1):
        for b in range(b1,b2+1):
            ret=count_bars(l,b)
            print("Chocolate Bar size ({0} x {1}), can be distributed to \"{2}\" children...".format(l,b,ret))
            tot_count=tot_count+ret

    print("\nSo, total number of \"" + str(tot_count) + "\" children will have chocolates distributed to them...\n")
    return 0

def count_bars(l,b):
    count=0
    while(l!=b):
        if b>l :
            b=b-l
        else:
            l=l-b
        count+=1
    else:
        count+=1

    return count


def main():
    inp=input("Enter the lengths and breadths(len1, len2, brd1, brd2): ")
    l1,l2,b1,b2=inp[0], inp[1], inp[2], inp[3]

    ret=create_combination(l1,l2,b1,b2)

    if ret:
        sys.exit(1)
    else:
        return 0


if __name__=="__main__":
    main()
