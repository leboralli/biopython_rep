string = 'ACTTGAGCCAACATGGTGCATACTTCGTAGAAGCAGTCGCAGTTTTATCATCACAAGAATGAAGGCAGACTACGGTGGAAATAGGCTACTAATCCCGTCCTCCTAAAAGCTTAGTGGACACGGACCTGATACGCGGACTTACGTTTTATACCCGGATTACTTACCAGCGAGAGACGCTGCTTATGACTCCTCTTCATGGGACCCAATTGGGGACTAACTCGTAGGCCTTTAGGTGTAAGGCAAGATCTAGTACCTCACACTACACTCAAGTACATGCAGCTACCGGCCGTTCGCGAATCCTAGAGGAAGCACTGGGTCTCGCTCACAAAATTCGTGCCCCGGCAGAGCGACCCCGGGCTCCATGTAGTCAAACTGGTGAGTCAAGCGATCTGTATAGACAGAACCGACACTAACCAACACAAGGGACTCGCATCGGGTTTTTCCCTTGGAAATGGCCCGCCAGCATGTGATGCCATAATCCCTACCAGGAATATGCCGACAAGAATGTGCTTAGCTAAGTCGACCTAATATTTGCCTGAATCTCCGCCCTTCGTCCATGCTAGGAAAGCGTCAAGTCCCTTGGGTTTACCGCGGTCTAGTCGCTTGACAATTTCCGGCTATCCTTTGGACCAGGAGGTTACCTACTCCCTACGACAACCCCCTTCAAGCGTGGCACCTTCGGAATCTCCCCCCTTTTTAAACCAGGTACGCTTGGGGCTCCTCCTTCTAACTCGCTTAACTCGGCCGCGATCATTTCCGTGTCTGTCGCGGTGTCTTGATTCTCTGTGGGATTATATCTCGGGGAAGCCGGTTCGAATGGTTCCGGGAAGTTAGAATCTTATAAACTAGTGAAGATCGGTCAGGTACTATAGGTTACCACGGTTGCGATTATGTCTTACCGCGTGAACTGGTAGGACGTCTAGATGTTGAGTCACCTT'

string2 = 'ACTTTGGACAACATGGAGAGAAGGAAAGATACGTGGTCTCAACTGACTAAGGACGATACTATGGAAAAGGGGGCGTGTAAATCACGTAATTGTGCCGGCGTAAAAAACTGGCAGCTAATAGCCAGTGGGTTGGCGGGCTTTCATTTTTATTACGTATCACAGACGATTGTGCGTGTAGGCGCTAGCGATTTGATTAACGAAGACAATGGGGCACGTTCCCGCCGTCCGTTAGATGTTGAGTAAGTTCAAGTACTTTACGATTCGCATAAGTCCAAGCGCCAAACGACCGTTTCCGAATTCTAGCAGAAGCACAGGCGTCCTCTCGCAAATGTTGTGTGGAGGCCGCGAGTCCCCGTCCGCGATCAAGCCAAACAGGGATGACTCGAGAGACCTAGGGCGTGAGCCCCGACTAACCCATGCACACCACCCCGATAAGTATCGTCCGTCTGTAGTGGACCGCAAGCCCTTGGCGACAAAAGTCATACTATTCATATGACGTCGTCGTTCATTTAAATAGAGTCGTCCTGATACATTCCAGGATCTCGGCCCATCCTTGATGTTTCGAGCTGATGCCAGCCCGTGGTGTAGCAGCAAACTAGTCTGTGTGCGATGTCACACTAGGCTTAGGATCAGTCGGCAGCCCGCTTCGGAAGATAGCACAATTAATGGCGAGAACCTGAGTCTAACCCCAGGCTTGTTAACGTGGTACACTGAGGTCGCCTCGTACCACATCGAGTCACTCCACCGCGACCATACCAGAGGTGTCCGATGTTGCCTTGCACTCTCGTGGCTTAAGACTCCGGGCCACCTCTATCAATGGTAGGAGGCACACATATTCTCCAGAACTAGGGAACAGCCATTTGGAAGTGGAGTTCAACACAGTTGCGATTATCTCAATCCCCGAGCCCTCGCAAGAATTCTATACGGTGGTCTAGCCG'

string = list(string)
string2 = list(string2)

common = []

total = 0

for i,j in zip(string,string2):
    if i == j:
        common.append(i)

total = len(string) - len(common)

print (total)