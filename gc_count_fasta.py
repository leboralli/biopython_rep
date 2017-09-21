from Bio import SeqIO

def count_gc(seq):
    total = seq.count('G') + seq.count('C')
    return (100*total)/len(seq)

dict = {}

with open('rosalind_gc.txt', 'rU') as handle:
    record_dict = SeqIO.to_dict(SeqIO.parse(handle, 'fasta'))
    for i in record_dict:
        print(record_dict[i].id)
        print(count_gc(record_dict[i].seq))
        dict[record_dict[i].id] = count_gc(record_dict[i].seq)
    maximum = max(dict,key=dict.get)
print('-----------------')
print (maximum)
print(max(dict.values()))
#print (record_dict)



    #for record in SeqIO.parse(handle, 'fasta'):
    #    print (record.id + '\n' + str(count_gc(record.seq)))
