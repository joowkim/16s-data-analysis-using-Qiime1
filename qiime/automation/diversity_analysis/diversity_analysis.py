import os

from qiime.automation.otu_cluster.otu_clustering import Biom
from qiime.automation.setting.settings import PathSettings

__author__ = "jkkim"


class DiversityAnalysis(object):
    def __init__(self, taxon, sampling_depth, ref_db, threads=1):
        self._settings_path = PathSettings(taxon, ref_db)
        self._biom_path = Biom(taxon)
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
            self._biom_path.filtered_biom_path,
            self.settings_path.diversity_result_dir,
            "map.txt",
            self._sampling_depth,
            self.post_fix_cmd,
            self._threads,
        )
        os.system(cmd)
