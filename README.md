<div align="center">
    <img src="https://shf.com.co/_nuxt/img/1b7499c.png">
</div>

<h1 style="margin-top:10px;" align="center"> ➰
  <strong>  SHF TEST BACKEND </strong> ➿ 
</h1>

## 🐙 Goals

Dada una matriz de números enteros. Obtenga el elemento máximo en la matriz que produce la suma más pequeña al agregar todos los elementos que son diferentes de sí mismo.

Ejemplo 1:

Entrada:
numbers = [1,2,3,3,3,3,4,5,6,6]

Tanto 3 como 6 producen la suma más pequeña (24), pero 6 es mayor que 3. Por lo tanto, 6 es el elemento máximo que produce la suma más pequeña. `(6, 24)`

## 🐋 Sobre la solución

Inicialmente la función valida que la lista ingresada no sea vacía. Si lo es lanza un ValueError.
Seguidamente si la función solo tiene un valor, el resultado será ese mismo valor.

Luego, se recorre todos los valores del array, y se realiza la suma con los demás items de array diferentes a él.
Seguido, crear un array de procesados que guarda los números que ya han sido calculados, de modo que se ahorren iteraciones.
Finalmente se valida que la suma obtenida sea menor a la mímina actual, así como que el número que la produce, el máximo posible.

Cuando termina, retorna una tulpa, con el mayor número que produce la menor suma, y el resultado de la suma.
## 🐋 To get started

1. Install and configure Python 3.x.
2. Run the code within test with: `python3 src/smaller_addition_mock.py`.
3. Install nose2 for the test: `pip install nose2`.
4. Run the test with nose2: `python -m nose2`.
5. Enjoy.

### 🐣 Examples of use

Formato de la respuesta: `("Número del vector", "suma")`

**Input:** `[1,2,3,3,3,3,4,5,6,6]`.

**Output:** `(6, 24)`


**Input:** `[0,7,1,-10,2,-4,-1,3,-2,10,-2,-6,-9,9,1,10,3,-2,0,9,6,-5,10,-10,-2,-5,-5,7,-6,-10,2,2,-5,-3,8,0,3,4,-2,-9,-8,-1,-5,-9,-3,-10,7,-3,-9,4,0,1,0,-9,-8,6,-5,1,-6,-1,0,9,-10,-9,-4,5,5,5,-1,-9,1,-7,-5,-4,0,7,-7,0,6,7,8,-2,0,-6,-6,-2,2,5,0,-4,6,-6,10,-8,-5,-5,7,0,7,-9]`.


**Output:** `(7, -127)`


**Input:** `[4,10,0,-2,10,-3,-9,0,6,10,6,10,-5,10,7,-10,-9,1,-2,-8,-10,9,-4,-9,5,1,-4,-10,2,-8,1,10,9,-1,0,4,9,7,9,7,-1,5,3,0,2,-7,4,0,7,0,-5,-6,-1,0,4,10,-2,-6,0,9,5,-5,-10,0,-7,-3,-6,5,7,-4,0,4,5,9,-4,4,1,10,1,-4,4,-4,9,-10,-10,-5,9,-3,4,0,3,-4,-1,2,-1,-5,10,7,-2,-4]
`.


**Output:** `(10, -14)`
