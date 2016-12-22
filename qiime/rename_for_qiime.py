import glob
import os
import sys

__author__ = "jkkim"


def rename_fastq_to_sampleid(start_dir):
    result_dict = dict()
    cur_path = os.getcwd()

    os.chdir(start_dir)

    dir_list = [x for x in glob.glob("*") if os.path.isdir(x)]

    for dir in dir_list:
        sample_id = dir.split("_")[0]
        os.chdir(dir)
        fastq_file = [x for x in glob.glob("*.fastq") if
                      os.path.isfile(x)]
        for i in fastq_file:
            if "fastqjoin.join.fastq" in i:
                print(i, ">", sample_id + ".fastq")
                os.rename(i, sample_id + ".fastq")

                # call count fastq reads!
                cnt = count_fastq(sample_id + ".fastq")

                result_dict[sample_id] = cnt

            elif "fastqjoin.un" in i:
                os.rename(i, i + "_")
            else:
                pass

        os.chdir("../")

    os.chdir(cur_path)
    return result_dict


def count_fastq(fname):
    with open(fname) as f:
        for i, _ in enumerate(f, start=1):
            pass
    return i / 4


if __name__ == '__main__':
    rename_fastq_to_sampleid(sys.argv[1])
