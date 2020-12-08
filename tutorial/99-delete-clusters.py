# tutorial/99-Delete-clusters.py

from azureml.core import Workspace
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException

ws = Workspace.from_config() # This automatically looks for a directory .azureml


cpu_cluster_name = "cpu-cluster"
cpu_cluster = ComputeTarget(workspace=ws, name=cpu_cluster_name)
#ComputeTarget.delete(ws, cpu_cluster_name)

cpu_cluster.delete()