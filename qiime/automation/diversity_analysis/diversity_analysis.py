import glob
import os

from qiime.automation.otu_cluster.otu_clustering import Biom
from qiime.automation.setting.settings import PathSettings

__author__ = "jkkim"


class DiversityAnalysis(object):
    def __init__(self, taxon, sampling_depth, threads=1):
        self._settings_path = PathSettings(taxon)
        self._biom_path = Biom(self.settings_path.otu_cluster_dir)
        self._post_fix_cmd = ""
        self._tre_path = os.path.join(self.settings_path.otu_cluster_dir,
                                      'rep_set.tre', )
        self._sampling_depth = sampling_depth
        self._threads = threads

    @property
    def settings_path(self):
        return self._settings_path

    @property
    def post_fix_cmd(self):
        return self.get_post_fix_cmd()

    def get_post_fix_cmd(self):
        if self.settings_path.taxon == 'its':
            self._post_fix_cmd = '--nonphylogenetic_diversity'
        else:
            # this is for bacteria!
            self._post_fix_cmd = '-t {} -p {}'.format(self._tre_path, self.settings_path.div_param_path)
        return self._post_fix_cmd

    def run_core_diversity(self):
        cmd = '''core_diversity_analyses.py -i {} -o {} -m {} -e {} {} -a -O {}
        '''.format(
            self._biom_path.biom_path,
            self.settings_path.diversity_result_dir,
            "map.txt",
            self._sampling_depth,
            self.post_fix_cmd,
            self._threads,
        )

        os.system(cmd)

    # deprecated
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
