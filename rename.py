import os
import glob
import fitz
from datetime import datetime
import re


class Rename:
    def rename(self):
        cwd = os.getcwd()
        src = cwd + '\\bills\\'
        des = 'C:\Users\DA063101\Documents\\YESTERDAY\\'
        amount = 0
        for pdf_file in glob.glob(src + "\\*.pdf"):
            file_name = list()
            file_name = (pdf_file.split('_'))
            # print file_name
            box_type = file_name[1]
            mode = file_name[3]
            file_no = file_name[5].split('.')[0]
            # print file_no
            date = (datetime.now()).strftime("%m%d%Y")
            doc1 = fitz.open(pdf_file)
            page = doc1.loadPage(0)
            text = page.getText()
            # print text
            # amount_str = re.search(r'Batch Total: ^\$?(([1-9]\d{0,2}(,\d{3})*)|0)?\.\d{1,2}', text).group()
            batch_amount = re.findall(r'Batch Total: \S*', text)
            # print batch_amount
            label, amount_dollar = batch_amount[0].split(':')
            amount_comma = amount_dollar.split('$')[1]
            temp_amount_list = amount_comma.split(',')
            temp_amount = ''
            temp_file_no = int(file_no) - 1
            for digit in temp_amount_list:
                temp_amount = temp_amount + digit
            name = ''
            if 826504 == int(box_type):
                location = 'P'
            elif 826791 == int(box_type):
                location = 'N'
            else:
                location = 'S'
            if 800 == int(mode):
                if file_no == '1':
                    name = 'BHMG CC ' + date + '(CREDIT CARDS)'
                else:
                    name = 'BHMG CC ' + date + '(CREDIT CARDS)'+'^'+str(temp_file_no)
            elif 99999 == int(mode):
                if temp_file_no == 0:
                    name = 'BHMG^MC^KC^'+'999^'+date+'^'+location
                else:
                    name = 'BHMG^MC^KC^'+'999^'+date+'^'+location+'^'+str(temp_file_no)
            elif 700 == int(mode):
                if temp_file_no == 0:
                    name = 'BHMG^MC^KC^' + '700^' + date + '^' + location
                else:
                    name = 'BHMG^MC^KC^' + '700^' + date + '^' + location + '^' + str(temp_file_no)
            elif 900 == int(mode):
                if temp_file_no == 0:
                    name = 'BHMG^MC^KC^' + '900^' + date + '^' + location
                else:
                    name = 'BHMG^MC^KC^' + '900^' + date + '^' + location + '^' + str(temp_file_no)
            else:
                """if file_no == '1':
                    amount = float(temp_amount)
                    name = 'BHMG^RB^KC^' + date + '^' + str(amount) + '^' + mode.zfill(3) + '^' + location
                else:"""
                amount = float(temp_amount) - float(amount)
                name = 'BHMG^RB^KC^' + date + '^' + str(amount) + '^' + mode.zfill(3) + '^' + location
                if os.path.exists(des+name+'.pdf'):
                    name = name + str(file_no)
            name = des + name+'.pdf'
            #name = pdf_file.split('\\')[6]
            print pdf_file
            print name
            doc1.save(name, garbage=4, clean=1)
            # os.rename(pdf_file, name)


r = Rename()
r.rename()
