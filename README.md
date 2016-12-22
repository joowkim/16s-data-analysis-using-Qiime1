
Toy qiime nearly automation program for Miseq data (by default setting)
=======================================================================

### Required program list
1. python3
2. Qiime
3. click - pip install click
4. usearch6.x version
5. cutadapt

#### Note

Fastq file name should have \_R1_, \_R2_


####  param example
==> 16s_params.txt <==

pick_otus:enable_rev_strand_match True
assign_taxonomy:id_to_taxonomy_fp gg_13_8_otus/taxonomy/97_otu_taxonomy.txt
assign_taxonomy:reference_seqs_fp gg_13_8_otus/rep_set/97_otus.fasta

==> its_params.txt <==

pick_otus:enable_rev_strand_match True
assign_taxonomy:assignment_method blast
assign_taxonomy:id_to_taxonomy_fp its_unite/sh_taxonomy_qiime_ver7_dynamic_20.11.2016.txt
assign_taxonomy:reference_seqs_fp its_unite/sh_refs_qiime_ver7_dynamic_20.11.2016.fasta

#### Database path setting

As you probably downloaded the database, set those files paths to a setting file.

Go to qiime > automation > setting > db_path.py

Edit db_path.py file, this file is where you want to put the database paths.

(I am thinking about using Yaml or json for this.)


#### How to use
 
 To run preprocess and otu clustering
 
 ```python3 preprocess.py --help ```
 
 To run diversity analysis
 
 ```python3 postprocess.py --help```
 
 To generate upgma dendrogram
 
 ```upgma_cluster.py -i *dm.txt -o *.tre```



 
/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * <phk@FreeBSD.ORG> wrote this file. As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return jkkim
 * ----------------------------------------------------------------------------
 */
 
 
