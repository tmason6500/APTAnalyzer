
# Python program to create
# a pdf file

import pandas as pd
import numpy as np
from fpdf import *
import RAPTORFunctions as apt


def pdfReport(groups: dict):
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()
    techniques_df, tactics_df, groups_df, software_df, mitigations_df, gfr_df, relationships_df = apt.buildDataFrames()
    groups = {'G0024':90, 'G0100':60, 'G0080':92, 'G0035':70, 'G0125':80, 'G0032':83, 'G0036':55}

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
    pdf.add_font('DejaVu', '', './PDFFiles/DejjaVuSansCondensed.tff', uni=True)  # added line
    # set style and size of header
    pdf.set_font('DejaVu','B',25)
    pdf.cell(80)
    pdf.cell(30,10,'R.A.P.T.O.R.',0,0,'C')
    pdf.ln(20)

    # 90+% Groups
    if nine != []:
        pdf.set_font("DejaVu", size = 20)
        pdf.cell(80)
        pdf.cell(30, 10, txt="+90% Match", align = 'C')
        pdf.set_font("DejaVu", size = 12)
        pdf.ln(20)

        for i in range(len(nine)):
            pdf.set_font("DejaVu", size = 16)
            pdf.multi_cell(190, 10, txt="{}".format(apt.getData(groups_df, nine[i], 'name')),align = 'L')
            pdf.set_font("DejaVu", size = 12)
            pdf.ln(5)
            desc = apt.getData(groups_df, nine[i], 'description')
            desc = apt.fix_pdf_description(desc)
            pdf.multi_cell(190, 10, txt="Description: {}".format(desc),align = 'L')
            pdf.ln(10)
            pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(groups_df, nine[i], 'associated groups')),align = 'L')
            pdf.ln(10)
            techniques = apt.getTechniquesByGroup(relationships_df, nine[i])
            for i in range(len(techniques)):
                pdf.multi_cell(190, 10, txt="Techniques: {}".format(apt.getData(techniques_df, techniques[i], 'name')),align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                pdf.multi_cell(180, 10, txt="Description: {}".format(apt.getData(techniques_df, techniques[i], 'description')),align = 'L')
                mitigations = apt.mitigationsByTechnique(relationships_df, techniques[i])
                if mitigations != []:
                    for j in range(len(mitigations)):
                        pdf.ln(5)
                        pdf.cell(20)
                        pdf.multi_cell(170, 10, txt="Mitigation: {}".format(apt.getData(mitigations_df, mitigations[j], 'name')),align = 'L')
                        pdf.ln(5)
                        pdf.cell(30)
                        pdf.multi_cell(160, 10, txt="{}".format(apt.getData(mitigations_df, mitigations[j], 'description')),align = 'L')
                pdf.ln(10)



        pdf.add_page()

    # 89% - 80% Group
    if eight != []:
        pdf.set_font("DejaVu", size = 20)
        pdf.cell(80)
        pdf.cell(30, 10, txt="89% - 80% Match", align = 'C')
        pdf.set_font("DejaVu", size = 12)
        pdf.ln(20)

        for i in range(len(eight)):
            pdf.set_font("DejaVu", size = 16)
            pdf.multi_cell(190, 10, txt="{}".format(apt.getData(groups_df, eight[i], 'name')),align = 'L')
            pdf.set_font("DejaVu", size = 12)
            pdf.ln(5)
            desc = apt.getData(groups_df, eight[i], 'description')
            desc = apt.fix_pdf_description(desc)
            pdf.multi_cell(190, 10, txt="Description: {}".format(desc),align = 'L')
            pdf.ln(10)
            pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(groups_df, eight[i], 'associated groups')),align = 'L')
            pdf.ln(10)
            techniques = apt.getTechniquesByGroup(relationships_df, eight[i])
            for i in range(len(techniques)):
                pdf.multi_cell(190, 10, txt="Techniques: {}".format(apt.getData(techniques_df, techniques[i], 'name')),align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                pdf.multi_cell(180, 10, txt="Description: {}".format(apt.getData(techniques_df, techniques[i], 'description')),align = 'L')
                mitigations = apt.mitigationsByTechnique(relationships_df, techniques[i])
                if mitigations != []:
                    for j in range(len(mitigations)):
                        pdf.ln(5)
                        pdf.cell(20)
                        pdf.multi_cell(170, 10, txt="Mitigation: {}".format(apt.getData(mitigations_df, mitigations[j], 'name')),align = 'L')
                        pdf.ln(5)
                        pdf.cell(30)
                        pdf.multi_cell(160, 10, txt="{}".format(apt.getData(mitigations_df, mitigations[j], 'description')),align = 'L')
                pdf.ln(10)
        pdf.add_page()

    # 79% - 70% Groups
    if seven != []:
        pdf.set_font("DejaVu", size = 20)
        pdf.cell(80)
        pdf.cell(30, 10, txt="79% - 70% Match", align = 'C')
        pdf.set_font("DejaVu", size = 12)
        pdf.ln(20)

        for i in range(len(seven)):
            pdf.set_font("DejaVu", size = 16)
            pdf.multi_cell(190, 10, txt="{}".format(apt.getData(groups_df, seven[i], 'name')),align = 'L')
            pdf.set_font("DejaVu", size = 20)
            pdf.ln(5)
            desc = apt.getData(groups_df, seven[i], 'description')
            #desc = apt.fix_pdf_description(desc)
            pdf.multi_cell(190, 10, txt="Description: {}".format(desc),align = 'L')
            pdf.ln(10)
            pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(groups_df, seven[i], 'associated groups')),align = 'L')
            pdf.ln(10)
            techniques = apt.getTechniquesByGroup(relationships_df, seven[i])
            for i in range(len(techniques)):
                pdf.multi_cell(190, 10, txt="Techniques: {}".format(apt.getData(techniques_df, techniques[i], 'name')),align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                pdf.multi_cell(180, 10, txt="Description: {}".format(apt.getData(techniques_df, techniques[i], 'description')),align = 'L')
                mitigations = apt.mitigationsByTechnique(relationships_df, techniques[i])
                if mitigations != []:
                    for j in range(len(mitigations)):
                        pdf.ln(5)
                        pdf.cell(20)
                        pdf.multi_cell(170, 10, txt="Mitigation: {}".format(apt.getData(mitigations_df, mitigations[j], 'name')),align = 'L')
                        pdf.ln(5)
                        pdf.cell(30)
                        pdf.multi_cell(160, 10, txt="{}".format(apt.getData(mitigations_df, mitigations[j], 'description')),align = 'L')
                pdf.ln(10)
        pdf.add_page()

    # 69% - 60% Groups
    if six != []:
        pdf.set_font("DejaVu", size = 20)
        pdf.cell(80)
        pdf.cell(30, 10, txt="69% - 60% Match", align = 'C')
        pdf.set_font("DejaVu", size = 12)
        pdf.ln(20)
        for i in range(len(six)):
            pdf.set_font("DejaVu", size = 16)
            pdf.multi_cell(190, 10, txt="{}".format(apt.getData(groups_df, six[i], 'name')),align = 'L')
            pdf.set_font("DejaVu", size = 12)
            pdf.ln(5)
            desc = apt.getData(groups_df, six[i], 'description')
            desc = apt.fix_pdf_description(desc)
            pdf.multi_cell(190, 10, txt="Description: {}".format(desc),align = 'L')
            pdf.ln(10)
            pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(groups_df, six[i], 'associated groups')),align = 'L')
            pdf.ln(10)
            techniques = apt.getTechniquesByGroup(relationships_df, six[i])
            for i in range(len(techniques)):
                pdf.multi_cell(190, 10, txt="Techniques: {}".format(apt.getData(techniques_df, techniques[i], 'name')),align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                pdf.multi_cell(180, 10, txt="Description: {}".format(apt.getData(techniques_df, techniques[i], 'description')),align = 'L')
                mitigations = apt.mitigationsByTechnique(relationships_df, techniques[i])
                if mitigations != []:
                    for j in range(len(mitigations)):
                        pdf.ln(5)
                        pdf.cell(20)
                        pdf.multi_cell(170, 10, txt="Mitigation: {}".format(apt.getData(mitigations_df, mitigations[j], 'name')),align = 'L')
                        pdf.ln(5)
                        pdf.cell(30)
                        pdf.multi_cell(160, 10, txt="{}".format(apt.getData(mitigations_df, mitigations[j], 'description')),align = 'L')
                pdf.ln(10)

        pdf.add_page()

    # 59% - 50% Groups
    if five != []:
        pdf.set_font("DejaVu", size = 20)
        pdf.cell(80)
        pdf.cell(30, 10, txt="59% - 50% Match", align = 'C')
        pdf.set_font("DejaVu", size = 12)
        pdf.ln(20)
        for i in range(len(five)):
            pdf.set_font("DejaVu", size = 16)
            pdf.multi_cell(190, 10, txt="{}".format(apt.getData(groups_df, five[i], 'name')),align = 'L')
            pdf.set_font("DejaVu", size = 12)
            pdf.ln(5)
            desc = apt.getData(groups_df, five[i], 'description')
            #desc = apt.fix_pdf_description(desc)
            pdf.multi_cell(190, 10, txt="Description: {}".format(desc),align = 'L')
            pdf.ln(10)
            pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(groups_df, five[i], 'associated groups')),align = 'L')
            pdf.ln(10)
            techniques = apt.getTechniquesByGroup(relationships_df, five[i])
            for i in range(len(techniques)):
                pdf.multi_cell(190, 10, txt="Techniques: {}".format(apt.getData(techniques_df, techniques[i], 'name')),align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                pdf.multi_cell(180, 10, txt="Description: {}".format(apt.getData(techniques_df, techniques[i], 'description')),align = 'L')
                mitigations = apt.mitigationsByTechnique(relationships_df, techniques[i])
                if mitigations != []:
                    for j in range(len(mitigations)):
                        pdf.ln(5)
                        pdf.cell(20)
                        pdf.multi_cell(170, 10, txt="Mitigation: {}".format(apt.getData(mitigations_df, mitigations[j], 'name')),align = 'L')
                        pdf.ln(5)
                        pdf.cell(30)
                        pdf.multi_cell(160, 10, txt="{}".format(apt.getData(mitigations_df, mitigations[j], 'description')),align = 'L')
                pdf.ln(10)

    # save the pdf with name .pdf
    pdf.output("./PDFFiles/RAPTOR.pdf")
