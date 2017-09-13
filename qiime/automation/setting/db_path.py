import json
import os

__author__ = "jkkim"

dirname = os.path.dirname
json_file = "database_info.json"
json_path = os.path.join(dirname(dirname(dirname(dirname(os.path.abspath(__file__))))), json_file)

with open(json_path, 'rt')as fin:
    data = json.load(fin)
multiple_split_param = data["multiple_split_params"]
bac_ref_seq_path = data["bac_ref_seq_path"]
bac_taxonomy_path = data["bac_taxonomy_path"]
bac_chimera_path = data["bac_chimera_path"]
bac_param_path = data["bac_param_path"]
bac_div_param_path = data["bac_div_param_path"]

its_ref_seq_path = data["its_ref_seq_path"]
its_taxonomy_path = data["its_taxonomy_path"]
its_chimera_path = data["its_chimera_path"]
its_param_path = data["its_param_path"]
