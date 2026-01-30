STOP = {"TAA", "TAG", "TGA"}
E = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
acc = "NC_000913.3"  # E. coli K-12 MG1655 complete genome
params={"db":"nuccore","id":acc,"rettype":"fasta","retmode":"text"}