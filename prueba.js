/* 🧠 PARTE TEÓRICA 

1. ¿Cuál es la diferencia entre 'let', 'const' y 'var' al declarar una variable en JavaScript?

La diferencia es que usando 'let' el valor puede reescribirse/cambiar, en cambio aplicando 'const' el valor es
fijo y no se altera.
Por último 'var' se puede re-declarar y mayormente se usa en funciones.

2. ¿Qué diferencias hay entre un objeto y un arreglo en JavaScript? ¿Cuándo conviene usar uno u otro?

Estos se pueden diferenciar en que los objetos tienen estructura con pares clave-valor. Usado mayormente
para entidades con propiedades, sin embargo los arrays son listas ordenadas, usados para 'colecciones' de datos.

Conviene usar un objeto cuando necesitamos describir una entidad, y cuando son varias usamos arreglos.

3. ¿Qué devuelve el método .filter() y cómo se diferencia de .map() al aplicarse sobre un array?

El método .filter() devuelve un nuevo array con los elementos que cumplen la condición.
Por otro lado .map() retorna un nuevo array con los resultados de aplicar una función a cada elemento.

4. ¿Qué método de arrays se utiliza para agregar un elemento al principio de un arreglo(array)?

Se utiliza el método .unShift(elemento).

💻 PARTE PRÁCTICA*/

const alumnos = [
  { nombre: "Ana", edad: 20, nota: 8 },
  { nombre: "Luis", edad: 17, nota: 5 },
  { nombre: "Carla", edad: 22, nota: 9 }
];

alumnos.forEach(alumnos => {
    if (alumnos.nota >= 6) {
      console.log("Aprobado");
    } else {
        console.log("Desaprobado");
    }
})

function obtenerPromedio(arr) {
    let suma = 0;
    arr.forEach(alumnos => suma += alumnos.nota);
    return suma / arr.length;
}

/* Ejercicio 2: map, filter, DOM */

// 1-
const mayores = alumnos.filter(alumnos => alumnos.edad >= 17);
console.log("Mayores de edad: ", mayores);

// 2-
const nombresMayús = alumnos.map(alumnos => alumnos.nombre.toUpperCase());
console.log("Nombres en mayúscula: ", nombresMayús);

// 3-
const contenedor = document.getElementById("lista");

alumnos.forEach(alumnos => {
    const li = document.createElement("li");
    li.textContent = alumnos.nombre;
    contenedor.append(li);
})

obtenerPromedio(arr);