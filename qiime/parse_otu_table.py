import sys

import pandas as pd

__author__ = "jkkim"


def get_samples(tsv_file):
    sample_list = None
    with open(tsv_file, 'rt')as fin:
        fin.readline()
        sample_list = fin.readline().strip().split("\t")

    # remove #OTU ID and taxonomy
    return sample_list[1:-1]


def write_sample_csv(tsv_file, sample_list):
    otu_table = pd.read_csv(tsv_file, sep="\t", skiprows=1)

    for sample in sample_list:
        otu = otu_table[['#OTU ID', sample, 'taxonomy']]
        otu[otu[sample] > 0].to_csv(sample + ".csv", sep=",", index=False)
        print("the otu {} table is generated!".format(sample))


def main(tsv_file):
    sample_list = get_samples(tsv_file)
    write_sample_csv(tsv_file, sample_list)


if __name__ == '__main__':
    test = r'test_otu_table/otu_tables.tsv'
    main(test)
    main(sys.argv[1])
