from datasette import hookimpl
import click
import sqlite3


@hookimpl
def register_commands(cli):
    @cli.command()
    @click.argument("files", type=click.Path(exists=True), nargs=-1)
    def verify(files):
        "Verify that SQLite files can be opened using Datasette"
        for file in files:
            conn = sqlite3.connect(str(file))
            try:
                conn.execute("select * from sqlite_master")
            except sqlite3.DatabaseError:
                raise click.ClickException("Invalid database: {}".format(file))
