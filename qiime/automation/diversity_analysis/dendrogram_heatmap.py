import glob
import os

from qiime.automation.otu_cluster.otu_clustering import Biom
from qiime.automation.setting.settings import PathSettings

__author__ = "jkkim"


class DendrogramAndHeatmap(object):
    def __init__(self, taxon):
        self._settings_path = PathSettings(taxon)
        self._biom_path = Biom(self.settings_path.otu_cluster_dir)

    @property
    def settings_path(self):
        return self._settings_path

    def make_dendrogram(self):
        tmp_bdiv_dir = [x for x in
                        os.listdir(self.settings_path.diversity_result_dir) if
                        x.startswith('bdiv')][0]
        bdiv_dir = os.path.join(self.settings_path.diversity_result_dir,
                                tmp_bdiv_dir)
        tmp_dm_path = os.path.join(self.settings_path.diversity_result_dir,
                                   bdiv_dir, "*dm.txt")
        dm_path = sorted(
            [x for x in glob.glob(tmp_dm_path) if os.path.isfile(x)])

        tre_path = sorted(
            [os.path.splitext(os.path.basename(x))[0] for x in dm_path])

        for dm, tre in zip(dm_path, tre_path):
            cmd = 'upgma_cluster.py -i {} -o {}.tre'.format(
                dm,
                os.path.join('result', tre)
            )

            os.system(cmd)
            print(cmd)

    def make_heatmap(self):
        biom_path = self._biom_path.biom_path

        cmd = '''summarize_taxa.py -i {} -o {} 
        '''.format(biom_path, self.settings_path.summarize_taxa_outpath)

        os.system(cmd)

        taxa_biom_list = sorted([i for i in glob.glob(os.path.join(self.settings_path.summarize_taxa_outpath,
                                                                   "*.biom")
                                                      )
                                 ])

        heatmap_list = sorted([os.path.splitext(i)[0] + ".heatmap.pdf" for i in taxa_biom_list])

        for biom, heatmap in zip(taxa_biom_list, heatmap_list):
            cmd2 = '''make_otu_heatmap.py -i {} -o {}
            '''.format(biom, heatmap)

            os.system(cmd2)

    def __call__(self, *args, **kwargs):
        self.make_dendrogram()
        self.make_heatmap()
