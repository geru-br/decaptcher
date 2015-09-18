from __future__ import print_function
import click
import logging
import sys



@click.group()
@click.option('-u', '--username', envvar='DECAPTCHER_USERNAME', default=None)
@click.option('-p', '--password', envvar='DECAPTCHER_PASSWORD', default=None)
@click.option('-d', '--debug', envvar='DEGUG', default=None)
@click.option('-s', '--silent', default=None)
def cli(username=None, password=None, debug=None, silent=None):
    if not silent:

        root = logging.getLogger()

        if debug:
            root.setLevel(logging.DEBUG)
        else:
            root.setLevel(logging.INFO)

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        ch.setFormatter(formatter)
        root.addHandler(ch)


@cli.command(name='post')
@click.argument('path')
@click.pass_context
def api_post(context, path):
    import api

    response = api.post(
        path,
        username=context.parent.params.get('username'),
        password=context.parent.params.get('password')
    )
    print(response.data)


@cli.command(name='balance')
@click.pass_context
def api_balance(context):
    import api

    response = api.balance(
        username=context.parent.params.get('username'),
        password=context.parent.params.get('password')
    )
    print(response.content)


@cli.command(name='picturebad')
@click.argument('majorid')
@click.argument('minorid')
@click.pass_context
def api_picturebad(context, majorid, minorid):
    import api

    response = api.picturebad(
        username=context.parent.params.get('username'),
        password=context.parent.params.get('password'),
        majorid=majorid,
        minorid=minorid
    )

    print('Status Code: {} || Response content: {}'.format(response.status_code, response.content))

if __name__ == '__main__':
    cli()
