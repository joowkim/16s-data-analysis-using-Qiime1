SamplingDepth=$1
Threads=$2
StichedReads="01.StichedReads"
FilteredFq="02.FilteredFq"
FastaFiles="03.FastaFiles"
RemovedChimera="04.RemovedChimera"
CombinedFasta="05.CombinedFasta"
Clustering="06.Clustering"
RDP_DataSet="/app/src/Microbiome/qiime_db/rdp/RDP_trainset16_022016.fa"
Biom="otu_table.biom"
Diversity="07.Diversity"
Map="map.txt"
TREE="/app/src/Microbiome/qiime_db/gg_13_8_otus/trees/99_otus.tree"
Param="/app/src/Microbiome/qiime_db/params/16s_div.txt"
PICRUST="08.Picrust"
PICRUST_BIOM="otus_corrected.biom"
PICRUST_TXT="otus_Corrected.txt"
KO_PREDICTION_BIOM="ko_predictions.biom"
KO_PREDICTION_TXT="ko_predictions.txt"
PATHWAY_PREDICTION_BIOM="pathway_predictions_biom"
PATHWAY_PREDICTION_TXT="pathway_predictions_txt"
otus_corrected_spf="otus_corrected.spf"
ko_prediction_spf="ko_predictions.spf"
pathway_prediction_spf="pathway_predictions.spf"


## correct otu table
mkdir -p $PICRUST

normalize_by_copy_number.py -i $Clustering/$Biom -o $PICRUST/$PICRUST_BIOM 

##
biom convert -i $PICRUST/$PICRUST_BIOM -o $PICRUST/$PICRUST_TXT --to-tsv --header-key taxnomy

##
predict_metagenomes.py -i $PICRUST/$PICRUST_BIOM -o $PICRUST/$KO_PREDICTION_BIOM

##
biom convert -i $PICRUST/$KO_PREDICTION_BIOM -o $PICRUST/$KO_PREDICTION_TXT --to-tsv --header-key KEGG_Description

##
categorize_by_function.py -i $PICRUST/$KO_PREDICTION_BIOM -c KEGG_Pathways -l 3 -o $PICRUST/$PATHWAY_PREDICTION_BIOM

##
biom convert -i $PICRUST/$PATHWAY_PREDICTION_BIOM -o $PICRUST/$PATHWAY_PREDICTION_TXT --to-tsv --header-key KEGG_Pathways

##
biom_to_stamp.py -m taxonomy $PICRUST/$PICRUST_BIOM > $PICRUST/$otus_corrected_spf
biom_to_stamp.py -m KEGG_Description $PICRUST/$KO_PREDICTION_BIOM > $PICRUST/$ko_prediction_spf
biom_to_stamp.py -m KEGG_Pathways $PICRUST/$PATHWAY_PREDICTION_BIOM > $PICRUST/$pathway_prediction_spf
