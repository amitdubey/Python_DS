def findletterfrq(st,letter)->int:
    count =0
    for i in st:
        if i ==letter:
            count +=1
    return count


def main():
    st ='missipppi'
    letter ='i'
    print(findletterfrq(st,letter))


if __name__ == "__main__":
    main()
    