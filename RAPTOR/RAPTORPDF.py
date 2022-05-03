# Python program to create
# a pdf file

from pydoc import describe
import pandas as pd
import numpy as np
from fpdf import *
import RAPTORFunctions as apt

Debug = False
if Debug:
    groups = {'G0024':90, 'G0100':60, 'G0080':92, 'G0035':70, 'G0125':80, 'G0032':83, 'G0036':55}
    group1 = {'G0024':90}

def pdfReport(groups: dict):
    pdf = FPDF()
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
    if nine != []:
        pdf.set_font("DejaVu", size = 20)
        pdf.cell(80)
        pdf.cell(30, 10, txt="+90% Match", align = 'C')
        pdf.set_font("DejaVu", size = 12)
        pdf.ln(20)

        for i in range(len(nine)):
            pdf.set_font("DejaVu", size = 16)
            pdf.multi_cell(190, 10, txt="{}".format(apt.getData(apt.groups_df, nine[i], 'name')),align = 'L')
            pdf.set_font("DejaVu", size = 12)
            pdf.ln(5)
            aptDesc = apt.getData(apt.groups_df, nine[i], 'description')
            aptDesc = apt.fix_pdf_description(aptDesc)
            pdf.multi_cell(180, 10, txt="{}".format(aptDesc),align = 'L')
            pdf.ln(10)
            pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(apt.groups_df, nine[i], 'associated groups')),align = 'L')
            pdf.ln(10)
            software = apt.getSoftwareByGroup(apt.relationships_df, nine[i])
            pdf.multi_cell(190, 10, txt="Software:  ", align = 'L')
            for j in range(len(software)):
                pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.software_df, software[j], 'name')), align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                softDesc = apt.getData(apt.software_df, software[j], 'description')
                softDesc = apt.fix_pdf_description(softDesc)
                pdf.multi_cell(170, 10, txt="{}".format(softDesc),align = 'L')
            techniques = apt.getTechniquesByGroup(apt.relationships_df, nine[i])
            pdf.multi_cell(190, 10, txt="Techniques: ", align = 'L')
            for j in range(len(techniques)):
                pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.techniques_df, techniques[j], 'name')),align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                techDesc = apt.getData(apt.techniques_df, techniques[j], 'description')
                techDesc = apt.fix_pdf_description(techDesc)
                pdf.multi_cell(170, 10, txt="{}".format(techDesc),align = 'L')
                mitigations = apt.mitigationsByTechnique(apt.relationships_df, techniques[j])
                if mitigations != []:
                    pdf.multi_cell(170, 10, txt="Mitigation: ", align = 'L')
                    for k in range(len(mitigations)):
                        pdf.ln(5)
                        pdf.cell(20)
                        pdf.multi_cell(160, 10, txt="{}".format(apt.getData(apt.mitigations_df, mitigations[k], 'name')),align = 'L')
                        pdf.ln(5)
                        pdf.cell(30)
                        mitDesc = apt.getData(apt.mitigations_df, mitigations[k], 'description')
                        mitDesc = apt.fix_pdf_description(mitDesc)
                        pdf.multi_cell(150, 10, txt="{}".format(mitDesc),align = 'L')
                pdf.ln(10)

    # 89% - 80% Group
    if eight != []:
        pdf.set_font("DejaVu", size = 20)
        pdf.cell(80)
        pdf.cell(30, 10, txt="89% - 80% Match", align = 'C')
        pdf.set_font("DejaVu", size = 12)
        pdf.ln(20)

        for i in range(len(eight)):
            pdf.set_font("DejaVu", size = 16)
            pdf.multi_cell(190, 10, txt="{}".format(apt.getData(apt.groups_df, eight[i], 'name')),align = 'L')
            pdf.set_font("DejaVu", size = 12)
            pdf.ln(5)
            aptDesc = apt.getData(apt.groups_df, eight[i], 'description')
            aptDesc = apt.fix_pdf_description(aptDesc)
            pdf.multi_cell(180, 10, txt="{}".format(aptDesc),align = 'L')
            pdf.ln(10)
            pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(apt.groups_df, eight[i], 'associated groups')),align = 'L')
            pdf.ln(10)
            software = apt.getSoftwareByGroup(apt.relationships_df, eight[i])
            pdf.multi_cell(190, 10, txt="Software:  ", align = 'L')
            for j in range(len(software)):
                pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.software_df, software[j], 'name')), align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                softDesc = apt.getData(apt.software_df, software[j], 'description')
                softDesc = apt.fix_pdf_description(softDesc)
                pdf.multi_cell(170, 10, txt="{}".format(softDesc),align = 'L')
            techniques = apt.getTechniquesByGroup(apt.relationships_df, eight[i])
            pdf.multi_cell(190, 10, txt="Techniques: ", align = 'L')
            for j in range(len(techniques)):
                pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.techniques_df, techniques[j], 'name')),align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                techDesc = apt.getData(apt.techniques_df, techniques[j], 'description')
                techDesc = apt.fix_pdf_description(techDesc)
                pdf.multi_cell(170, 10, txt="{}".format(techDesc),align = 'L')
                mitigations = apt.mitigationsByTechnique(apt.relationships_df, techniques[j])
                if mitigations != []:
                    pdf.multi_cell(170, 10, txt="Mitigation: ", align = 'L')
                    for k in range(len(mitigations)):
                        pdf.ln(5)
                        pdf.cell(20)
                        pdf.multi_cell(160, 10, txt="{}".format(apt.getData(apt.mitigations_df, mitigations[k], 'name')),align = 'L')
                        pdf.ln(5)
                        pdf.cell(30)
                        mitDesc = apt.getData(apt.mitigations_df, mitigations[k], 'description')
                        mitDesc = apt.fix_pdf_description(mitDesc)
                        pdf.multi_cell(150, 10, txt="{}".format(mitDesc),align = 'L')
                pdf.ln(10)

    # 79% - 70% Groups
    if seven != []:
        pdf.set_font("DejaVu", size = 20)
        pdf.cell(80)
        pdf.cell(30, 10, txt="79% - 70% Match", align = 'C')
        pdf.set_font("DejaVu", size = 12)
        pdf.ln(20)

        for i in range(len(seven)):
            pdf.set_font("DejaVu", size = 16)
            pdf.multi_cell(190, 10, txt="{}".format(apt.getData(apt.groups_df, seven[i], 'name')),align = 'L')
            pdf.set_font("DejaVu", size = 12)
            pdf.ln(5)
            aptDesc = apt.getData(apt.groups_df, seven[i], 'description')
            aptDesc = apt.fix_pdf_description(aptDesc)
            pdf.multi_cell(180, 10, txt="{}".format(aptDesc),align = 'L')
            pdf.ln(10)
            pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(apt.groups_df, seven[i], 'associated groups')),align = 'L')
            pdf.ln(10)
            software = apt.getSoftwareByGroup(apt.relationships_df, seven[i])
            pdf.multi_cell(190, 10, txt="Software:  ", align = 'L')
            for j in range(len(software)):
                pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.software_df, software[j], 'name')), align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                softDesc = apt.getData(apt.software_df, software[j], 'description')
                softDesc = apt.fix_pdf_description(softDesc)
                pdf.multi_cell(170, 10, txt="{}".format(softDesc),align = 'L')
            techniques = apt.getTechniquesByGroup(apt.relationships_df, seven[i])
            pdf.multi_cell(190, 10, txt="Techniques: ", align = 'L')
            for j in range(len(techniques)):
                pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.techniques_df, techniques[j], 'name')),align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                techDesc = apt.getData(apt.techniques_df, techniques[j], 'description')
                techDesc = apt.fix_pdf_description(techDesc)
                pdf.multi_cell(170, 10, txt="{}".format(techDesc),align = 'L')
                mitigations = apt.mitigationsByTechnique(apt.relationships_df, techniques[j])
                if mitigations != []:
                    pdf.multi_cell(170, 10, txt="Mitigation: ", align = 'L')
                    for k in range(len(mitigations)):
                        pdf.ln(5)
                        pdf.cell(20)
                        pdf.multi_cell(160, 10, txt="{}".format(apt.getData(apt.mitigations_df, mitigations[k], 'name')),align = 'L')
                        pdf.ln(5)
                        pdf.cell(30)
                        mitDesc = apt.getData(apt.mitigations_df, mitigations[k], 'description')
                        mitDesc = apt.fix_pdf_description(mitDesc)
                        pdf.multi_cell(150, 10, txt="{}".format(mitDesc),align = 'L')
                pdf.ln(10)

    # 69% - 60% Groups
    if six != []:
        pdf.set_font("DejaVu", size = 20)
        pdf.cell(80)
        pdf.cell(30, 10, txt="69% - 60% Match", align = 'C')
        pdf.set_font("DejaVu", size = 12)
        pdf.ln(20)

        for i in range(len(six)):
            pdf.set_font("DejaVu", size = 16)
            pdf.multi_cell(190, 10, txt="{}".format(apt.getData(apt.groups_df, six[i], 'name')),align = 'L')
            pdf.set_font("DejaVu", size = 12)
            pdf.ln(5)
            aptDesc = apt.getData(apt.groups_df, six[i], 'description')
            aptDesc = apt.fix_pdf_description(aptDesc)
            pdf.multi_cell(180, 10, txt="{}".format(aptDesc),align = 'L')
            pdf.ln(10)
            pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(apt.groups_df, six[i], 'associated groups')),align = 'L')
            pdf.ln(10)
            software = apt.getSoftwareByGroup(apt.relationships_df, six[i])
            pdf.multi_cell(190, 10, txt="Software:  ", align = 'L')
            for j in range(len(software)):
                pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.software_df, software[j], 'name')), align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                softDesc = apt.getData(apt.software_df, software[j], 'description')
                softDesc = apt.fix_pdf_description(softDesc)
                pdf.multi_cell(170, 10, txt="{}".format(softDesc),align = 'L')
            techniques = apt.getTechniquesByGroup(apt.relationships_df, six[i])
            pdf.multi_cell(190, 10, txt="Techniques: ", align = 'L')
            for j in range(len(techniques)):
                pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.techniques_df, techniques[j], 'name')),align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                techDesc = apt.getData(apt.techniques_df, techniques[j], 'description')
                techDesc = apt.fix_pdf_description(techDesc)
                pdf.multi_cell(170, 10, txt="{}".format(techDesc),align = 'L')
                mitigations = apt.mitigationsByTechnique(apt.relationships_df, techniques[j])
                if mitigations != []:
                    pdf.multi_cell(170, 10, txt="Mitigation: ", align = 'L')
                    for k in range(len(mitigations)):
                        pdf.ln(5)
                        pdf.cell(20)
                        pdf.multi_cell(160, 10, txt="{}".format(apt.getData(apt.mitigations_df, mitigations[k], 'name')),align = 'L')
                        pdf.ln(5)
                        pdf.cell(30)
                        mitDesc = apt.getData(apt.mitigations_df, mitigations[k], 'description')
                        mitDesc = apt.fix_pdf_description(mitDesc)
                        pdf.multi_cell(150, 10, txt="{}".format(mitDesc),align = 'L')
                pdf.ln(10)

    # 59% - 50% Groups
    if five != []:
        pdf.set_font("DejaVu", size = 20)
        pdf.cell(80)
        pdf.cell(30, 10, txt="59% - 50% Match", align = 'C')
        pdf.set_font("DejaVu", size = 12)
        pdf.ln(20)

        for i in range(len(five)):
            pdf.set_font("DejaVu", size = 16)
            pdf.multi_cell(190, 10, txt="{}".format(apt.getData(apt.groups_df, five[i], 'name')),align = 'L')
            pdf.set_font("DejaVu", size = 12)
            pdf.ln(5)
            aptDesc = apt.getData(apt.groups_df, five[i], 'description')
            aptDesc = apt.fix_pdf_description(aptDesc)
            pdf.multi_cell(180, 10, txt="{}".format(aptDesc),align = 'L')
            pdf.ln(10)
            pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(apt.groups_df, five[i], 'associated groups')),align = 'L')
            pdf.ln(10)
            software = apt.getSoftwareByGroup(apt.relationships_df, five[i])
            pdf.multi_cell(190, 10, txt="Software:  ", align = 'L')
            for j in range(len(software)):
                pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.software_df, software[j], 'name')), align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                softDesc = apt.getData(apt.software_df, software[j], 'description')
                softDesc = apt.fix_pdf_description(softDesc)
                pdf.multi_cell(170, 10, txt="{}".format(softDesc),align = 'L')
            techniques = apt.getTechniquesByGroup(apt.relationships_df, five[i])
            pdf.multi_cell(190, 10, txt="Techniques: ", align = 'L')
            for j in range(len(techniques)):
                pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.techniques_df, techniques[j], 'name')),align = 'L')
                pdf.ln(5)
                pdf.cell(10)
                techDesc = apt.getData(apt.techniques_df, techniques[j], 'description')
                techDesc = apt.fix_pdf_description(techDesc)
                pdf.multi_cell(170, 10, txt="{}".format(techDesc),align = 'L')
                mitigations = apt.mitigationsByTechnique(apt.relationships_df, techniques[j])
                if mitigations != []:
                    pdf.multi_cell(170, 10, txt="Mitigation: ", align = 'L')
                    for k in range(len(mitigations)):
                        pdf.ln(5)
                        pdf.cell(20)
                        pdf.multi_cell(160, 10, txt="{}".format(apt.getData(apt.mitigations_df, mitigations[k], 'name')),align = 'L')
                        pdf.ln(5)
                        pdf.cell(30)
                        mitDesc = apt.getData(apt.mitigations_df, mitigations[k], 'description')
                        mitDesc = apt.fix_pdf_description(mitDesc)
                        pdf.multi_cell(150, 10, txt="{}".format(mitDesc),align = 'L')
                pdf.ln(10)
    # save the pdf with name .pdf
    pdf.output("./PDFFiles/RAPTOR.pdf", 'F')

