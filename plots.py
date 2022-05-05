from Bio import SeqIO
import xlsxwriter
import pandas as pd
import openpyxl
from reportlab.lib.units import cm
from Bio.Graphics import BasicChromosome

#entries = [
#    ("Chr I", "CHR_I/NC_003070.gbk"),
#    ("Chr II", "CHR_II/NC_003071.gbk"),
#    ("Chr III", "CHR_III/NC_003074.gbk"),
#    ("Chr IV", "CHR_IV/NC_003075.gbk"),
#    ("Chr V", "CHR_V/NC_003076.gbk"),
#]
entries = ["Chr1", "Chr2", "Chr3", "Chr4", "Chr5"]
max_len = 3133627  # Could compute this from the entries dict
telomere_length = 10000  # For illustration

chr_diagram = BasicChromosome.Organism()
chr_diagram.page_size = (32 * cm, 21 * cm)  # A4 landscape
seq = SeqIO.parse("Bduncani_v1.fa", "fasta")
record_dict = SeqIO.to_dict(seq)

index = 0
for ch in entries:
    #record = record_dict[ch]
    #length = len(record.seq)
    record = SeqIO.read(ch+"_gene.gb", "genbank")
    length = len(record)
    #features = [f for f in record.features if f.type == "gene"]
    # Record an Artemis style integer color in the feature's qualifiers,
    # 1 = dark grey, 2 = red, 3 = green, 4 = blue, 5 =cyan, 6 = magenta, 10 = orange
    features = []
    for f in record.features:
        """
        if f.type == "gene1":
            f.qualifiers["color"] = [2]
            features.append(f)
        elif f.type == "gene2":
            f.qualifiers["color"] = [3]
            features.append(f)
        elif f.type == "gene3":
            f.qualifiers["color"] = [4]
            features.append(f)
        elif f.type == "gene4":
            f.qualifiers["color"] = [5]
            features.append(f)
        elif f.type == "gene5":
            f.qualifiers["color"] = [6]
            features.append(f)
        elif f.type == "gene6":
            f.qualifiers["color"] = [10]
            features.append(f)
        elif f.type == "gene7": # gpi: brown
            f.qualifiers["color"] = [11]
            features.append(f)
        elif f.type == "gene8": # ap: light sky blue
            f.qualifiers["color"] = [9]
            features.append(f)
        """
        if f.type == "gene9":
            f.qualifiers["color"] = [2]
            features.append(f)
        elif f.type == "mRNA":
            f.qualifiers["color"] = [1]
            features.append(f)
    #for f in features:
    #    f.qualifiers["color"] = [2]
    #features2 = [f for f in record.features if f.type == "centromere"]
    #for f in features2:
    #    f.qualifiers["color"] = [3]
    #features = []
    #for ID in gene_dict.keys():


    cur_chromosome = BasicChromosome.Chromosome(ch)
    # Set the scale to the MAXIMUM length plus the two telomeres in bp,
    # want the same scale used on all five chromosomes so they can be
    # compared to each other
    cur_chromosome.scale_num = max_len + 2 * telomere_length

    # Add an opening telomere
    start = BasicChromosome.TelomereSegment()
    start.scale = telomere_length
    cur_chromosome.add(start)

    # Add a body - again using bp as the scale length here.
    body = BasicChromosome.AnnotatedChromosomeSegment(length, features)
    body.scale = length
    cur_chromosome.add(body)

    # Add a closing telomere
    end = BasicChromosome.TelomereSegment(inverted=True)
    end.scale = telomere_length
    cur_chromosome.add(end)

    # This chromosome is done
    chr_diagram.add(cur_chromosome)

chr_diagram.draw("duplicate_genes.pdf", "")
