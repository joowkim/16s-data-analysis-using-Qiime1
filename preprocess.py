import click

from qiime.automation.preprocess.run_preprocess import PreProcess

__author__ = "jkkim"


@click.command()
@click.option('-i', help='rawdata dir')
@click.option('-s', help="sample type is either bac or its.")
@click.option('-t', type=int, help="threads.")
def main(i, t, s):
    """do preprocess and otu clustering for community analysis."""
    run = PreProcess(rawdata_dir=i, taxon=s, threads=t)
    run.preprocess_run()


if __name__ == '__main__':
    main()
