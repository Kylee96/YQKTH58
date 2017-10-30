#Task 3
dna1 = "ACTCGGTAA"

# Things in a function stay in a function, everytime you use a new variable inside a function, you must define it
# What is in the bracket after defining the function (dna) is different from what is outside (x)
print "Using the function method,"
# Defining the function for the reverse method
def reverse_dna(dna):
    rev = ""
    final = ""
    for i in range(0,len(dna)):
        rev = dna[len(dna)-i-1]
        final = final + rev
    return final
# Saving it as a variable for future use
a = reverse_dna(dna1)
print "Reverse of dna1 is:" ,a

# Trying out the reverse function with other examples of DNA Strands
dna2 = "AGCTCTAGC"
print "Reverse of dna2 is:", reverse_dna(dna2)
dna3 = "TGCACATGG"
print "Reverse of dna3 is:", reverse_dna(dna3)
dna4 = "GCCATTACG"
print "Reverse of dna4 is:", reverse_dna(dna4)
dna5 = "CCTAGGACT"
print "Reverse of dna5 is:", reverse_dna(dna5)

# Defining the function for the complement method
def complement_dna(dna):
    newdna = ''
    for i in range (0, len(dna)):
        if dna[i] == "T":
            newdna += "A"
        if dna[i] == "A":
            newdna += "T"
        if dna[i] == "G":
            newdna += "C"
        if dna[i] == "C":
            newdna += "G"
    return newdna
print "Complement of dna1 is:", complement_dna(dna1)

# Defining the function for the reverse complement method
def reverse_complement(newdna):
    newdna1 = ''
    for i in range (0, len(newdna)):
        if newdna[i] == "T":
            newdna1 += "A"
        if newdna[i] == "A":
            newdna1 += "T"
        if newdna[i] == "G":
            newdna1 += "C"
        if newdna[i] == "C":
            newdna1 += "G"
    return newdna1
print "Reverse complement of dna1 is:", reverse_complement(a)

# Task 4
print ''
print "Using the dictionary method,"
# Mapping keys to values in the dictionary
dictionary = {'A' : 'T', 'T' : 'A', 'C':'G', 'G' : 'C'}

# Finding the complement dna using the dictionary method
def complement_dna(dna):
    dna = list(dna)
    newdna = []
    for i in dna:
        newdna.append(dictionary[i])
    return newdna
print "Complement of dna1 is:", "".join(complement_dna(dna1))

# Finding the reverse complement dna using the dictionary method
def reverse_complement(dna):
    dna = reverse_dna(dna)
    dna = complement_dna(dna)
    return dna
print "Reverse complement of dna1 is:", "".join(reverse_complement(dna1))