def grouppdfReport(groups: dict, name):
    pdf = FPDF()
    single = []
    for key in groups:
        single.append(key)

    # Add a page
    pdf.add_page()
    pdf.add_font('DejaVu', '', './PDFFiles/DejaVuSans.ttf', uni=True)  # added line
    # set style and size of header
    pdf.set_font('DejaVu','',25)
    pdf.cell(80)
    pdf.cell(30,10,'R.A.P.T.O.R.',0,0,'C')
    pdf.ln(20)

    for i in range(len(single)):
        pdf.set_font("DejaVu", size = 16)
        pdf.multi_cell(190, 10, txt="{}".format(apt.getData(apt.groups_df, single[i], 'name')),align = 'L')
        pdf.set_font("DejaVu", size = 12)
        pdf.ln(5)
        aptDesc = apt.getData(apt.groups_df, single[i], 'description')
        aptDesc = apt.fix_pdf_description(aptDesc)
        pdf.multi_cell(180, 10, txt="{}".format(aptDesc),align = 'L')
        pdf.ln(10)
        pdf.multi_cell(190, 10, txt="Associated Groups: {}".format(apt.getData(apt.groups_df, single[i], 'associated groups')),align = 'L')
        pdf.ln(10)
        software = apt.getSoftwareByGroup(apt.relationships_df, single[i])
        pdf.multi_cell(190, 10, txt="Software:  ", align = 'L')
        for j in range(len(software)):
            pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.software_df, software[j], 'name')), align = 'L')
            pdf.ln(5)
            pdf.cell(10)
            softDesc = apt.getData(apt.software_df, software[j], 'description')
            softDesc = apt.fix_pdf_description(softDesc)
            pdf.multi_cell(170, 10, txt="{}".format(softDesc),align = 'L')
        techniques = apt.getTechniquesByGroup(apt.relationships_df, single[i])
        pdf.multi_cell(190, 10, txt="Techniques: ", align = 'L')
        for j in range(len(techniques)):
            pdf.multi_cell(180, 10, txt="{}".format(apt.getData(apt.techniques_df, techniques[j], 'name')),align = 'L')
            pdf.ln(5)
            pdf.cell(10)
            techDesc = apt.getData(apt.techniques_df, techniques[j], 'description')
            techDesc = apt.fix_pdf_description(techDesc)
            pdf.multi_cell(170, 10, txt="{}".format(techDesc),align = 'L')
            mitigations = apt.mitigationsByTechnique(apt.relationships_df, techniques[j])
            if mitigations != []:
                pdf.multi_cell(170, 10, txt="Mitigation: ", align = 'L')
                for k in range(len(mitigations)):
                    pdf.ln(5)
                    pdf.cell(20)
                    pdf.multi_cell(160, 10, txt="{}".format(apt.getData(apt.mitigations_df, mitigations[k], 'name')),align = 'L')
                    pdf.ln(5)
                    pdf.cell(30)
                    mitDesc = apt.getData(apt.mitigations_df, mitigations[k], 'description')
                    mitDesc = apt.fix_pdf_description(mitDesc)
                    pdf.multi_cell(150, 10, txt="{}".format(mitDesc),align = 'L')
            pdf.ln(10)

    # save the pdf with name .pdf
    output_path='./PDFFiles/'+name+'.pdf'
    pdf.output(output_path, 'F')

if Debug:
    grouppdfReport(group1, list(group1.keys())[0])