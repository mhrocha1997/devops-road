[WIP]
# DevOps Road

The main goal of this repository is to serve as a lab for learning DevOps Engineering, and a knowledge/experience compendium.


## Load Testing
### Fortio

```sh
kubectl run -it fortio -n apps --rm --image=fortio/fortio -- load -qps 6000 -t 120s -c 50 "http://app-ts-svc/exampe-k8s"
```
-qps: query per second
-c: simultaneous connections
