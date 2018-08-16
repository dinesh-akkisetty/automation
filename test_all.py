import unittest
import pandas as pd
import fitz
from readexcel import ReadExcel
from BHMG.rename import Rename


class TestExcelMethods(unittest.TestCase):
    def setUp(self):
        self.obj_excel = ReadExcel()
        self.obj_rename = Rename()

    def test_ExtractValues_EmptyDataFrame(self):
        empty_df = pd.DataFrame()
        self.assertEqual('Empty Frame', ReadExcel.extract_values(empty_df))

    def test_ExtractValues_NonEmptyDataFrame(self):
        data = {'website': ['Facebook', 'Gmail'], 'userid': ['dinesh10933@gmail.com', 'dinesh10933@gmail.com'], 'password': ['7k62rPHwUOvEVSmoHDMRmHO07DmGDdX7nTj7Ni6rTg=', 'b4yXyhEnRcfd43Kn1TTMoAv2reEhds8orBI/veyHrg=']}
        non_empty_df = pd.DataFrame(data)
        list_excepted = [[u'7k62rPHwUOvEVSmoHDMRmHO07DmGDdX7nTj7Ni6rTg=', u'dinesh10933@gmail.com', u'Facebook'], [u'b4yXyhEnRcfd43Kn1TTMoAv2reEhds8orBI/veyHrg=', u'dinesh10933@gmail.com', u'Gmail']]
        self.assertEqual(list_excepted, ReadExcel.extract_values(non_empty_df))

    def test_GetFiles_InvalidDirectory(self):
        src ='D:/Users/DA063101/'
        status = Rename.get_files(src)
        self.assertEqual(-2, status)

    def test_GetFiles_EmptyDirectory(self):
        src = 'C:\Users\DA063101\Documents\empty'
        status = Rename.get_files(src)
        self.assertEqual(-1, status)

    def test_GetFiles_ValidDirectory_OnlyPdf(self):
        src = "C:\Users\DA063101\Documents\\08122018"
        expected_files = ['C:\Users\DA063101\Documents\\08122018\BHMG^MC^KC^700^08092018^S.pdf']
        self.assertEqual(expected_files, Rename.get_files(src))

    def test_GetFiles_ValidDirectory_AllFiles(self):
        src = "C:\Users\DA063101\Documents\\08122018"
        expected_files = ['C:\Users\DA063101\Documents\\08122018\BHMG^MC^KC^700^08092018^S.pdf']
        self.assertEqual(expected_files, Rename.get_files(src))

    def test_CheckFile_InvalidFile(self):
        file_name = 'testfile.pdf'
        self.assertEqual('Invalid File', Rename.check_and_split_file_name(file_name))

    def test_CheckFile_ValidFile(self):
        file_name = 'bt_826504_0810_1_doc_1.pdf'
        expected = ['bt', '826504', '0810', '1', 'doc', '1.pdf']
        self.assertEqual(expected, Rename.check_and_split_file_name(file_name))

    def test_GetBatchAmount_Valid(self):
        text = 'Batch Total: $1,123.4'
        amount = '1123.4'
        self.assertEqual(amount, Rename.get_batch_amount(text))

    def test_GetBatchAmount_Invalid(self):
        text = 'Batch Total:'
        self.assertEqual(-1, Rename.get_batch_amount(text))

    def test_GetBatchAmount_Invalid_1(self):
        text = 'Batch Total: $'
        self.assertEqual(-2, Rename.get_batch_amount(text))

    def test_NewFileName_ValidReceiptBatch_1(self):
        file_name = ['bt', '826504', '0810', '1', 'doc', '1.pdf']
        temp_amount = 1123.4
        # date = (datetime.now()).strftime("%m%d%Y")
        name = 'BHMG^RB^KC^08152018^1123.40^001^P'
        self.assertEqual(name, Rename.new_file_name(file_name, temp_amount))

    def test_NewFileName_ValidReceiptBatch_2(self):
        file_name = ['bt', '826504', '0810', '1', 'doc', '2.pdf']
        previous_batch_amount = 123.4
        temp_amount = 1123.4
        name = 'BHMG^RB^KC^08152018^1000.00^001^P'
        self.assertEqual(name, Rename.new_file_name(file_name, temp_amount, previous_batch_amount))

    def test_NewFileName_ValidReceiptBatch_3(self):
        file_name = ['bt', '826791', '0810', '700', 'doc', '2.pdf']
        temp_amount = 1123.4
        name = 'BHMG^MC^KC^700^08152018^N^1'
        self.assertEqual(name, Rename.new_file_name(file_name, temp_amount))

    def test_NewFileName_ValidReceiptBatch_4(self):
        file_name = ['bt', '826791', '0810', '700', 'doc', '1.pdf']
        temp_amount = 1123.4
        name = 'BHMG^MC^KC^700^08152018^N'
        self.assertEqual(name, Rename.new_file_name(file_name, temp_amount))

    def test_NewFileName_ValidReceiptBatch_5(self):
        file_name = ['bt', '826796', '0810', '800', 'doc', '2.pdf']
        temp_amount = 1123.4
        name = 'BHMG CC 08152018(CREDIT CARDS)^1'
        self.assertEqual(name, Rename.new_file_name(file_name, temp_amount))

    def test_NewFileName_ValidReceiptBatch_6(self):
        file_name = ['bt', '826796', '0810', '800', 'doc', '1.pdf']
        temp_amount = 1123.4
        name = 'BHMG CC 08152018(CREDIT CARDS)'
        self.assertEqual(name, Rename.new_file_name(file_name, temp_amount))

    def test_NewFileName_ValidReceiptBatch_7(self):
        file_name = ['bt', '826796', '0810', '99999', 'doc', '2.pdf']
        temp_amount = 1123.4
        name = 'BHMG^MC^KC^999^08152018^S^1'
        self.assertEqual(name, Rename.new_file_name(file_name, temp_amount))

    def test_NewFileName_ValidReceiptBatch_8(self):
        file_name = ['bt', '826791', '0810', '99999', 'doc', '1.pdf']
        temp_amount = 1123.4
        name = 'BHMG^MC^KC^999^08152018^N'
        self.assertEqual(name, Rename.new_file_name(file_name, temp_amount))

    def test_NewFileName_ValidReceiptBatch_9(self):
        file_name = ['bt', '826796', '0810', '900', 'doc', '2.pdf']
        temp_amount = 1123.4
        name = 'BHMG^MC^KC^900^08152018^S^1'
        self.assertEqual(name, Rename.new_file_name(file_name, temp_amount))

    def test_NewFileName_ValidReceiptBatch_10(self):
        file_name = ['bt', '826791', '0810', '900', 'doc', '1.pdf']
        temp_amount = 1123.4
        name = 'BHMG^MC^KC^900^08152018^N'
        self.assertEqual(name, Rename.new_file_name(file_name, temp_amount))

    def test_MoveFiles_1(self):
        des = 'C:\Users\DA063101\Documents\\08122018'
        name = 'BHMG^MC^KC^900^08152018^N'
        doc1 = fitz.open('C:\Users\DA063101\Documents\\08122018\BHMG^MC^KC^700^08092018^S.pdf')
        self.assertEqual(1, Rename.move_files(des, name, doc1))

    def test_rename_eob_1(self):
        src = 'C:\Users\DA063101\Documents\empty'
        self.assertEqual(-1, Rename.rename_eob(self.obj_rename, src))

    def test_rename_eob_2(self):
        src = 'D:/Users/DA063101/'
        self.assertEqual(-2, Rename.rename_eob(self.obj_rename, src))

    def test_rename_eob_3(self):
        src = 'C:/Users/DA063101/PycharmProjects/WebAutomation/bills'
        print 'done'
        self.assertEqual(1, Rename.rename_eob(self.obj_rename, src))

    """@mock.patch('__main__.visit', return_value = 2)
    def test_visit(self, mock_r):
        list_excepted = [[u'7k62rPHwUOvEVSmoHDMRmHO07DmGDdX7nTj7Ni6rTg=', u'dinesh10933@gmail.com', u'Facebook'],[u'b4yXyhEnRcfd43Kn1TTMoAv2reEhds8orBI/veyHrg=', u'dinesh10933@gmail.com', u'Gmail']]
        assert visit(list_excepted, 'Gmail') == 0
    """


if __name__ == '__main__':
    unittest.main()
