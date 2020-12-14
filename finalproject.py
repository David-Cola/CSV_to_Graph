from FunctionLibrary import CSV_Read, CSV_Plot, Trend

class Analyzer(object):
    def __init__(self, config):
        self.config = config        
        # Load Config file 
        csv = CSV_Read(config)
        self.number_of_datasets = csv[0]
        self.datasets = csv[2]
        
        self.filepath_index = csv[1].index("filepath")
        self.year_index = csv[1].index("year_col_name")
        self.value_index = csv[1].index("value_col_name")
        self.unit_codes_index = csv[1].index("unit_code_col_name")
        
        self.unit_codes = csv[1].index("unit_codes")
        
        
    def plot(self, dataset_index):
        headers = ["Year", "Total"]
        data = self.sum(dataset_index)
        CSV_Plot(data, headers, 0, 1)
    
    def trend(self, dataset_index):
        data = self.sum(dataset_index)
        return Trend(data, 0, 1)
    
    def sum(self, dataset_index):        
      	# Get information about a specific dataset (row) in our config file
        file_path = self.datasets[self.filepath_index][dataset_index]
        year_col = self.datasets[self.year_index][dataset_index]
        value_col = self.datasets[self.value_index][dataset_index]
        unit_col = self.datasets[self.unit_codes_index][dataset_index]
        unit_codes = self.datasets[self.unit_codes][dataset_index].split(",")
        
        # After we have all the information from the config file,
        # read the data from the file provided by the config
        csv = CSV_Read(file_path)
        number_of_lines = csv[0]
        header = csv[1]
        csv_data = csv[2]
        
        # Get the index of each relevant column
        data_year_index = header.index(year_col)
        data_value_index = header.index(value_col)
        data_unit_index = header.index(unit_col)
        
        data = [[], []] #[['1960', '1970'...], [0,1000,...]]
        for row in range(0, number_of_lines):
            if csv_data[data_unit_index][row] not in unit_codes:
                continue

            #valid row at this point
            #first check if year in our dataset (p)
            #if not, create and give it value 0
            year = str(csv_data[data_year_index][row])
            if year not in data[0]:
                data[0] += [year]
                data[1] += [0]

            #Have a valid dataset at this point which cointains current year and value
            #Now get index for current row's year so we can add row values
            value = csv_data[data_value_index][row]
            print (value)
            value = int(float(value)) if value != "NA" else 0
            year_index = data[0].index(year)
            data[1][year_index] += value

        return data


