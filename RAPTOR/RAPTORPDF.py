# Python program to create
# a pdf file

import pandas as pd
import numpy as np
from fpdf import *
import RAPTORFunctions as apt

Debug = False
if Debug:
    groups = {'G0024':90, 'G0100':60, 'G0080':92, 'G0035':70, 'G0125':80, 'G0032':83, 'G0036':55}

pdf = FPDF()

def addGroup(group: dict, string: str):
    if group != []:
        if string != '':
            pdf.set_font("DejaVu", size = 20)
            pdf.cell(80)
            pdf.cell(30, 10, txt="{}".format(string), align = 'C')
            pdf.set_font("DejaVu", size = 12)
            pdf.ln(20)

        for i in range(len(group)):
            pdf.set_font("DejaVu", size = 16)
            pdf.multi_cell(190, 10, txt="{}".format(apt.getData(apt.groups_df, group[i], 'name')),align = 'L')
            pdf.set_font("DejaVu", size = 12)
            pdf.ln(5)
            desc = apt.getData(apt.groups_df, group[i], 'description')
            desc = apt.fix_pdf_description(desc)
            pdf.multi_cell(190, 10, txt="{}".format(desc),align = 'L')
            pdf.ln(10)
            pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(apt.groups_df, group[i], 'associated groups')),align = 'L')
            pdf.ln(10)
            software = apt.getSoftwareByGroup(apt.relationships_df, group[i])
            pdf.multi_cell(190, 10, txt="Software:  ", align = 'L')
            for j in range(len(software)):
                pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.software_df, software[j], 'name')), align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                pdf.multi_cell(170, 10, txt="{}".format(apt.getData(apt.software_df, software[j], 'description')),align = 'L')
            techniques = apt.getTechniquesByGroup(apt.relationships_df, group[i])
            pdf.multi_cell(190, 10, txt="Techniques: ", align = 'L')
            for j in range(len(techniques)):
                pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.techniques_df, techniques[j], 'name')),align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                pdf.multi_cell(170, 10, txt="{}".format(apt.getData(apt.techniques_df, techniques[j], 'description')),align = 'L')
                mitigations = apt.mitigationsByTechnique(apt.relationships_df, techniques[j])
                if mitigations != []:
                    pdf.multi_cell(170, 10, txt="Mitigation: ", align = 'L')
                    for k in range(len(mitigations)):
                        pdf.ln(5)
                        pdf.cell(20)
                        pdf.multi_cell(160, 10, txt="{}".format(apt.getData(apt.mitigations_df, mitigations[k], 'name')),align = 'L')
                        pdf.ln(5)
                        pdf.cell(30)
                        pdf.multi_cell(150, 10, txt="{}".format(apt.getData(apt.mitigations_df, mitigations[k], 'description')),align = 'L')
                pdf.ln(10)

        pdf.add_page()

def pdfReport(groups: dict):

    # Populating Groups by % and linking to data
    nine = []
    eight = []
    seven = []
    six = []
    five = []
    single=[]
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
        else:
            single.append(key)


    # Add a page
    pdf.add_page()
    pdf.add_font('DejaVu', '', './PDFFiles/DejaVuSans.ttf', uni=True)  # added line
    # set style and size of header
    pdf.set_font('DejaVu','',25)
    pdf.cell(80)
    pdf.cell(30,10,'R.A.P.T.O.R.',0,0,'C')
    pdf.ln(20)

    # 90+% Groups
    addGroup(nine, '90+% Groups')

    # 89% - 80% Group
    addGroup(eight, '89% - 80% Groups')

    # 79% - 70% Groups
    addGroup(seven, '79% - 70% Groups')

    # 69% - 60% Groups
    addGroup(six, '69% - 60% Groups')

    # 59% - 50% Groups
    addGroup(five, '59% - 50% Groups')

    # save the pdf with name .pdf
    pdf.output("./PDFFiles/RAPTOR.pdf")

def grouppdfReport(groups: dict, name):
    # Add a page
    pdf.add_page()
    pdf.add_font('DejaVu', '', './PDFFiles/DejaVuSans.ttf', uni=True)  # added line
    # set style and size of header
    pdf.set_font('DejaVu','',25)
    pdf.cell(80)
    pdf.cell(30,10,'R.A.P.T.O.R.',0,0,'C')
    pdf.ln(20)

    addGroup(groups, '')

    # save the pdf with name .pdf
    output_path='./PDFFiles/'+name+'.pdf'
    pdf.output(output_path)

if Debug:
    pdfReport(groups)