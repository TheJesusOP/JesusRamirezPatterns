# Object Pool 

(Piscina de objetos) es un patrón de diseño para el desarrollo de software. El patrón object pool es un patrón de diseño de software que usa un conjunto de objetos inicializados preparados para su uso. Esto es más efectivo normalmente que creando y destruyento los objetos bajo demanda. Un cliente del pool le pedirá un objeto para realizar las operaciones con el objeto. Cuando el cliente termina retorna el objeto al pool para que lo retenga hasta que vuelva a necesitar usarse. Es decir, los objetos no se crean (salvo la primera vez) ni se destruyen, simplemente se van reciclando.

Este patrón de diseño suele mejorar significativamente el rendimiento en situaciones donde el coste de iniciar una instancia de clase es alto y cuando el número de instancias simultáneas no es muy alto.
