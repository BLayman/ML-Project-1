#!/usr/bin/env python3


class Converter():

    def __init__(self, data, attributes):
        self.data_file = data
        self.attribute_file = attributes
        self.data = []
        self.att = []

    def convert(self):
        self.arff_relation()
        self.process_attributes()
        self.process_data()

    def process_attributes(self):
        with open(self.attribute_file) as f:
            for line in f:
                line = line.split(',')
                self.att.append(line)
        self.trim_attributes()
        self.arff_attributes()

    def process_data(self):
        with open(self.data_file) as f:
            for line in f:
                line = line.split(',')
                if not len(line) > 1:
                    line = ''.join(line)
                    line = line.split(' ')
                self.data.append(line)
        self.arff_data()

    def arff_relation(self):
        arff = open('data.arff', 'w')
        arff.write('@relation goes_here\n\n')
        arff.close()

    def arff_attributes(self):
        arff = open('data.arff', 'a')
        for r in range(len(self.att)):
            if self.att[r][1] == 'string' or self.att[r][1] == 'numeric':
                arff.write("@attribute %s %s\n" % (self.att[r][0], self.att[r][1]))
            else:
                if self.att[r][1][:1] == '{': # This is a nominal-specification
                    arff.write("@attribute %s %s\n" % (self.att[r][0], self.att[r][1].replace('&', ',')))
                else: # This is a date
                    arff.write("@attribute %s %s\n" % (self.att[r][0], self.att[r][1]))
        arff.write("\n")
        arff.close()


    def arff_data(self):
        arff = open('data.arff', 'a')
        arff.write("@data\n")
        for r in range(len(self.data)):
            arff.write(','.join(self.data[r]))
        arff.close()


    def trim_attributes(self):
        for r in range(len(self.att)):
            for c in range(len(self.att[r])):
                s = list(self.att[r][c])
                s = [x for x in s if x != '\"']
                s = [x for x in s if x != '\n']
                self.att[r][c] = ''.join(s)
            self.att[r][0] = self.att[r][0].replace(" ", "_")

if __name__ == "__main__":
    converter = Converter('heart/heart_data.txt', 'heart/heart_att.txt')
    converter.convert()
