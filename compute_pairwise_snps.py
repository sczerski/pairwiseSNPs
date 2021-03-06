# Please simply make any necessary changes depending on the number of strains/sequences you are analyzing.
# I will make into a generalized function eventually ;)
# -SC 3/10/12  (happy birthday to me)
#---------------------------------------------------------------------------------------------------

#def PairwiseDifSNPs(file, num_seqs)
#prior to reading your file, make a copy and eliminate the header. if you keep vars labels just skip first line

#initialize list to hold file lines
lines = []    

#read file, extract every line into list mylines
with open ("Path\\to\\my\\SNPsfile.txt", 'rt') as snpfile: #change 
    for line in snpfile:                
        lines.append(line)           

#initialize list to contain snps
mysnps = []

#extract only SNPs from file. This number would change depending on num of sequences
for element in mylines:
    mysnps.append(element[:3])

#remove any SNPs with gaps (entire "row")
coresnps = [ x for x in mysnps if "-" not in x ]

#total number of coresnps is the number of polymorphic positions in the alignment
totalsnps = len(coresnps)
print('Total number of polymorphic positions: ', totalsnps)

#create vector of snps for each strain #while true, do this for how many sequences
refsnp = []
midsnp = []
lastsnp = []
for snps in puresnps:
    refsnp.append(snps[0])
    midsnp.append(snps[1])
    lastsnp.append(snps[2])

#perform pairwise comparisons for each strain: 1v2, 2v3, 3v1 #for loop

#1v2
m=0
firstsecond=0
for r in refsnp:
    if r == midsnp[m]:
            ''
    elif r != midsnp[m]:
            firstsecond+=1
    m+=1

print(firstsecond)

#2v3
l=0
secondthird=0
for m in midsnp:
    if m == lastsnp[l]:
        ''
    elif m != lastsnp[l]:
        secondthird+=1
        
    l+=1
    
print(secondthird)

#3v1
r = 0
thirdfirst=0
for l in lastsnp:
    if l == refsnp[r]:
        ''
    elif l != refsnp[r]:
        thirdfirst+=1
        
    r+=1
    
print(thirdfirst)
