import json
import os

__author__ = "jkkim"

dirname = os.path.dirname
json_file = "database_info.json"
json_path = os.path.join(dirname(dirname(dirname(dirname(os.path.abspath(__file__))))), json_file)

with open(json_path, 'rt')as fin:
    data = json.load(fin)
multiple_split_param = data["multiple_split_params"]

gg_bac_ref_seq_path = data["gg_bac_ref_seq_path"]
gg_bac_taxonomy_path = data["gg_bac_taxonomy_path"]
gg_bac_chimera_path = data["gg_bac_chimera_path"]
gg_bac_param_path = data["gg_bac_param_path"]
gg_bac_div_param_path = data["gg_bac_div_param_path"]

silva_bac_ref_seq_path = data["silva_bac_ref_seq_path"]
silva_bac_taxonomy_path = data["silva_bac_taxonomy_path"]
silva_bac_chimera_path = data["silva_bac_chimera_path"]
silva_bac_param_path = data["silva_bac_param_path"]
silva_bac_div_param_path = data["silva_bac_div_param_path"]

its_ref_seq_path = data["its_ref_seq_path"]
its_taxonomy_path = data["its_taxonomy_path"]
its_chimera_path = data["its_chimera_path"]
its_param_path = data["its_param_path"]
