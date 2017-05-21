#!/bin/bash

for i in `seq 0 17`
do
  ./run.sh --stage $i >& ./output/results/out.$i
  echo $i
done;

./results.sh > ./output/results/performance.out
echo "Finished calculating results"
