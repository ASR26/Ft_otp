# Descripción
Este proyecto consiste en hacer un programa que genere una contraseña temporal para leer los datos de un archivo que contiene una contraseña cifrada, similar al funcionamiento del <a href=""https://www.xataka.com/basics/google-authenticator-que-como-funciona-como-configurarlo">Google Authenticator</a>.

## Funcionamiento
Para usar el programa primero tendremos que crear una clave, que sera nuestra "contraseña", y la guardaremos en un archivo:
  ```
  echo -n "NEVER GONNA GIVE YOU UP NEVER GONNA LET YOU DOWN" > key.txt
  ```
Esta contraseña está en texto claro así que tendremos que pasarla a hexadecimal, para ello usaremos el comando `xxd`
  ```
  xxd -p -c256 key.txt > key.hex
  ```
La contraseña debe ser de al menos 64 caracteres, para comprobar cuantos caracteres tiene nuestra contraseña hexadecimal usaremos el siguiente comando:
  ```
  cat key.hex | wc -c
  ```
Esto nos devolverá el número de caracteres del archivo `key.hex`. En caso de que tenga menos de 64 caracteres tendremos que usar otra contraseña.

Ahora que tenemos una contraseña válida podemos empezar a ejecutar el programa. Primero guardaremos la contraseña hexadecimal en un archivo encriptado, para esto usaremos la flag `-g`
  ```
  ./ft_otp -g key.hex
  ```
Al ejecutarlo nos pedirá una contraseña de validación para poder acceder posteriormente al archivo. La contraseña deberá ser exactamente de 16 caracteres.
Tras esto se almacenará la contraseña encriptada en el archivo `ft_otp.key`, este sería el archivo al que tendríamos acceso en un caso real. 
Ahora queremos generar la contraseña temporal, para esto usaremos la flag `-k`:
  ```
  ./ft_otp -k ft_otp.key
  ```
Se nos pedirá la contraseña que dimos a la hora de encriptar el archivo y si la introducimos correctamente se nos devolverá una contraseña temporal de 6 dígitos que durará 30 segundos.

Otra forma de conseguir acceso a nuestra contraseña sería usando la flag '-qr':
  ```
  ./ft_otp -qr ft_otp.key
  ```
Este comando nos volverá a pedir la contraseña que usamos para encriptar el archivo y si la introducimos correctamente nos imprimirá un código qr que contiene la contraseña hexadecimal.
Este proyecto está basado en el proyecto ft_otp del repositorio 42malaga_bootcamp-ciberseguridad de <a href="https://github.com/15Galan/">15Galan</a>
