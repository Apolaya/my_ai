import pandas as pd
import os


# This class uses panda to creata  dataframe from the excel file found on the telemtry website.
# the goal is to extract what data we need so we can make it a string file for the LLM
# We are gonna need two files eventually so we can ask the LLM to compare and contrast 
class telemetry_reader:
    def __init__(self, file_name: str) -> None:
        self.file = os.path.join(file_name)
    
    def extract(self):
        try:
            panda_file = pd.read_excel(self.file, sheet_name=3)
            sector_1 = panda_file.columns.get_loc('Sector 1')
            panda_file_all_sectors = panda_file.iloc[:,sector_1:]
            return panda_file_all_sectors.to_string(header=True)
        except FileExistsError:
            return "File not found - apolaya"
        

    def find_lap_times(self):
        lap_time_column = "Lap time"
        try:
            panda_file = pd.read_excel(
                io=self.file,
                sheet_name=3,
            )
            if lap_time_column in panda_file.columns:
                lap_times_string = panda_file[lap_time_column].to_string(index=False)
                return lap_times_string
            else:
                return "COLUMN NOT FOUND"
        except FileNotFoundError:
            return "FILE NOT FOUND"

    def find_sector_times(self):
        start_column = "Sector 1"  # The column from which to start
        try:
            # Read the Excel file (sheet index 3 means the 4th sheet)
            panda_file = pd.read_excel(io=self.file, sheet_name=3)

            # Check if the start column exists
            if start_column in panda_file.columns:
                sector_times_string = panda_file[start_column].to_string(index=False)
                return sector_times_string
            else: 
                return "Column not found"
        except FileNotFoundError:
            return FileNotFoundError
                

    def print_lap_times(self):
        # Read the Excel file and print its content
        excel_data = self.find_lap_times()
        print(excel_data)

    def print_sector_times(self):
        excel_data = self.find_sector_times()
        print(excel_data)
