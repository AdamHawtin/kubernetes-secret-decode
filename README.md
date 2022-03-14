# Kubernetes secret decoder [![Build Status](https://travis-ci.org/AdamHawtin/kubernetes-secret-decode.svg?branch=master)](https://travis-ci.org/AdamHawtin/kubernetes-secret-decode)
Inspired by https://github.com/ashleyschuett/kubernetes-secret-decode

A python script to decode the data fields of the output of `kubectl get secret <secret> -o yaml` (or `-o json`) so they are human readable (and copy-paste-able).

## Dependencies
Requires python >= 3.10 to run 

For development dependencies are managed with [pipenv](https://github.com/pypa/pipenv). The dependencies are then frozen in [requirements.txt](requirements.txt) for installation using ` pipenv lock --requirements > requirements.txt`.

## Installation
To download the latest release and install through your current Pip run:
```shell script
curl -L https://github.com/AdamHawtin/kubernetes-secret-decode/archive/v0.1.0.tar.gz --output ./kubernetes-secret-decode-0.1.0.tar.gz
tar xzf kubernetes-secret-decode-0.1.0.tar.gz -C . && pushd kubernetes-secret-decode-0.1.0
make install
popd
```

Or you can clone the repo then run:
```shell script
make install
```

## Usage
Pipe the output of the kubectl get secret command to `ksd` like so
```shell script
kubectl get secret very-secret-things -o yaml | ksd
```

Also work with JSON output:
```shell script
kubectl get secret very-secret-things -o json | ksd
```

Can also be called on a file like 
```shell script
ksd very-secret-things.json
```
