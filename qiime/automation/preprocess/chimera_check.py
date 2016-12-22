import os

from work.microbiome.qiime.automation.setting.settings import PathSettings

__author__ = "jkkim"


class Chimera(object):
    def __init__(self, PreProcess):
        self._settings_path = PathSettings(PreProcess.taxon)

    @property
    def settings_path(self):
        return self._settings_path

    def check_chimera(self):
        cmd = '''identify_chimeric_seqs.py -i {} -m {} -o {} -r {}'''.format(
            self.settings_path.length_trimmed_seqs_fna_path,
            "usearch61",
            self.settings_path.chimera_checked_dir,
            self.settings_path.chimera_ref_path,
        )

        os.system(cmd)

    def filter_chimera(self):
        cmd = 'filter_fasta.py -f {} -o {} -s {} -n'.format(
            self.settings_path.length_trimmed_seqs_fna_path,
            self.settings_path.seqs_chimeras_filtered_fna_path,
            os.path.join(self.settings_path.chimera_checked_dir,
                         "chimeras.txt", )
        )

        os.system(cmd)
        print("remove chimera sequences done!")
