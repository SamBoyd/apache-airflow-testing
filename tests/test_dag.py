from dags import S3ToBigQuery_Dag
from airflow.models import DAG


class TestDag(object):
    def test_should_be_a_valid_dag(self):
        test_dag = S3ToBigQuery_Dag.dag
        assert isinstance(test_dag, DAG)
