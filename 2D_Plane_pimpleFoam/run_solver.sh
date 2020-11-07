#!/bin/bash

foamCleanTutorials
blockMesh | tee log.blockMesh

rm -rf 0
cp -r 0_org 0

decomposePar
mpirun -np 4 renumberMesh -overwrite -parallel 
mpirun -np 4 pimpleFoam -parallel | tee log.solver
