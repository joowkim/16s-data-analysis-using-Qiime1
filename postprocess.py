import click

from qiime.automation.diversity_analysis.diversity_analysis import \
    DiversityAnalysis

__author__ = "jkkim"


@click.command()
@click.option('-s', help="sample type is either bac or its.")
@click.option('-t', type=int, help="threads.")
@click.option("-e", type=int,
              help="sampling depth. have a look at stats_reads_per_sample.txt and pick a number")
def main(t, e, s):
    '''do diversity analysis'''
    run = DiversityAnalysis(taxon=s, sampling_depth=e, threads=t)
    run.run_core_diversity()
    print("core-diversity done")


if __name__ == '__main__':
    main()
