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

LEFSE="09.Lefse"
LEFSE_MAP="map.lefse"
JSON="otu.json"
biom2lefse="/app/src/Microbiome/microbiome_helper_pipeline/biom2lefse/biom2lefse"
LEFSE_1="lefse.1"
LEFSE_in="lefse.in"
LEFSE_res="lefse.res"
LEFSE_png="lefse.png"
Cladorgram="cladorgram.png"

mkdir -p $LEFSE

awk '{FS=OFS="\t"; print $1, $5}' $Map >  $LEFSE/$LEFSE_MAP

biom convert -i $Clustering/$Biom -o $LEFSE/$JSON --to-json --table-type="OTU table" --header-key taxonomy

python2 $biom2lefse -i $LEFSE/$JSON -f Description -o $LEFSE/$LEFSE_1 -m $LEFSE/$LEFSE_MAP

format_input.py $LEFSE/$LEFSE_1 $LEFSE/$LEFSE_in -c 1 -o 100000

run_lefse.py $LEFSE/$LEFSE_in $LEFSE/$LEFSE_res

plot_res.py $LEFSE/$LEFSE_res $LEFSE/$LEFSE_png

plot_cladogram.py $LEFSE/$LEFSE_res $LEFSE/$Cladorgram --format png
