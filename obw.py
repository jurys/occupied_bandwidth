import FSU as instrument
import matplotlib.pyplot as plt
import time
import numpy as np
import math
from numpy import NaN, Inf, arange, isscalar, asarray, array
import sys
import operator
#import docx as doc
import os

def dbm_to_mw(dBm):
    """This function converts a power given in dBm to a power given in mW."""
    return 10**((dBm)/10.)

def projekt_dir():
    print('Geben Sie Projekt Namen ein: ')
    prj_name = str(input())
    try:
        os.mkdir('report\\' + prj_name)
    except:
        print('Projekt schon vorhanden')
    return prj_name

def set_OCW(f_low, f_high, fc):
    print('Geben Sie OCW ein : ')
    OCW = float(input())
    if((float(fc)+0.5*OCW)<float(f_high) and (float(fc)-0.5*OCW)>float(f_low)):
        print('OCW out of range')
    return OCW

def set_frequency_band():
    print('Geben Sie Operating Frequency Band ein: ')
    band = input()
    if band == ('a' or 'A'):
        f_low_OFB = 26957000
        f_high_OFB = 27283000
        band ='A'
    elif band == ('c' or 'C'):
        f_low_OFB = 40660000
        f_high_OFB = 40700000
        band ='C'
    elif band == ('d' or 'D'):
        f_low_OFB = 169400000
        f_high_OFB = 169475000
        band ='D'
    elif band == ('e' or 'E'):
        f_low_OFB = 169400000
        f_high_OFB = 169487500
        band ='E'
    elif band == ('f' or 'F'):
        f_low_OFB = 169487500
        f_high_OFB = 169587500
        band ='F'
    elif band == ('g' or 'G'):
        f_low_OFB = 169587500
        f_high_OFB = 169812500
        band ='G'
    elif band == ('h' or 'H'):
        f_low_OFB = 433050000
        f_high_OFB = 434790000
        band ='H'
    elif band == ('i' or 'I'):
        f_low_OFB = 433050000
        f_high_OFB = 434790000
        band ='I'
    elif band == ('j' or 'J'):
        f_low_OFB = 433040000
        f_high_OFB = 434790000
        band ='J'
    elif band == ('k' or 'K'):
        f_low_OFB = 863000000
        f_high_OFB = 865000000
        band ='K'
    elif band == ('l' or 'L'):
        f_low_OFB = 865000000
        f_high_OFB = 868000000
        band ='L'
    elif band == ('m' or 'M'):
        f_low_OFB = 868000000
        f_high_OFB = 868600000
        band ='M'
    elif band == ('n' or 'N'):
        f_low_OFB = 868700000
        f_high_OFB = 869200000
        band ='N'
    elif band == ('o' or 'O'):
        f_low_OFB = 869400000
        f_high_OFB = 869650000
        band ='O'
    elif band == ('p' or 'P'):
        f_low_OFB = 869400000
        f_high_OFB = 869650000
        band ='P'
    elif band == ('q' or 'Q'):
        f_low_OFB = 869700000
        f_high_OFB = 870000000
        band ='Q'
    elif band == ('r' or 'R'):
        f_low_OFB = 869700000
        f_high_OFB = 870000000
        band ='R'
    elif band == ('s' or 'S'):
        f_low_OFB = 34995000
        f_high_OFB = 35225000
        band ='S'
    elif band == ('t' or 'T'):
        f_low_OFB = 40665000
        f_high_OFB = 40695000
        band ='T'
    elif band == ('u' or 'U'):
        f_low_OFB = 138200000
        f_high_OFB = 138450000
        band ='U'
    elif band == ('v' or 'V'):
        f_low_OFB = 169475000
        f_high_OFB = 169487500
        band ='V'
    elif band == ('w' or 'W'):
        f_low_OFB = 169587500
        f_high_OFB = 169600000
        band ='W'
    elif band == ('x' or 'X'):
        f_low_OFB = 863000000
        f_high_OFB = 870000000
        band ='X'
    elif band == ('y' or 'y'):
        f_low_OFB = 870000000
        f_high_OFB = 875800000
        band ='Y'
    elif band == ('z' or 'Z'):
        f_low_OFB = 875800000
        f_high_OFB = 876000000
        band ='Z'
    elif band == ('aa' or 'AA'):
        f_low_OFB = 870000000
        f_high_OFB = 875800000
        band ='AA'
    elif band == ('ab' or 'AB'):
        f_low_OFB = 915000000
        f_high_OFB = 915200000
        band ='AB'
    elif band == ('ac' or 'AC'):
        f_low_OFB = 920800000
        f_high_OFB = 921000000
        band ='AC'
    elif band == ('ad' or 'AD'):
        f_low_OFB = 915200000
        f_high_OFB = 920800000
        band ='AD'
    return f_low_OFB, f_high_OFB, band

