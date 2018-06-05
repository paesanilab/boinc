import sys
sys.path.append("bin")

from boinc2docker_create_work import boinc2docker_create_work, read_create_work_args

from argparse import Namespace

args = Namespace(rsc_disk_bound=5000000000,rsc_memory_bound=6000000000)

wu = boinc2docker_create_work(
    image = "paesanilab/psi4:0.0.2",
    command = ['python', 'run_psi4.py', '--mol', 'O      -6.738646395e-00 -1.491617397e+00  -1.095035971e-10,H       8.141855337e-01  -1.866159045e+00 -2.044214632e-10,H       7.436878209e-02  -5.443285903e-01   4.259078718e-11'],
    appname = "boinc2docker",
    entrypoint=None,
    native_unzip=False,
    memory=None,
    create_work_args=read_create_work_args(args),
    verbose=True,
    force_reimport=False)
print wu
