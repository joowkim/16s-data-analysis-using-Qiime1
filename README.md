
Deprecated
===================================================================

### Required program list
1. python3
2. Qiime
3. click - pip install click
4. usearch6.x version
5. cutadapt
6. krona

How to install required tools

conda install above tools -y -c bioconda

---------
#### Note

Fastq file names shouldn't be modified.

------
####  param example
==> 16s_params.txt <==

pick_otus:enable_rev_strand_match True

assign_taxonomy:id_to_taxonomy_fp gg_13_8_otus/taxonomy/97_otu_taxonomy.txt

assign_taxonomy:reference_seqs_fp gg_13_8_otus/rep_set/97_otus.fasta

==> 16s_div.txt <==

alpha_diversity:metrics shannon,simpson,observed_otus,PD_whole_tree,chao1

beta_diversity:metrics unweighted_unifrac,weighted_unifrac

==> its_params.txt <==

pick_otus:enable_rev_strand_match True

assign_taxonomy:assignment_method blast

assign_taxonomy:id_to_taxonomy_fp its_unite/sh_taxonomy_qiime_ver7_dynamic_20.11.2016.txt

assign_taxonomy:reference_seqs_fp its_unite/sh_refs_qiime_ver7_dynamic_20.11.2016.fasta

-----

#### Database path setting

As you probably downloaded the database, set those files paths to a database_info.json.


----------------------
#### How to use
 
 To run preprocess and otu clustering
 
 ```python3 preprocess.py --help ```
 
 To run diversity analysis
 
 ```python3 postprocess.py --help```
 
 To generate upgma dendrogram
 
 ```upgma_cluster.py -i *dm.txt -o *.tre```


------

### License

 * "THE BEER-WARE LICENSE" (Revision 42):
 * <phk@FreeBSD.ORG> wrote this file. As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return jkkim


 
 