def set_fc(f1, f2):
    global fc
    print('Geben Sie Center Frequency[Hz] für den Operating Channel ein: ')
    fc = int(input())
    r = range(f1, f2)
    if ((fc in r)):# and (fc_high < (f_low_OFB+0.5*(f2-f1))):
        return fc
    else:
       print('flow_OFB out range')
       return 1

def split_to_float(text, divider=1):

    numbers = []
    # split the text
    words = text.split(',')
    # text to double

    for word in words:
            numbers.append(float(word)/divider)
    return numbers

def plot_hor_line(f, value_min, value_max, line_style="--"):
    limitF = [f, f]

    limitValue = [round_to_min(value_min), round_to_max(value_max)]
    plt.plot(limitF, limitValue, color="red", linewidth=0.7, linestyle=line_style, label="Limit")

def round_to_max(value):
    value1 = value +9
    if value1<(10):
        value1 = 10
    return int(value1)

def round_to_min(value):
    value1 = value -9
    return int(value1)

def f_name():
    print('Geben Sie Eindeutige frequenz namen:')
    f_name = str(input())
    return f_name

def generate_latex_pdf(row0,row1,row2,row3,row4,row5,Xtrace0, Xtrace1, Xtrace2, Xtrace3, Xtrace4, Xtrace5,
                    peak0,peak1,peak2,peak3,peak4,peak5,):
    geometry_options = {
        "head": "40pt",
        "margin": "0.5in",
        "bottom": "0.6in",
        "includeheadfoot": True
    }


    doc = Document(geometry_options=geometry_options)

    # Generating first page style
    first_page = PageStyle("firstpage")
    # Header image
    with first_page.create(Head("L")) as header_left:
        with header_left.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                         pos='c')) as logo_wrapper:
            logo_file = os.path.join(#os.path.dirname(__file__) +
                                     'CetecomLogo.png')
            logo_wrapper.append(StandAloneGraphic(image_options="width=120px",
                                                  filename=logo_file))
    # Add document title
    with first_page.create(Head("R")) as right_header:
        with right_header.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                          pos='c', align='r')) as title_wrapper:
            title_wrapper.append(LargeText(bold("ETSI EN 300 220")))
            title_wrapper.append(LineBreak())
            title_wrapper.append(MediumText(bold(NoEscape(r'\today'))))
            title_wrapper.append(LineBreak())
            #title_wrapper.append(MediumText(bold(NoEscape(r'\time'))))
    # Add footer adress
    with first_page.create(Foot("L")) as footer_left:

        with footer_left.create(Tabularx(
                "X",
                width_argument=NoEscape(r"\textwidth"))) as footer_table:
            footer_table.add_hline(color="blue")
            footer_table.add_row(MediumText(bold("CETECOM Essen")))
            footer_table.add_row(MediumText(bold("Im Teelbruch 116")))
            footer_table.add_row(MediumText(bold("45219 Essen - Germany")))
    # Add footer page
    with first_page.create(Foot("R")):
        first_page.append(simple_page_number())

    with doc.create(Section('Settings')):
        doc.append(FSW.query('*IDN?'))
        with doc.create(LongTabu("X[l] X[l] X[l] X[l]",
                                 row_height=1.5)) as settings_table:
            settings_table.add_row(["Center frequency",
                                    "Span",
                                    "RBW",
                                    "Detector",
                                    ],
                                   mapper=bold,
                                   color="lightgray")
            settings_table.add_empty_row()
            settings_table.add_row(row0, color="lightgray")


    with doc.create(Section('Plot Out Of Band Emissions for Operating Channel')):
        with doc.create(Figure(position='h!')) as spectrum:
            spectrum.add_image('foo1.png')

    doc.preamble.append(first_page)

    doc.change_document_style("firstpage")


    # Add statement table
    if((len(peak0)+len(peak1)+len(peak2)+len(peak3)+len(peak4)+len(peak5))>0):
        doc.append(NewPage())
        with doc.create(LongTabu("X[l] X[l] X[l] X[r]",
                                 row_height=1.5)) as data_table:
            data_table.add_row(["Frequency(MHz)",
                                "Mergin(dB)",
                                "RMS(dBm)",
                                "Limit(dBm)",
                                ],
                               mapper=bold,
                               color="lightgray")
            data_table.add_empty_row()
            data_table.add_hline()

            k=0
            k = row_for_peak_table(Xtrace0, peak0, k, data_table)
            k = row_for_peak_table(Xtrace1, peak1, k, data_table)
            k = row_for_peak_table(Xtrace2, peak2, k, data_table)
            k = row_for_peak_table(Xtrace3, peak3, k, data_table)
            k = row_for_peak_table(Xtrace4, peak4, k, data_table)
            k = row_for_peak_table(Xtrace5, peak5, k, data_table)
    doc.generate_pdf("report/report", clean_tex=False)

