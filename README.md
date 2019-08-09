# Kubernetes secret decoder
Inspired by https://github.com/ashleyschuett/kubernetes-secret-decode

A python script to decode the data fields of the output of `kubectl get secret <secret> -o yaml` (or `-o json`) so they are human readable (and copy-paste-able).

## Dependencies
Requires python >= 3.6 to run 

For development requires [pipenv](https://github.com/pypa/pipenv).

## Installation
Run 
```shell script
make install
```
This will install the package to your current pip.

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