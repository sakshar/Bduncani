import xlsxwriter


f = open("Babesia_duncani_WA1.gff3", "r")
line = f.readline().strip()
workbook = xlsxwriter.Workbook("gene_list.xlsx")
worksheet = workbook.add_worksheet("gene")
i = 1
worksheet.write("A"+str(i), "ID")  # 8
worksheet.write("B"+str(i), "chr")  # 0
worksheet.write("C"+str(i), "start")  # 3
worksheet.write("D"+str(i), "end")  # 4
worksheet.write("E"+str(i), "sign")  # 6
while True:
    line = f.readline()
    if not line:
        break
    words = line.strip().split()
    if words[0] == "contig5":
        words[0] = "chr5"
    if words[2] == "gene":
        i += 1
        worksheet.write("A" + str(i), words[8][:-1].split("=")[-1])  # 8
        worksheet.write("B" + str(i), words[0])  # 0
        worksheet.write("C" + str(i), words[3])  # 3
        worksheet.write("D" + str(i), words[4])  # 4
        worksheet.write("E" + str(i), words[6])  # 6
workbook.close()
f.close()
