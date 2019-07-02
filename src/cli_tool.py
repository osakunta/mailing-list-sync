import click
from src.googleintegration.directory import groups as google_groups
from src.googleintegration.sheets import spreadsheets
from src.synchronizer import synchronize_group


@click.group()
def cli():
    pass


@cli.command()
def groups():
    group_list = google_groups.list_all()

    if not group_list:
        click.echo('No groups in the domain.')
    else:
        for group in group_list:
            click.echo(u'{0} ({1})'.format(group['name'], group['email']))


@cli.command()
@click.argument('sheet', required=True)
@click.argument('cells', required=True)
@click.argument('group', required=True)
def sync(sheet, cells, group):
    cell_values = spreadsheets.get(sheet, cells)
    synchronize_group(group, cell_values)
