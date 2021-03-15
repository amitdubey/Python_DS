def applypermutations(targetarray,givenaray):
    for i in range(len(a)):
        while perm[i] !=i:
            a[perm[i]],a[i]=a[i],a[perm[i]]
            perm[perm[i]],perm[i] =perm[i],perm[perm[i]]
            