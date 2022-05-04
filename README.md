# Bduncani
Scripts and data for Bduncani genome project
The MGFs directory contains the list gene_ID for each gene_family in separate text files.
1. umgf1.txt for BdUMGF1
2. umgf2.txt for BdUMGF2
3. umgf3.txt for BdUMGF3
4. OG6_101304.txt for BdOMGF1
5. OG6_101515.txt for BdOMGF2
6. OG6_103347.txt for BdOMGF3
7. gpi.txt for GPI
8. ap.txt for AP2
The scripts:
# gene_collector.py:
It reads the Babesia_duncani_WA1.gff3 file and writes to a spreadsheet "gene_list.xlsx". The xlsx output contains the following information for each gene per row:
(ID, chr, start, end, sign)

# gb_creator.py:
The plotter expects the input data in .gb/.gbk format. To translate the gene_family information into a .gb/.gbk file per chromosome, it is required to run this script. It reads each file from MGFs directory and writes the relevant information for each gene per family into separate files for each chromosome. For example:
if a gene XXX_YYYY belongs to the family BdUMGF1 and located on the negative strand of chr2 spanning from 10000 to 15000, it will be written to temp/chr2.txt file as:
     gene1           complement(10000..15000)
                     /gene="XXX_YYYY"

After running the script, you have to manually copy the contents of this text file into the corresponding chrN_gene.gb file where N=[1,5]. Paste the contents between line 21 and the feature "CONTIG".

# plots.py:
It takes the whole genome Bduncani_v1.fa and the .gb/.gbk files for each chromosome as input. Then it assings different color for different gene families and produce the plot as gene_chrom.pdf. (Unfortunately, I couldn't find a way to add legends using this script)

# color.py:
It produces the legends in a plot named as legends.png
Then, manually take a screenshot of the legends from legends.png and save it as legends_crop.png

# image_inserter.py:
It takes the gene_chrom.pdf and legends_crop.png files as inputs and generates a new pdf file named gene_chrom_legends.pdf with the legends placed in the lower middle part of the page.
