import os

from qiime.automation.setting.db_path import bac_chimera_path
from qiime.automation.setting.db_path import bac_div_param_path
from qiime.automation.setting.db_path import bac_param_path
from qiime.automation.setting.db_path import bac_ref_seq_path
from qiime.automation.setting.db_path import bac_taxonomy_path
from qiime.automation.setting.db_path import its_chimera_path
from qiime.automation.setting.db_path import its_param_path
from qiime.automation.setting.db_path import its_ref_seq_path
from qiime.automation.setting.db_path import its_taxonomy_path

__author__ = "jkkim"


class PathSettings(object):
    def __init__(self, taxon):
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

        self._default_analysis_dir = "02.Results"
        self._otu_cluster_dir = os.path.join(self._default_analysis_dir,
                                             "02.1.otu_clustering_{}".format(
                                                 taxon), )
        self._diversity_result_dir = os.path.join(self._default_analysis_dir,
                                                  '02.2.diversity_analysis_{}'.format(
                                                      taxon), )
        self.set_type_taxon()

        self._summarize_taxa_outpath = os.path.join(self._otu_cluster_dir, "taxa")

    @property
    def summarize_taxa_outpath(self):
        return self._summarize_taxa_outpath

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

    def set_type_taxon(self):
        if self._sample_taxon == 'bac':
            self._chimera_ref_path = bac_chimera_path
            self._ref_seq_path = bac_ref_seq_path
            self._taxonomy_path = bac_taxonomy_path
            self._param_path = bac_param_path
            self._div_param_path = bac_div_param_path

        elif self._sample_taxon == "its":
            self._chimera_ref_path = its_chimera_path
            self._ref_seq_path = its_ref_seq_path
            self._taxonomy_path = its_taxonomy_path
            self._param_path = its_param_path
        else:
            print("taxon is either bac or its!")
            quit()
