from datasette.cli import cli
from click.testing import CliRunner
import pytest
import sqlite3


@pytest.mark.parametrize("is_valid", (True, False))
def test_verify(is_valid, tmpdir):
    runner = CliRunner()
    db_path = str(tmpdir / "db.db")
    if is_valid:
        sqlite3.connect(db_path).execute("create table foo (id integer primary key)")
    else:
        open(db_path, "w").write("bad file")
    result = runner.invoke(cli, ["verify", db_path])
    if is_valid:
        assert result.exit_code == 0
    else:
        assert result.exit_code == 1
        assert result.output.strip() == ("Error: Invalid database: {}".format(db_path))
