import boto3
import pytest
from click.testing import CliRunner
from fscmds.fstree import cli as fstree_cli
from moto import mock_s3

aws_env = {
    "AWS_ACCESS_KEY_ID": "key-id",
    "AWS_SECRET_ACCESS_KEY": "secret",
    "AWS_DEFAULT_REGION": "region",
}


@pytest.fixture(scope="session")
def fstree_run():
    runner = CliRunner(env=aws_env)

    def _run(fspath, level=1):
        res = runner.invoke(fstree_cli, [f"-L{level}", fspath])
        return res

    return _run


@pytest.fixture(scope="session")
def s3():
    name = "bucket"
    with mock_s3():
        client = boto3.client("s3", region_name=aws_env["AWS_DEFAULT_REGION"])
        client.create_bucket(
            Bucket=name,
            CreateBucketConfiguration={
                "LocationConstraint": aws_env["AWS_DEFAULT_REGION"]
            },
        )
    yield client


def test_fstree_s3(fstree_run, s3):
    res = fstree_run("s3://bucket/")
    assert res.exit_code == 0, res.output
