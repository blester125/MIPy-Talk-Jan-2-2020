# for i in 10 20 40 80 100 150 200 300 400 500 600 800 1000 2000 5000 10000; do
for i in 5000 10000; do
    for j in 2 4 10 20 30 50 70 100 150; do
        echo points=${i} dims=${j}
        python speed.py --points ${i} --dims ${j}
    done
done
