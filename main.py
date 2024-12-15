import csv



def write_to_file(filename, data_chunk, data_header = None):
    with open(filename, 'w') as new_file:  # creating new file.
        writer = csv.writer(new_file)
        if data_header:
            writer.writerow(data_header)  # headers will add on each new file.
        writer.writerows(data_chunk)  # chunk data will be stored in new file.

def split_csv(filename, row_count = 400):
    chunk = []
    row_number = 0
    file_number = 1
    header = ''
    original_file_name, extension = filename.split('.')

    with open(filename, 'r') as file: # open salaries.csv file in reading mode.
        reader = csv.reader(file) # csv.reader will read file and assign it to reader.
        for row in reader: # the loop will run on each row.
            if header == '': # if it's null then it will assign the headers on first call.
                header = row # header names are stored in array format -> ['years', 'salary']
                continue

            chunk.append(row) # rows will add on chunk array one by one.
            row_number += 1
            if row_number >= row_count: # when the loop run 400 times, this condition will true.
                write_to_file(f'chunk-{original_file_name}-{file_number}.{extension}', chunk, header)
                chunk = [] # chunk will reset.
                file_number += 1
                row_number = 0

        # now suppose we have 3,000 rows in salaries.csv, and we are storing 400 records in each csv file,
        # so in that case it will only generate 7 files with 400 records, and what about remaining 200 records?
        # so in last case whenever we get records less than 400 it will also remain in chunk[] so below function
        # will work.
        if chunk:
            write_to_file(f'chunk-{original_file_name}-{file_number}.{extension}', chunk, header)

split_csv('salaries.csv')