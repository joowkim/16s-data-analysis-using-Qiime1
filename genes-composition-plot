# Title     : TODO
# Objective : TODO
# Created by: jkim
# Created on: 2018-10-10
library("tidyverse")

otu.table <- "E:/test/Description_otu_table_L6.txt"

group1 <-"KHASs"
group2 <- "HKAs"


taxa <- read.delim(otu.table, sep="\t", row=1)

split <- strsplit(rownames(taxa),";")
taxaStrings <- sapply(split,function(x) paste(x[1:6],collapse=";"))
gtaxa <- taxa
splitg <- strsplit(rownames(gtaxa),";")                               # Split and rejoin on lv7
gtaxaStrings <- sapply(splitg,function(x) paste(x[1:6],collapse=";")) # level 7 is species, 8 is strain, 6 is genera
gtaxa <- rowsum(gtaxa,gtaxaStrings)                                    # Collapse by taxonomy name
gtaxa <- sweep(gtaxa,2,colSums(gtaxa),'/')
gtaxa <- gtaxa[order(rowMeans(gtaxa),decreasing=T),]


rownam <- row.names(filtered.taxa)
filtered.taxa <- gtaxa * 100
#etc <- filtered.taxa[filtered.taxa$KHASs >= 1 | filtered.taxa$HKAs >= 1,]
#filtered.taxa$Genus <- rownam
etc <- filtered.taxa %>%  rownames_to_column("Genus") %>% filter_(paste(group1, ">= 1 | ", group2, ">= 1")) %>% column_to_rownames("Genus")

#rownames(etc) <- rownam
#filtered.taxa <- gtaxa * 100
#traspose to add to map for later use
etc.t <- t(etc)
colnames(etc.t) <- gsub(".*;g__?", "", colnames(etc.t))
colnames(etc.t) <- gsub("_", "", colnames(etc.t))
colnames(etc.t) <- gsub(";.*","",colnames(etc.t))

etc.df <- as.data.frame(etc.t)
## v777 is for others
etc.df$V777 <-  100 - rowSums(etc.df)

tmp <- etc.df[, order(colnames(etc.df))]
colnames(etc.df)
tmp <- t(etc.df)
sth <-as.data.frame(tmp)
sth$Genus <- row.names(sth)
row.names(sth) <- NULL

others <- sth %>% filter(str_detect(Genus, "V[123456789]")) %>% select(-Genus) %>% summarise_all(funs(sum))
others$Genus <- "Others"

mid <- sth %>% filter(!str_detect(Genus, "V[123456789]"))

final <- rbind(mid, others)

final %>% select(-Genus) %>% summarise_all(sum)

rnd <- function(num) { return (round(num,3))}

final <- final %>% mutate_if(is.numeric, rnd)


write_csv(final, "genus-composition.csv")

long <- gather(final, key = "Sample", value = "Proportion", -Genus)

p <- ggplot(long) + geom_bar(aes(x=Sample, y=Proportion, fill=Genus), stat = "identity")+ theme_light() +
  ylab("Proportion (%)")  + theme(axis.title.y=element_text(size=15), axis.title.x=element_text(size=15)) +
  theme(text=element_text(size=15))  +  theme(axis.text.x=element_text(size=17)) + xlab("")
  theme(axis.text.y=element_text(size=20)) + theme(legend.text=element_text(size=15)) +theme(legend.title=element_text(size=15))
p  


ggsave(paste0("Genus-plot",'.tiff'), width=12.5, height=10, units="cm", dpi = 900)
