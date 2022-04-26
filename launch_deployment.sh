#!/bin/bash

runningNodes = ""
while [ "${runningNodes}" -l "4" ];do
	sleep 5
	runningNodes = "$(kubectl get pods -o name | wc -l)"
done

cd /local/repository/
kubectl apply -f cloudcooked.yaml
