import click

from qiime.automation.diversity_analysis.dendrogram_heatmap import DendrogramAndHeatmap


@click.command()
@click.option('-s', help="sample type is either bac or its.")
def main(s):
    sample_type = s
    DendroHeat = DendrogramAndHeatmap(sample_type)
    DendroHeat()
    print("dendrogram & heatmap work is done.")


if __name__ == '__main__':
    main()
