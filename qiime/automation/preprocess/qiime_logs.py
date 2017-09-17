import os
from typing import NamedTuple

from collections import defaultdict

from qiime.automation.otu_cluster.otu_clustering import Biom
from qiime.automation.setting.settings import PathSettings
from qiime.utils.utils import count_sample_reads_fa
from qiime.utils.utils import count_trimmed_gz

__author__ = "jkkim"


class Data(NamedTuple):
    sample_name: str
    qual_trimmed_reads: int
    merged_reads: int
    chimera_reads: int
    cleaned_reads: int


class Logs(object):
    def __init__(self, PreProcess):
        if not os.path.isdir("02.Logs"):
            os.makedirs("02.Logs")

        self._rawdata_dir = os.path.abspath(PreProcess.rawdata_dir)
        self._taxon = PreProcess.taxon
        self._settings_path = PathSettings(PreProcess.taxon, PreProcess.ref_db)
        self._logs_path = os.path.join('02.Logs', 'reads_stat.log')

        self._cnt_join_fastq_dict = PreProcess.cnt_join_fastq_dict

        self._sample_name_list = sorted(self._cnt_join_fastq_dict.keys())

        self._cnt_chimera_filtered_reads_dict = count_sample_reads_fa(
            self._sample_name_list,
            self.settings_path.seqs_chimeras_filtered_fna_path
        )

        self._reads_logs_list = list()

        self._trimmed_fq_read_dict = count_trimmed_gz(self._rawdata_dir)

    @property
    def logs_path(self):
        return self._logs_path

    @property
    def settings_path(self):
        return self._settings_path

    def make_map_file(self):
        with open("map.txt", 'wt')as fout:
            fout.write("#SampleID" + "\n")
            for i in self._sample_name_list:
                fout.write(i + "\n")

    def make_logs(self):
        result = list()
        biom = Biom(self._taxon)

        stat_file = os.path.join(biom._otu_cluster_dir, "stats_reads_per_sample.txt")

        clean_raw_reads_dict = defaultdict(float)
        for sample_name in self._sample_name_list:
            with open(stat_file, 'rt')as fin:
                for line in fin:
                    if line.startswith(sample_name):
                        sample = line.split(":")[0]
                        num = float(line.split(":")[1].strip())
                        clean_raw_reads_dict[sample] = num

        for i in self._trimmed_fq_read_dict:
            data = Data(sample_name=i,
                        qual_trimmed_reads=self._trimmed_fq_read_dict[i],
                        merged_reads=self._cnt_join_fastq_dict[i],
                        chimera_reads=self._cnt_chimera_filtered_reads_dict[i],
                        cleaned_reads=clean_raw_reads_dict[i]
                        )
            result.append(data)

        return result

    def write_logs(self, reads_log_list):
        with open(self._logs_path, 'wt')as fout:
            fout.write("sample_name trimmed_reads   merged_reads    chimera_reads   cleaned_reads\n")

            for i in reads_log_list:
                tmp = "{},{},{},{},{}\n".format(i.sample_name,
                                                i.qual_trimmed_reads,
                                                i.merged_reads,
                                                i.chimera_reads,
                                                i.cleaned_reads, )
                fout.write(tmp)


                # fout.write("---merged fastq reads----\n")
                # for sample_id in sorted(self._cnt_join_fastq_dict.keys()):
                #     fout.write(
                #         sample_id + "\t" +
                #         round(
                #             self._cnt_join_fastq_dict[sample_id]).__str__() + "\n"
                #     )
                #
                # fout.write("---length trim reads-----\n")
                #            cnt_length_trim_reads_dict = count_sample_reads_fa(
                #                self._sample_name_list,
                #                self.settings_path.length_trimmed_seqs_fna_path
                #            )
                #            for sample_id in sorted(cnt_length_trim_reads_dict.keys()):
                #                fout.write(sample_id + "\t" + cnt_length_trim_reads_dict[
                #                    sample_id].__str__() + "\n")
                #
                # fout.write("---chimera trim reads-----\n")
                # cnt_chimera_filtered_reads_dict = count_sample_reads_fa(
                #     self._sample_name_list,
                #     self.settings_path.seqs_chimeras_filtered_fna_path
                # )
                #
                # for sample_id in sorted(cnt_chimera_filtered_reads_dict.keys()):
                #     fout.write(sample_id + "\t" + cnt_chimera_filtered_reads_dict[
                #         sample_id].__str__() + "\n")
