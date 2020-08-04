import unittest
# from fileread import create_cast_list
import fileread as f


class TestCast(unittest.TestCase):

    def test_castlist(self):
        cast_list = f.create_cast_list('./list_cast.txt')
        self.assertEqual(len(cast_list) > 3, True)

    def test_read_file(self):
        test_data = 'hello world !'
        file_data = f.read_file('./data.txt')
        self.assertNotEqual(file_data, test_data)

    def test_read_file_with(self):
        file_data = f.read_file_with('./data-w.txt')
        print('Length rad ---> ', len(file_data))
        self.assertTrue(len(file_data) > 5)

   # append function always executes before read function
    def test_append_file(self):
        file_data_len_bf = len(f.read_file_with('./data-w.txt'))
        print('Length BF ---> ', file_data_len_bf)
        f.append_file('./data-w.txt')
        file_data_len_af = len(f.read_file_with('./data-w.txt'))
        print('Length AF ---> ', file_data_len_af)
        self.assertEqual(file_data_len_af, file_data_len_bf + 1)

if __name__ == '__main__':
    unittest.main()
