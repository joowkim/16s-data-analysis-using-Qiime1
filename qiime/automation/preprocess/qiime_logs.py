import os

from qiime.automation.setting.settings import PathSettings
from qiime.utils.utils import count_sample_reads_fa

__author__ = "jkkim"


class Logs(object):
    def __init__(self, PreProcess):
        if not os.path.isdir("03.Logs"):
            os.makedirs("03.Logs")

        self._settings_path = PathSettings(PreProcess.taxon)
        self._logs_path = os.path.join('03.Logs', 'reads_stat.log')

        self._cnt_join_fastq_dict = PreProcess._cnt_join_fastq_dict

        self._sample_name_list = sorted(self._cnt_join_fastq_dict.keys())

    @property
    def logs_path(self):
        return self._logs_path

    @property
    def settings_path(self):
        return self._settings_path

    def write_sample_id(self):
        with open("map.txt", 'wt')as fout:
            fout.write("#SampleID" + "\n")
            for i in self._sample_name_list:
                fout.write(i + "\n")

    def write_logs(self):
        with open(self._logs_path, 'wt')as fout:
            fout.write("sample_id   reads\n")

            fout.write("---merged fastq reads----\n")
            for sample_id in sorted(self._cnt_join_fastq_dict.keys()):
                fout.write(
                    sample_id + "\t" +
                    round(
                        self._cnt_join_fastq_dict[sample_id]).__str__() + "\n"
                )

            fout.write("---length trim reads-----\n")
            cnt_length_trim_reads_dict = count_sample_reads_fa(
                self._sample_name_list,
                self.settings_path.length_trimmed_seqs_fna_path
            )
            for sample_id in sorted(cnt_length_trim_reads_dict.keys()):
                fout.write(sample_id + "\t" + cnt_length_trim_reads_dict[
                    sample_id].__str__() + "\n")

            fout.write("---chimera trim reads-----\n")
            cnt_chimera_filtered_reads_dict = count_sample_reads_fa(
                self._sample_name_list,
                self.settings_path.seqs_chimeras_filtered_fna_path
            )

            for sample_id in sorted(cnt_chimera_filtered_reads_dict.keys()):
                fout.write(sample_id + "\t" + cnt_chimera_filtered_reads_dict[
                    sample_id].__str__() + "\n")
