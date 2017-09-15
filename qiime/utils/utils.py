import glob
import gzip
import os
from collections import defaultdict

__author__ = "jkkim"


def parse_fasta(fa_handler):
    '''
    takes a file handler. so if you want to use this function then put the with statement before this function
    :param fa_handler:
    :return:
    '''
    name, seq = None, []
    for line in fa_handler:
        line = line.strip()
        if line.startswith(">"):
            if name:
                yield (name, ''.join(seq))
            name = line.split()[0][1:]
            seq = []
        else:
            seq.append(line)
    if name:
        yield (name, ''.join(seq))


def count_fq_gz(fname):
    with gzip.open(fname, 'rt')as fin:
        for i, _ in enumerate(fin, start=1):
            pass
    return i / 4


def count_file(fname):
    with open(fname, 'rt') as fin:
        for i, _ in enumerate(fin, start=1):
            pass
    return i


def check_dir(dir):
    if not os.path.isdir(dir):
        print(
            "{} is not found!".format(
                dir,
            )
        )
        raise ValueError


def check_file(file_name):
    if not os.path.isfile(file_name):
        print(
            "{} is not found!".format(
                file_name,
            )
        )
        raise ValueError


def count_fasta(fname):
    cnt = 0
    with open(fname, 'rt')as fin:
        for line in fin:
            if line.startswith(">"):
                cnt += 1

    return cnt


def count_sample_reads_fa(sample_list, fasta):
    result = defaultdict(int)
    sample_set = set(sample_list)

    with open(fasta, 'rt')as fin:
        for gene, _ in parse_fasta(fin):
            sample_id = gene.split("_")[0]
            if sample_id in sample_set:
                result[sample_id] += 1

    return result


def count_trimmed_gz(input_dir):
    result = defaultdict(int)
    fq_list = [i for i in glob.glob(os.path.join(input_dir, "*_R1_*.gz")) if os.path.isfile(i)]

    for i in fq_list:
        sample_name = os.path.basename(i).split("_")[0]
        result[sample_name] = count_fq_gz(i)
    return result
