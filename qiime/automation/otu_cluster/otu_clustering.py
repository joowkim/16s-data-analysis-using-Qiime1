import glob
import os

from qiime.automation.setting.settings import PathSettings
from qiime.utils.utils import check_dir
from .krona import krona_main

__author__ = "jkkim"


class OTU(object):
    def __init__(self, PreProcess):
        self._settings_path = PathSettings(PreProcess.taxon)
        self._post_fix_cmd = ""
        self.set_cmd()
        self._threads = PreProcess._threads
        self.__taxon = PreProcess.taxon

    @property
    def seqs_chimeras_filtered_fna_path(self):
        return self._settings_path.seqs_chimeras_filtered_fna_path

    @property
    def setting_path(self):
        return self._settings_path

    def set_cmd(self):
        if self.setting_path.taxon == "its":
            self._post_fix_cmd = r'--suppress_align_and_tree'
        else:
            pass

    def run_otu_cluster(self):
        cmd = '''pick_closed_reference_otus.py -i {} -o {} -r {} -p {} {} -f -a -O {} -t {}'''.format(
            self.seqs_chimeras_filtered_fna_path,
            self.setting_path.otu_cluster_dir,
            self.setting_path.ref_seq_path,
            self.setting_path.param_path,
            self._post_fix_cmd,
            self._threads,
            self.setting_path.taxonomy_path
        )

        os.system(cmd)
        print("otu clustering done!")

    def run_biom(self):
        biom = Biom(self.__taxon)
        biom.get_biom_path()
        biom.make_otu_tables()
        biom.make_krona()


class Biom(object):
    def __init__(self, taxon):
        self._settings_path = PathSettings(taxon)
        self._otu_cluster_dir = self._settings_path.otu_cluster_dir
        self._biom_path = self.get_biom_path()
        # TODO dynamic path for otu_table_path some other time.
        self._otu_table_path = ""

    @property
    def biom_path(self):
        return self._biom_path

    def get_biom_path(self):
        check_dir(self._otu_cluster_dir)
        tmp_biom_path = os.path.join(self._otu_cluster_dir, "*.biom")
        pynast_biom_path = sorted([x for x in glob.glob(tmp_biom_path)],
                                  key=len,
                                  reverse=True, )[0]

        return pynast_biom_path

    def make_otu_tables(self):
        cmd = "biom summarize-table -i {} -o {}".format(
            self.biom_path,
            os.path.join(
                self._otu_cluster_dir,
                "stats_reads_per_sample.txt", )
        )
        os.system(cmd)

        cmd2 = "biom summarize-table -i {} -o {} --qualitative".format(
            self.biom_path,
            os.path.join(
                self._otu_cluster_dir,
                "stats_OTUs_per_sample.txt", )
        )
        os.system(cmd2)

        cmd3 = "biom convert -i {} -o {} --to-tsv --header-key taxonomy".format(
            self.biom_path,
            os.path.join(
                self._otu_cluster_dir,
                'otu_table.tsv.bak',
            )
        )

        os.system(cmd3)

        cmd4 = "alpha_diversity.py -i {} -o {} -m {}".format(
            self.biom_path,
            os.path.join(self._settings_path.final_path, "alpha_diversity_simpson_shannon_goodscor.txt"),
            "simpson,shannon,goods_coverage",
        )

        os.system(cmd4)

    def make_krona(self):
        otu_table_path = os.path.join(self._otu_cluster_dir, 'otu_table.tsv.bak')
        krona_otu_table_path = os.path.join(self._otu_cluster_dir, 'otu_table.tsv')

        if not os.path.isdir(self._settings_path._krona_path):
            os.makedirs(self._settings_path._krona_path)

        sed_cmd = "sed -n '1!p' {} | sed 's@;\ @;@g' > {}".format(otu_table_path, krona_otu_table_path)
        os.system(sed_cmd)

        krona_path = os.path.join(self._settings_path.krona_path, 'krona.html')
        krona_main(krona_otu_table_path, krona_path)

        print("generating krona.html is done.")
