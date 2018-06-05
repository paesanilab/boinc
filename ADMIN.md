# Documentation for Admins

The BOINC clients download the `psi4` container on their machine, this container is defined in:

https://github.com/paesanilab/docker-images/blob/master/psi4/Dockerfile

Then we can execute any file which is included in that contaier.
For example now we have a single file that computes Energy and Forces for a Monomer, it gets as a command line argument `--mol` the geometry for the molecule.

https://github.com/paesanilab/docker-images/blob/master/psi4/run_psi4.py

## Test the container outside of BOINC

If we have `docker` installed on a machine we can test this locally.

Download the container with `docker pull paesanilab/psi4`

First we can test the `run_psi4.py` file which is included in the container with:

    docker run -it paesanilab/psi4 python run_psi4.py --mol "O      -6.738646395e-02  -1.491617397e+00  -1.095035971e-10,H       8.141855337e-01  -1.866159045e+00  -2.044214632e-10,H       7.436878209e-02  -5.443285903e-01   4.259078718e-11"
    
We are passing the molecule geometry **inside a quoted string** as a command line argument, newlines should be replaced by commas.

Later if we want to customize the script, we can then mount it inside the container with `-v` as:

    docker run -v $(pwd)/run_psi4.py:/run_psi4.py  -it paesanilab/psi4 python run_psi4.py --mol "O      -6.738646395e-02  -1.491617397e+00  -1.095035971e-10,H       8.141855337e-01  -1.866159045e+00  -2.044214632e-10,H       7.436878209e-02  -5.443285903e-01   4.259078718e-11"
    
Then you can submit a pull request to https://github.com/paesanilab/docker-images with your improved version.

## Submit BOINC jobs

* SSH to the machine on Jetstream that runs the BOINC server
* execute `boinc_connect_server.sh` to get a terminal inside the Docker container which is actually running the BOINC server
