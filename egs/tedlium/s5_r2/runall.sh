#!/bin/bash

for i in `seq 17 17`
do
  ./run.sh --stage $i >& ./output/28_APRIL_17/out.$i
  echo $i
done;

./results.sh > ./output/28_APRIL_17/performance.out
echo "Finished calculating results"
