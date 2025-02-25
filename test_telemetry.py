import unittest
import telemetry_reader

class Test_telemetry_reader(unittest.TestCase):

    def setUp(self): # -> DataFrame from pandas
        tr = telemetry_reader.telemetry_reader(
            "/Users/apolaya/Documents/my_ai/telemetry_data/Garage 61 - GR Buttkicker Cup - Fixed - Race - Export - 2024-09-13-18-29-30.xlsx"
        )
        return tr
    
    def test_extract(self):
        print("tesst extract\n----------------\n")
        tr = self.setUp() 
        print(tr.extract())


    
        
        
if __name__ == '__main__':
    unittest.main()
