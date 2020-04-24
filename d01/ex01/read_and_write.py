def transform_file(filename='ds.csv'):
    # Transforms .csv file to .tsv
    f = open(filename, 'r')
    content = ""
    for line in f:
        for symb in line:
            content += symb if symb != ',' else '\t'
    f.close()
    new_filename = "ds.tsv"
    f = open(new_filename, 'w')
    f.write(content)
    f.close()

if __name__ == "__main__":
    transform_file()