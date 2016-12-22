import sys

__author__ = "jkkim"

from seq_tools.parse_fasta import parse_fasta


def rewrite_fa(fasta):
    with open(fasta, 'rt')as fin, open("trimmed" + fasta, 'wt')as fout:
        for name, seq in parse_fasta(fin):
            rename = name.replace('.fastq', '')
            fout.write(rename + "\n")
            fout.write(seq + "\n")


def main(fasta):
    rewrite_fa(fasta)


if __name__ == '__main__':
    main(sys.argv[1])
