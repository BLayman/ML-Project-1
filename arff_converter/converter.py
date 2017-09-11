#!/usr/bin/env python3

# class for converting .csv attribute and data files to a .arff file
class Converter():

    # assign data and attribute files to class fields,
    # initialize data and att lists for storing lines of data and attributes
    def __init__(self, data, attributes):
        self.data_file = data
        self.attribute_file = attributes
        self.data = []
        self.att = []

    # entry point for conversion process
    def convert(self):
        self.arff_relation()
        self.process_attributes()
        self.process_data()

    # open input attribute file and append parsed lines to att
    def process_attributes(self):
        with open(self.attribute_file) as f:
            for line in f:
                line = line.split(',')
                self.att.append(line)
        self.trim_attributes()
        self.arff_attributes()

    # open input data file and append parsed data to self.data
    def process_data(self):
        with open(self.data_file) as f:
            f = unicode(f, errors='ignore')
            for line in f:
                line = line.split(',')
                if not len(line) > 1:
                    line = ''.join(line)
                    line = line.split(' ')
                self.data.append(line)
        self.arff_data()

    # add relation line to arff output file
    def arff_relation(self):
        arff = open('data.arff', 'w')
        arff.write('@relation goes_here\n\n')
        arff.close()

    # write attribute portion of arff output file, using self.att list
    def arff_attributes(self):
        arff = open('data.arff', 'a')
        for r in range(len(self.att)):
            # handle different kinds of attributes
            if self.att[r][1] == 'string' or self.att[r][1] == 'numeric':
                arff.write("@attribute %s %s\n" % (self.att[r][0], self.att[r][1]))
            else:
                if self.att[r][1][:1] == '{': # This is a nominal-specification
                    arff.write("@attribute %s %s\n" % (self.att[r][0], self.att[r][1].replace('&', ',')))
                else: # This is a date
                    arff.write("@attribute %s %s\n" % (self.att[r][0], self.att[r][1]))
        arff.write("\n")
        arff.close()

    # write data portion of arff output file using self.data list
    def arff_data(self):
        arff = open('data.arff', 'a')
        arff.write("@data\n")
        for r in range(len(self.data)):
            # write data to arff file
            arff.write(','.join(self.data[r]))
        arff.close()

    # remove special characters and replace blanks with underscores for strings in att sub lists
    def trim_attributes(self):
        # for every line r in att
        for r in range(len(self.att)):
            # and for every string c in r
            for c in range(len(self.att[r])):
                s = list(self.att[r][c])
                s = [x for x in s if x != '\"']
                s = [x for x in s if x != '\n']
                self.att[r][c] = ''.join(s)
            self.att[r][0] = self.att[r][0].replace(" ", "_")

# create instance of Converter class and run convert() method
if __name__ == "__main__":
    converter = Converter('online_retail_data.csv', 'online_retail_att.csv')
    converter.convert()