def main():
    inst = instrument.FSU('GPIB0::1::INSTR')

    inst.open_over_gpib()

    #prj_name = projekt_dir()

    name = f_name()

    f_low_OFB, f_high_OFB, band = set_frequency_band()

    fc = set_fc(f_low_OFB, f_high_OFB)

    OCW = set_OCW(f_low_OFB, f_high_OFB, fc)


    rbw_pattern = [100, 200, 300, 500, 1000, 2000, 3000, 5000, 10000, 30000, 50000, 100000]
    i = 0
    for value in rbw_pattern:
        if (OCW*0.01) <= value:
            break
        i = i + 1
    RBW = rbw_pattern[i]

    inst.preset()

    inst.set_continuous_mode_on_off(0)

    inst.set_center(fc)

    inst.set_span(2*OCW)

    inst.set_RBW_xVBW(RBW, x=3)

    inst.send_SCPI('DISP:TRAC:Y:RLEV 15')

    inst.send_SCPI('DISP:TRAC:Y:RLEV:OFFS 0.3')  # anpassen an Kabel

    inst.set_detector('RMS')

    inst.send_SCPI('CALC:MARK:FUNC:POW:OBW')

    inst.start()

    time.sleep(2)
    inst.start()

    time.sleep(2)
    inst.start()

    time.sleep(2)

    print('-----')
    print(inst.query('CALC:MARK:FUNC:POW:RES? OBW'))
    print('-----')
    inst.send_SCPI('MMEM:STOR:MARK E:\\' + name+'"marker.txt"')

    x_trace, y_trace = inst.get_trace_data(1)

    x_trace = split_to_float(x_trace, 1000000)

    y_trace = split_to_float(y_trace)

    p = 0
    p_ges = 0
    for row in y_trace:
        p_mw = dbm_to_mw(float(row))

        p_ges = p_ges + p_mw

    #print(p_ges)
    i = 0
    for row in y_trace:
        i=i+1
        p_mw = dbm_to_mw(float(row))
        p = p + p_mw

        if p >= (p_ges * 0.005):
            break
    a=x_trace[i-1]
    print(a)
    i = 0
    for row in y_trace:
        i=i+1
        p_mw = dbm_to_mw(float(row))
        p = p + p_mw

        if p >= (p_ges * 0.995):
            break

    b = x_trace[i+1]
    print(b)
    print((b-a)*1000000)

main()