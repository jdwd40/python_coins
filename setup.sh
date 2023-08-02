#!/bin/bash

# root directory
mkdir  coins
cd  coins

# create subdirectories
mkdir -p myapp/controllers
mkdir -p myapp/models
mkdir -p myapp/utils

# go back to the root directory
cd ..

# create the tests directory
mkdir tests
cd tests

# create subdirectories
mkdir -p unit
mkdir -p integration

# go back to the root directory
cd ..

# create additional directories
mkdir logs
mkdir docs
