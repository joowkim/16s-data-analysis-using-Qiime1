import glob
import os

import pylab
from Bio import Phylo

from qiime.automation.otu_cluster.otu_clustering import Biom
from qiime.automation.setting.settings import PathSettings

__author__ = "jkkim"


class DendrogramAndHeatmap(object):
    def __init__(self, taxon):
        self._settings_path = PathSettings(taxon)
        self._biom_path = Biom(taxon)

    @property
    def settings_path(self):
        return self._settings_path

    def make_dendrogram(self):
        tmp_bdiv_dir = [x for x in
                        os.listdir(self.settings_path.diversity_result_dir) if
                        x.startswith('bdiv')][0]
        tmp_dm_path = os.path.join(self.settings_path.diversity_result_dir,
                                   tmp_bdiv_dir, "*dm.txt")
        dm_path = sorted(
            [x for x in glob.glob(tmp_dm_path) if os.path.isfile(x)])

        tre_path = sorted(
            [os.path.splitext(x)[0] + ".tre" for x in dm_path])

        for dm, tre in zip(dm_path, tre_path):
            cmd = 'upgma_cluster.py -i {} -o {}'.format(
                dm,
                tre,
            )
            os.system(cmd)

        for tre in tre_path:
            tree = Phylo.read(tre, "newick")
            Phylo.draw(tree, do_show=False)
            pylab.axis("off")
            pylab.savefig(tre + ".png", format="png")

    def make_heatmap(self):
        biom_path = self._biom_path.biom_path

        cmd = '''summarize_taxa.py -i {} -o {} 
        '''.format(biom_path, self.settings_path.otu_heatmap_path)

        os.system(cmd)

        taxa_biom_list = sorted([i for i in glob.glob(os.path.join(self.settings_path.otu_heatmap_path,
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
