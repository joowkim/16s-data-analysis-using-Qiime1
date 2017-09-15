import click

from qiime.automation.diversity_analysis.dendrogram_heatmap import DendrogramAndHeatmap


@click.command()
@click.option('-s', help="sample type is either bac or its.")
@click.option('-r', help="ref database is either gg or silva.")
def main(s):
    sample_type = s
    DendroHeat = DendrogramAndHeatmap(sample_type, ref_db)
    DendroHeat()
    print("dendrogram & heatmap work is done.")


if __name__ == '__main__':
    main()
