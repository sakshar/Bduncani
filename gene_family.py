import pandas as pd
import openpyxl
import xlsxwriter

df = pd.read_excel("Babesia_duncani_WA1.protein.compressed.xlsx", engine="openpyxl")
gene_fam = {}
for index, row in df.iterrows():
    name = row['Protein accession'].split("-")[0]
    families = row['InterPro annotations - accession'].split("|")
    for family in families:
        if family not in gene_fam:
            gene_fam[family] = []
        gene_fam[family] += [name]

#f = open("gene_family.txt", "w")
workbook = xlsxwriter.Workbook("gene_family.xlsx")
worksheet = workbook.add_worksheet("geneFamily")
i = 1
worksheet.write("A"+str(i), "family")
worksheet.write("B"+str(i), "genes")
for family in gene_fam.keys():
    i += 1
    worksheet.write("A" + str(i), family)
    worksheet.write("B" + str(i), (',').join(gene_fam[family]))
workbook.close()
