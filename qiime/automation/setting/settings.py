import os

from qiime.automation.setting.db_path import gg_bac_chimera_path
from qiime.automation.setting.db_path import gg_bac_div_param_path
from qiime.automation.setting.db_path import gg_bac_param_path
from qiime.automation.setting.db_path import gg_bac_ref_seq_path
from qiime.automation.setting.db_path import gg_bac_taxonomy_path

from qiime.automation.setting.db_path import silva_bac_chimera_path
from qiime.automation.setting.db_path import silva_bac_div_param_path
from qiime.automation.setting.db_path import silva_bac_param_path
from qiime.automation.setting.db_path import silva_bac_ref_seq_path
from qiime.automation.setting.db_path import silva_bac_taxonomy_path

from qiime.automation.setting.db_path import its_chimera_path
from qiime.automation.setting.db_path import its_param_path
from qiime.automation.setting.db_path import its_ref_seq_path
from qiime.automation.setting.db_path import its_taxonomy_path
from qiime.automation.setting.db_path import multiple_split_param

__author__ = "jkkim"


class PathSettings(object):
    def __init__(self, taxon, ref_db):
        self._ref_db = ref_db
        self._default_preprocess_dir = '01.Preprocess'
        self._join_fastq_dir = os.path.join(self._default_preprocess_dir,
                                            '01.1.Join_fastq', )
        self._split_out_dir = os.path.join(self._default_preprocess_dir,
                                           '01.2.Split_out', )
        self._seq_fna_path = os.path.join(self._split_out_dir,
                                          "seqs.fna", )
        self._length_trimmed_seqs_fna_path = os.path.join(self._split_out_dir,
                                                          "seqs.length_trimmed.fna", )
        self._chimera_checked_dir = os.path.join(self._default_preprocess_dir,
                                                 "01.3.Chimera_checked", )
        self._seqs_chimeras_filtered_fna_path = os.path.join(
            self._chimera_checked_dir,
            "seqs_chimeras_filtered.fna", )
        self._sample_taxon = taxon
        self._chimera_ref_path = None
        self._ref_seq_path = None
        self._taxonomy_path = None
        self._param_path = None
        self._multiple_split_param = multiple_split_param

        self._default_analysis_dir = "03.OTU_clustering_result"
        self._otu_cluster_dir = os.path.join(self._default_analysis_dir,
                                             "03.1.otu_clustering_{}".format(
                                                 taxon), )
        self.set_ref_database()

        self._final_dir = "04.Diversity_results"

        if not os.path.isdir(self._final_dir):
            os.makedirs(self._final_dir)

        self._final_path = os.path.abspath(self._final_dir)

        self._krona_path = os.path.join(self._final_path, "04.2.Krona")
        self._otu_heatmap_path = os.path.join(self._final_path, "04.3.Heatmap")

        self._diversity_result_dir = os.path.join(self._final_path,
                                                  '04.1.diversity_analysis_{}'.format(
                                                      taxon), )
        self._pcoa_2d_dir = os.path.join(self.final_path, "04.4.PcoA.2d")

        self._map_file_path = os.path.join(os.getcwd(), "map.txt")

    @property
    def multiple_split_param(self):
        return self._multiple_split_param

    @property
    def map_file_path(self):
        return self._map_file_path

    @property
    def pcao_2d_path(self):
        return self._pcoa_2d_dir

    @property
    def krona_path(self):
        return self._krona_path

    @property
    def otu_heatmap_path(self):
        return self._otu_heatmap_path

    @property
    def final_path(self):
        return self._final_path

    @property
    def diversity_result_dir(self):
        return self._diversity_result_dir

    @property
    def taxon(self):
        return self._sample_taxon

    @property
    def seq_fna_path(self):
        return self._seq_fna_path

    @property
    def split_out_dir(self):
        return self._split_out_dir

    @property
    def join_fastq_dir(self):
        return self._join_fastq_dir

    @property
    def length_trimmed_seqs_fna_path(self):
        return self._length_trimmed_seqs_fna_path

    @property
    def seqs_chimeras_filtered_fna_path(self):
        return self._seqs_chimeras_filtered_fna_path

    @property
    def chimera_checked_dir(self):
        return self._chimera_checked_dir

    @property
    def chimera_ref_path(self):
        return self._chimera_ref_path

    @property
    def param_path(self):
        return self._param_path

    @property
    def ref_seq_path(self):
        return self._ref_seq_path

    @property
    def otu_cluster_dir(self):
        return self._otu_cluster_dir

    @property
    def div_param_path(self):
        return self._div_param_path

    @property
    def taxonomy_path(self):
        return self._taxonomy_path

    def set_ref_database(self):
        if self._ref_db == "gg":
            self._chimera_ref_path = gg_bac_chimera_path
            self._ref_seq_path = gg_bac_ref_seq_path
            self._taxonomy_path = gg_bac_taxonomy_path
            self._param_path = gg_bac_param_path
            self._div_param_path = gg_bac_div_param_path

        elif self._ref_db == "silva":
            self._chimera_ref_path = silva_bac_chimera_path
            self._ref_seq_path = silva_bac_ref_seq_path
            self._taxonomy_path = silva_bac_taxonomy_path
            self._param_path = silva_bac_param_path
            self._div_param_path = silva_bac_div_param_path

        elif self._ref_db == "unite":
            self._chimera_ref_path = its_chimera_path
            self._ref_seq_path = its_ref_seq_path
            self._taxonomy_path = its_taxonomy_path
            self._param_path = its_param_path
        else:
            raise ValueError("ref db should be either gg or silva!")
