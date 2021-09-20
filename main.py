#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 ██████╗ ██████╗  █████╗ ██╗  ████████╗███████╗███╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗██╔══██╗██║  ╚══██╔══╝██╔════╝████╗  ██║██╔════╝██╔══██╗
██║  ███╗██████╔╝███████║██║     ██║   █████╗  ██╔██╗ ██║█████╗  ██████╔╝
██║   ██║██╔═══╝ ██╔══██║██║     ██║   ██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╔╝██║     ██║  ██║███████╗██║   ███████╗██║ ╚████║███████╗██║  ██║
 ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
Proudly made by Et3rnal | GPAltener 1.0 | 2021
"""

import argparse
import os, img2pdf, string, qrcode
from random import choice
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from PIL import Image, ImageDraw, ImageFont

class GPAltener():

    def __init__(self, nv):
        self.nv = None

    def gen_date(self, timestamp=None):
        timestamp = str(timestamp).lower()  # avoiding a typo
        if timestamp != 'none':  # possible-entries: m (minutes), h (hours), d (days)
            max_len = len(timestamp) - 1
            get_num = timestamp[0:max_len]
            if str(timestamp).endswith('m'):
                date = (datetime.today() - timedelta(minutes=int(get_num))).strftime("%Y-%m-%d %H:%M")
                duration_end = (datetime.today() - timedelta(minutes=int(get_num)) + relativedelta(months=2)).strftime("%Y-%m-%d %H:%M")
            elif str(timestamp).endswith('h'):
                date = (datetime.today() - timedelta(hours=int(get_num))).strftime("%Y-%m-%d %H:%M")
                duration_end = (datetime.today() - timedelta(hours=int(get_num)) + relativedelta(months=2)).strftime("%Y-%m-%d %H:%M")
            elif str(timestamp).endswith('d'):
                date = str((datetime.today() - timedelta(days=int(get_num))).strftime("%Y-%m-%d %H:%M"))
                duration_end = (datetime.today() - timedelta(days=int(get_num)) + relativedelta(months=2)).strftime("%Y-%m-%d %H:%M")
        else:
            date = str((datetime.today()).strftime("%Y-%m-%d %H:%M"))
            duration_end = (datetime.today() + relativedelta(months=2)).strftime("%Y-%m-%d %H:%M")
        
        row = []
        for element in str(date).split('-'):
            row.append(element)
        file_name = 'galimybiu_pasas_' + row[0] + '_' + row[1] + '_' + row[2][:2]
        return date, duration_end, file_name

    def gen_fake_hash(self):
        count = 284
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '@$%&'
        qr_hash = "".join(str(choice(chars)) for i in range(count))
        return qr_hash

    def bypass(self, full_name: str, birth_year: int, timestamp=None):
        if timestamp != None:
            date, duration_end, file_name = self.gen_date(timestamp)
        else:
            date, duration_end, file_name = self.gen_date(None)
        
        qr_code = qrcode.make(self.gen_fake_hash())
        qr_code.save('qr.png')

        sample_loader = Image.open(os.getcwd() + '/sample.jpg')
        qr_img = Image.open('qr.png').resize((360, 360))

        drawing_tool = ImageDraw.Draw(sample_loader)
        font_tool = ImageFont.truetype('Roboto-Regular.ttf', 27)
        drawing_tool.text((620.5, 272.5), str(full_name.upper()),(0, 0, 0), font=font_tool)
        drawing_tool.text((620.5, 356), str(birth_year),(0, 0, 0), font=font_tool)
        drawing_tool.text((620.5, 440), str(date),(0, 0, 0), font=font_tool)
        drawing_tool.text((620.5, 524.5), str(duration_end),(0, 0, 0), font=font_tool)
        sample_loader.paste(qr_img, (130, 220))
        sample_loader.save(file_name + '.jpg')
        with open(file_name + '.pdf', 'wb') as wd:
            wd.write(img2pdf.convert(file_name + '.jpg'))

        # cleanup
        os.remove(os.getcwd() + '/qr.png')
        os.remove(os.getcwd() + '/' + str(file_name) + '.jpg')
        return print('Jūsų galimybių pasas buvo išsaugotas: ' + str(os.getcwd()) + '/' + file_name + '.pdf')

def main(full_name: str, birth_year: int, timestamp=None):
    gp = GPAltener(None)
    gp.bypass(full_name=full_name, birth_year=birth_year, timestamp=timestamp)
    return

data_parser = argparse.ArgumentParser(description="BypassGP 1.0")
data_parser.add_argument('-v', '--pv', required=True, help='Jūsų pilnas vardas', type=str)
data_parser.add_argument('-g', '--gm', required=True, help='Jūsų gimimo metai', type=int)
data_parser.add_argument('-d', '--delay', required=False, help='Išdavimo datos parametras (neprivalomas)', type=str)
arguments = vars(data_parser.parse_args())

if len(arguments['pv']) > 5:
    if len(str(arguments['gm'])) > 3 and len(str(arguments['gm'])) < 5:
        if len(str(arguments['delay'])) > 1 and str(arguments['delay']) != 'None':
            if str(arguments['delay']).endswith('m') or str(arguments['delay']).endswith('h') or str(arguments['delay']).endswith('d'):
                main(arguments['pv'], arguments['gm'], arguments['delay'])
            else:
                print('Neteisingi laukelio \'delay\' duomenys. Praleidžiama..')
                main(arguments['pv'], arguments['gm'])
        else:
            main(arguments['pv'], arguments['gm'])
    else:
        print('Neteisingi laukelio \'gimimo metai (gm)\' duomenys!')
        quit()
else:
    print('Neteisingi laukelio \'pilnas vardas (pv)\' duomenys!')
    quit()