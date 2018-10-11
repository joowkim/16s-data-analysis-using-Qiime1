# Title     : TODO
# Objective : TODO
# Created by: jkim
# Created on: 2018-10-10
library("tidyverse")

map.txt <- "E:/test/map.txt"
map <- read_tsv(map.txt)

shannon.txt <- "E:/test/shannon.txt"
pdtree.txt <- "E:/test/PD_whole_tree.txt"
sim.txt <- "E:/test/simpson.txt"

tmp <- read_tsv(shannon.txt)
tmp <- tmp %>% tail(10)
sh <- tmp %>% select(-X1, -`sequences per sample`, -iteration)
sh <- sh %>% summarise_all(funs(mean))

sh.df.long <- sh %>% gather(Sample, value)
sh.merge.df <- merge(x = sh.df.long, y = map.df, by.x="Sample", by.y="SampleID")
sh.merge.df$Index <- "Shannon"

tmp <- read_tsv(pdtree.txt)
tmp <- tmp %>% tail(10)
pd <- tmp %>% select(-X1, -`sequences per sample`, -iteration)
pd <- pd %>% summarise_all(funs(mean))

pd.df.long <- pd %>% gather(Sample, value)
pd.merge.df <- merge(x = pd.df.long, y = map.df, by.x="Sample", by.y="SampleID")
pd.merge.df$Index <- "PD-whole-tree"


tmp <- read_tsv(shannon.txt)
tmp <- tmp %>% tail(10)
sim <- tmp %>% select(-X1, -`sequences per sample`, -iteration)
sim <- sim %>% summarise_all(funs(mean))

sim.df.long <- sim %>% gather(Sample, value)
sim.merge.df <- merge(x = sim.df.long, y = map.df, by.x="Sample", by.y="SampleID")
sim.merge.df$Index <- "Inverse Simpson"


final.df <- rbind(pd.merge.df, sh.merge.df)
final.df <- rbind(final.df, sim.merge.df)


ggplot(final.df) + geom_boxplot(aes(x=Description, y=value, color=Description)) + theme_bw() + theme(plot.title = element_text(hjust = 0.5)) + 
  xlab("") + ylab("") + facet_wrap(~Index, scale="free") + 
  theme(axis.title.y=element_text(size=15), axis.title.x=element_text(size=15)) +
  theme(text=element_text(size=15)) + scale_fill_brewer(palette="Set3") +
  labs(color = "Sample") + theme(legend.text=element_text(size=15))

ggsave(paste0("alpha",'.tiff'), width=20, height=10, units="cm", dpi=900)
