import os

from qiime.automation.otu_cluster.otu_clustering import OTU
from qiime.automation.preprocess.chimera_check import Chimera
from qiime.automation.preprocess.qiime_logs import Logs
from qiime.automation.setting.settings import PathSettings
from qiime.rename_for_qiime import rename_fastq_to_sampleid
from qiime.utils.utils import check_dir
from qiime.utils.utils import check_file

__author__ = "jkkim"


class PreProcess(object):
    def __init__(self, rawdata_dir, taxon, threads=1):
        self._settings_path = PathSettings(taxon)
        self._taxon = taxon
        self._rawdata_dir = rawdata_dir
        self._cur_dir_path = os.path.abspath(os.getcwd())

        self._cnt_join_fastq_dict = dict()
        self._sample_name_list = list()
        self._threads = threads

    @property
    def taxon(self):
        return self._taxon

    @property
    def rawdata_dir(self):
        return self._rawdata_dir

    @property
    def cur_dir_path(self):
        return self._cur_dir_path

    @property
    def cnt_join_fastq_dict(self):
        return self._cnt_join_fastq_dict

    @property
    def sample_name_list(self):
        return self._sample_name_list

    @property
    def settings_path(self):
        return self._settings_path

    def merge_fastq(self):
        cmd = "multiple_join_paired_ends.py -i {} -o {}".format(
            self.rawdata_dir,
            self.settings_path.join_fastq_dir,
        )
        os.system(cmd)

        os.chdir(self._cur_dir_path)
        print("multiple_join_paired_ends done!")

    # This function gets sample names!
    def rename_merged_fastq(self):
        check_dir(self.settings_path.join_fastq_dir)
        self._cnt_join_fastq_dict = rename_fastq_to_sampleid(
            self.settings_path.join_fastq_dir)
        self._sample_name_list = sorted(self._cnt_join_fastq_dict.keys())

        os.chdir(self._cur_dir_path)
        print("rename fastq.join.join.fastq done!")

    def multiple_split_run(self):
        check_dir(self.settings_path.join_fastq_dir)

        cmd = "multiple_split_libraries_fastq.py -i {} -o {} -p {}".format(
            self.settings_path.join_fastq_dir,
            self.settings_path.split_out_dir,
            self.settings_path.multiple_split_param,
        )
        os.system(cmd)
        os.chdir(self._cur_dir_path)
        print("multiple_split_run done!")

    def rename_trim_seqs_fna(self):
        check_dir(self.settings_path.split_out_dir)
        check_file(self.settings_path.seq_fna_path)

        sed_cmd = "sed -i {} -e 's/.fastq//g'".format(
            self.settings_path.seq_fna_path,
        )

        os.system(sed_cmd)

        cutadat_cmd = "cutadapt {} -m 400 -o {} -M 470".format(
            self.settings_path.seq_fna_path,
            self.settings_path.length_trimmed_seqs_fna_path,

        )
        os.system(cutadat_cmd)
        os.chdir(self.cur_dir_path)
        # print("rename and trim length seqs.fna done!")

    def make_map_file(self):
        with open("map.txt", 'wt')as fout:
            fout.write("#SampleID" + "\n")
            for i in self._sample_name_list:
                fout.write(i + "\n")

    def preprocess_run(self):
        self.merge_fastq()
        self.rename_merged_fastq()
        self.multiple_split_run()
        self.rename_trim_seqs_fna()
        chimera = Chimera(self)
        chimera.check_chimera()
        chimera.filter_chimera()
        logs = Logs(self)
        # this function is for creating a map file.
        self.make_map_file()

        otu = OTU(self)
        otu.run_otu_cluster()
        otu.run_biom()
        logs.write_logs(logs.make_logs())
