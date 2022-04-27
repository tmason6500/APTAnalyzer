
# Python program to create
# a pdf file
  
import pandas as pd
import numpy as np
from fpdf import *
import RAPTORFunctions as apt
  
  
# save FPDF() class into a 
# variable pdf
pdf = FPDF()
techniques_df, tactics_df, groups_df, software_df, mitigations_df, gfr_df, relationships_df = apt.buildDataFrames()
groups = {'G0130':95, 'G0100':95, 'G0080':62, 'G0035':70, 'G0125':94, 'G0032':83, 'G0036':55}

# Populating Groups by % and linking to data
nine = []
eight = []
seven = []
six = []
five = []
for key in groups:
    # 90+% Groups
    if groups[key] >= 90:
        nine.append(key)
    # 89% - 80% Groups
    elif groups[key] >= 80 and groups[key] < 90:
        eight.append(key)
    # 79% - 70% Groups
    elif groups[key] >= 70 and groups[key] < 80:
        seven.append(key)
    # 69% - 60% Groups
    elif groups[key] >= 60 and groups[key] < 70:
        six.append(key)
    # 59% - 50% Groups
    elif groups[key] >= 50 and groups[key] < 60:
        five.append(key)
  
# Add a page
pdf.add_page()
pdf.add_font('Arial', '', 'c:/windows/fonts/arial.ttf', uni=True)  # fixes unicode issue with the single quotation
# set style and size of header
pdf.set_font('Arial','B',25)
pdf.cell(80)
pdf.cell(30,10,'R.A.P.T.O.R.',0,0,'C')
pdf.ln(20)

# 90+% Groups
pdf.set_font("Arial", size = 20)
pdf.cell(80)
pdf.cell(30, 10, txt="+90% Groups", align = 'C')
pdf.set_font("Arial", size = 12)
pdf.ln(20)

for i in range(len(nine)):
    pdf.multi_cell(190, 10, txt="{}".format(apt.getData(groups_df, nine[i], 'name')),align = 'L')
    desc = apt.getData(groups_df, nine[i], 'description')
    desc = apt.fix_pdf_description(desc)
    pdf.multi_cell(190, 10, txt="Description: {}".format(desc),align = 'L')
    pdf.ln(10)
    pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(groups_df, nine[i], 'associated groups')),align = 'L')
    pdf.ln(20)

# 89% - 80% Groups
pdf.add_page()
pdf.set_font("Arial", size = 20)
pdf.cell(80)
pdf.cell(30, 10, txt="89% - 80% Groups", align = 'C')
pdf.set_font("Arial", size = 12)
pdf.ln(20)

for i in range(len(eight)):
    pdf.multi_cell(190, 10, txt="{}".format(apt.getData(groups_df, eight[i], 'name')),align = 'L')
    desc = apt.getData(groups_df, eight[i], 'description')
    desc = apt.fix_pdf_description(desc)
    pdf.multi_cell(190, 10, txt="Description: {}".format(desc),align = 'L')
    pdf.ln(10)
    pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(groups_df, eight[i], 'associated groups')),align = 'L')
    pdf.ln(20)

# 79% - 70% Groups
pdf.add_page()
pdf.set_font("Arial", size = 20)
pdf.cell(80)
pdf.cell(30, 10, txt="79% - 70% Groups", align = 'C')
pdf.set_font("Arial", size = 12)
pdf.ln(20)

for i in range(len(seven)):
    pdf.multi_cell(190, 10, txt="{}".format(apt.getData(groups_df, seven[i], 'name')),align = 'L')
    desc = apt.getData(groups_df, seven[i], 'description')
    #desc = apt.fix_pdf_description(desc)
    pdf.multi_cell(190, 10, txt="Description: {}".format(desc),align = 'L')
    pdf.ln(10)
    pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(groups_df, seven[i], 'associated groups')),align = 'L')
    pdf.ln(20)

# 69% - 60% Groups
pdf.add_page()
pdf.set_font("Arial", size = 20)
pdf.cell(80)
pdf.cell(30, 10, txt="69% - 60% Groups", align = 'C')
pdf.set_font("Arial", size = 12)
pdf.ln(20)
for i in range(len(six)):
    pdf.multi_cell(190, 10, txt="{}".format(apt.getData(groups_df, six[i], 'name')),align = 'L')
    desc = apt.getData(groups_df, six[i], 'description')
    desc = apt.fix_pdf_description(desc)
    pdf.multi_cell(190, 10, txt="Description: {}".format(desc),align = 'L')
    pdf.ln(10)
    pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(groups_df, six[i], 'associated groups')),align = 'L')
    pdf.ln(20)

# 59% - 50% Groups
pdf.add_page()
pdf.set_font("Arial", size = 20)
pdf.cell(80)
pdf.cell(30, 10, txt="59% - 50% Groups", align = 'C')
pdf.set_font("Arial", size = 12)
pdf.ln(20)
for i in range(len(five)):
    pdf.multi_cell(190, 10, txt="{}".format(apt.getData(groups_df, five[i], 'name')),align = 'L')
    desc = apt.getData(groups_df, five[i], 'description')
    #desc = apt.fix_pdf_description(desc)
    pdf.multi_cell(190, 10, txt="Description: {}".format(desc),align = 'L')
    pdf.ln(10)
    pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(groups_df, five[i], 'associated groups')),align = 'L')
    pdf.ln(20)
  
# save the pdf with name .pdf
pdf.output("RAPTOR.pdf")
