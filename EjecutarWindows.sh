#!/bin/bash

move Entradas\Compras.inf salidaCompras
move Entradas\ListRepZ.txt ListRepZ

cd salidaCompras
python convertidorCompras.py
cd ..

cd ListRepZ
python exe.py
cd ..

del salidaCompras\Compras.inf
del ListRepZ\ListRepZ.txt

move salidaCompras\salidaCompras.txt Salidas
move ListRepZ\salidaListRepZ.txt Salidas
