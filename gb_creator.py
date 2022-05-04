import xlsxwriter
import pandas as pd
import openpyxl


def gb_writer(gene_dict, genes, fs, fam):
    name = "gene"+str(fam)
    for g in genes:
        tup = gene_dict[g]
        if tup[0] == "chr1":
            fs[0].write("     "+name)
            if tup[3] == '+':
                fs[0].write("           "+str(tup[1])+".."+str(tup[2])+"\n")
            elif tup[3] == '-':
                fs[0].write("           complement(" + str(tup[1]) + ".." + str(tup[2]) + ")\n")
            fs[0].write("                     /gene="+"\""+g+"\"\n")
        elif tup[0] == "chr2":
            fs[1].write("     " + name)
            if tup[3] == '+':
                fs[1].write("           " + str(tup[1]) + ".." + str(tup[2]) + "\n")
            elif tup[3] == '-':
                fs[1].write("           complement(" + str(tup[1]) + ".." + str(tup[2]) + ")\n")
            fs[1].write("                     /gene=" + "\"" + g + "\"\n")
        elif tup[0] == "chr3":
            fs[2].write("     " + name)
            if tup[3] == '+':
                fs[2].write("           " + str(tup[1]) + ".." + str(tup[2]) + "\n")
            elif tup[3] == '-':
                fs[2].write("           complement(" + str(tup[1]) + ".." + str(tup[2]) + ")\n")
            fs[2].write("                     /gene=" + "\"" + g + "\"\n")
        elif tup[0] == "chr4":
            fs[3].write("     " + name)
            if tup[3] == '+':
                fs[3].write("           " + str(tup[1]) + ".." + str(tup[2]) + "\n")
            elif tup[3] == '-':
                fs[3].write("           complement(" + str(tup[1]) + ".." + str(tup[2]) + ")\n")
            fs[3].write("                     /gene=" + "\"" + g + "\"\n")
        elif tup[0] == "chr5":
            fs[4].write("     " + name)
            if tup[3] == '+':
                fs[4].write("           " + str(tup[1]) + ".." + str(tup[2]) + "\n")
            elif tup[3] == '-':
                fs[4].write("           complement(" + str(tup[1]) + ".." + str(tup[2]) + ")\n")
            fs[4].write("                     /gene=" + "\"" + g + "\"\n")


entries = ["chr1", "chr2", "chr3", "chr4", "chr5"]
families = pd.read_excel("gene_family.xlsx", engine="openpyxl")
gene_list = pd.read_excel("gene_list.xlsx", engine="openpyxl")

#fam = "RAP domain"
fam = open("gene_family.txt", "r")
genes = []
while True:
    line = fam.readline().strip()
    if not line:
        break
    #if line[1:-1] == fam:
    #    genes = f.readline().strip().split(",")
    #    break
    genes += fam.readline().strip().split(",")
fam.close()

gene_dict = {}
for ID in genes:
    val = gene_list[gene_list["ID"] == ID]
    tup = str(val.values[0])[1:-1].split()
    ch = tup[1][1:-1]
    start = int(tup[2])
    end = int(tup[3])
    sign = tup[4][1:-1]
    if ch in entries:
        gene_dict[ID] = (ch, start, end, sign)

gpi = open("MGFs/gpi.txt", "r")
ap = open("MGFs/ap.txt", "r")
gpi_gene, ap_gene = [], []
while True:
    line = gpi.readline().strip()
    if not line:
        break
    g = line.split("-")[0]
    if g in gene_dict.keys():
        gpi_gene.append(g)
while True:
    line = ap.readline().strip()
    if not line:
        break
    g = line.split("-")[0]
    if g in gene_dict.keys():
        ap_gene.append(g)
print(len(gpi_gene), len(ap_gene))

ufam1 = open("MGFs/umgf1.txt", "r")
ufam2 = open("MGFs/umgf2.txt", "r")
ufam3 = open("MGFs/umgf3.txt", "r")
ofam1 = open("MGFs/OG6_101304.txt", "r")
ofam2 = open("MGFs/OG6_101515.txt", "r")
ofam3 = open("MGFs/OG6_103347.txt", "r")

gene1, gene2, gene3 = [], [], []
genes_1 = ufam1.readline().strip().split("\t")
print(len(genes_1))
#gene1 = [g.split("-")[0] for g in genes_1]
for g in genes_1:
    n = g.split("-")[0]
    if n in gene_dict.keys():
        gene1.append(n)
ufam1.close()
genes_2 = ufam2.readline().strip().split("\t")
print(len(genes_2))
#gene2 = [g.split("-")[0] for g in genes_2]
for g in genes_2:
    n = g.split("-")[0]
    if n in gene_dict.keys():
        gene2.append(n)
ufam2.close()
genes_3 = ufam3.readline().strip().split("\t")
print(len(genes_3))
#gene3 = [g.split("-")[0] for g in genes_3]
for g in genes_3:
    n = g.split("-")[0]
    if n in gene_dict.keys():
        gene3.append(n)
ufam3.close()

gene4, gene5, gene6 = [], [], []
while True:
    line = ofam1.readline().strip()
    if not line:
        break
    g = line.split("-")[0]
    if g in gene_dict.keys():
        gene4.append(g)
while True:
    line = ofam2.readline().strip()
    if not line:
        break
    g = line.split("-")[0]
    if g in gene_dict.keys():
        gene5.append(g)
while True:
    line = ofam3.readline().strip()
    if not line:
        break
    g = line.split("-")[0]
    if g in gene_dict.keys():
        gene6.append(g)
ofam1.close()
ofam2.close()
ofam3.close()

print(len(gene1), len(gene2), len(gene3), len(gene4), len(gene5), len(gene6))

fs = [open("temp/chr1.txt", "w"), open("temp/chr2.txt", "w"), open("temp/chr3.txt", "w"), open("temp/chr4.txt", "w"), open("temp/chr5.txt", "w")]
# gene1
gb_writer(gene_dict, gene1, fs, 1)
# gene2
gb_writer(gene_dict, gene2, fs, 2)
# gene3
gb_writer(gene_dict, gene3, fs, 3)
# gene4
gb_writer(gene_dict, gene4, fs, 4)
# gene5
gb_writer(gene_dict, gene5, fs, 5)
# gene6
gb_writer(gene_dict, gene6, fs, 6)
# gene7
gb_writer(gene_dict, gpi_gene, fs, 7)  # color: brown
# gene8
gb_writer(gene_dict, ap_gene, fs, 8)  # color: light sky blue
for f in fs:
    f.close()
