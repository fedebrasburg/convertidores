#!/bin/zsh

mv Entradas/Compras.inf salidaCompras
mv Entradas/ListRepZ.txt ListRepZ

cd salidaCompras
python tNuevo.py
cd ..

cd ListRepZ
python exe.py
cd ..

rm salidaCompras/Compras.inf
rm ListRepZ/ListRepZ.txt

mv salidaCompras/salidaCompras.txt Salidas
mv ListRepZ/salidaListRepZ.txt Salidas
