#!/bin/bash

echo ">>> importing submodules..."
git submodule init &&
git submodule update &&

echo ">>> Enforcing correct branchies"
echo ">>> Updating hdl" 
cd hdl 
git checkout hdl_2017_r1
cd ..

echo ">>> Updating linux"
cd linux
git checkout 2017_R1
cd ..

