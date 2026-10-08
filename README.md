# Proyectos3_sprint1

# Proyecto RII 3 - Sprint 1 - Grupo 14

Este repositorio contiene el proyecto realizado para el Sprint 1 de la asignatura **Proyecto RII 3: Robots Inteligentes**.

El programa utiliza **ROS 2 Humble** y **Turtlesim** para controlar de forma automática una tortuga que dibuja el número del grupo, en este caso el número **14**.

También se han implementado tres servicios ROS 2 que permiten:

- Detener el dibujo.
- Reanudar el dibujo.
- Reiniciar el dibujo desde el principio.

Todo el sistema se puede ejecutar mediante un único archivo `launch`.

---

# 1. Sistema operativo necesario

El proyecto ha sido desarrollado y probado utilizando:

```text
Ubuntu 22.04
ROS 2 Humble
Python 3
```

ROS 2 Humble está diseñado para Ubuntu 22.04.

---

# 2. Instalación de ROS 2 Humble

Si ROS 2 Humble ya está instalado, se puede pasar directamente al apartado **3. Descargar el proyecto**.

## 2.1 Actualizar Ubuntu

Abrir una terminal y ejecutar:

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 2.2 Configurar el idioma del sistema

Comprobar que el sistema utiliza UTF-8:

```bash
locale
```

Si fuese necesario, instalar y configurar los locales:

```bash
sudo apt update
sudo apt install locales -y
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

---

## 2.3 Activar los repositorios necesarios

Instalar:

```bash
sudo apt install software-properties-common -y
```

Activar el repositorio `universe`:

```bash
sudo add-apt-repository universe
```

---

## 2.4 Añadir el repositorio de ROS 2

Instalar `curl`:

```bash
sudo apt install curl -y
```

Añadir la clave de ROS:

```bash
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
-o /usr/share/keyrings/ros-archive-keyring.gpg
```

Añadir el repositorio:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | \
sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

Actualizar:

```bash
sudo apt update
```

---

## 2.5 Instalar ROS 2 Humble

Instalar ROS 2 Humble Desktop:

```bash
sudo apt install ros-humble-desktop -y
```

Instalar también las herramientas de desarrollo:

```bash
sudo apt install ros-dev-tools -y
```

---

## 2.6 Comprobar que ROS 2 funciona

Cargar ROS 2:

```bash
source /opt/ros/humble/setup.bash
```

Comprobar la versión instalada:

```bash
echo $ROS_DISTRO
```

Debe aparecer:

```text
humble
```

También se puede comprobar:

```bash
printenv | grep ROS
```

---

# 3. Instalar Turtlesim y Colcon

Instalar Turtlesim:

```bash
sudo apt install ros-humble-turtlesim -y
```

Instalar Colcon:

```bash
sudo apt install python3-colcon-common-extensions -y
```

Comprobar que Turtlesim está instalado:

```bash
source /opt/ros/humble/setup.bash
ros2 pkg executables turtlesim
```

Deben aparecer los ejecutables de Turtlesim.

---

# 4. Descargar el proyecto

El proyecto se encuentra alojado en GitHub.

Abrir una terminal y situarse en la carpeta en la que se quiera descargar.

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Ejemplo:

```bash
git clone https://github.com/USUARIO/Proyectos3_sprint1.git
```

Entrar en la carpeta:

```bash
cd Proyectos3_sprint1
```

La estructura principal del proyecto será similar a:

```text
Proyectos3_sprint1/
│
├── README.md
│
└── src/
    └── g14_prii3_turtlesim/
        │
        ├── g14_prii3_turtlesim/
        │   ├── __init__.py
        │   └── control_turtle.py
        │
        ├── launch/
        │   └── turtlesim.launch.py
        │
        ├── package.xml
        ├── setup.py
        └── setup.cfg
```

---

# 5. Compilar el proyecto

Una vez dentro de:

```text
Proyectos3_sprint1
```

cargar ROS 2:

```bash
source /opt/ros/humble/setup.bash
```

Compilar el workspace:

```bash
colcon build
```

Si todo se ha compilado correctamente aparecerá un mensaje similar a:

```text
Summary: 1 package finished
```

Después de compilar se crearán automáticamente las carpetas:

```text
build/
install/
log/
```

---

# 6. Cargar el workspace

Después de compilar hay que cargar el workspace:

```bash
source install/setup.bash
```

Este comando debe ejecutarse cada vez que se abra una terminal nueva desde la que se quiera trabajar con este proyecto.

---

# 7. Ejecutar el proyecto

El proyecto se ejecuta desde un único archivo `launch`.

Desde la carpeta:

```text
Proyectos3_sprint1
```

ejecutar:

```bash
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch g14_prii3_turtlesim turtlesim.launch.py
```

El archivo `launch` iniciará automáticamente:

```text
Turtlesim
+
Nodo de control de la tortuga
```

La tortuga comenzará automáticamente a dibujar el número:

```text
14
```

No es necesario ejecutar `turtlesim_node` ni `control_turtle.py` manualmente.

---

# 8. Evitar comunicación con otros ordenadores ROS 2

Si se está trabajando en una red donde existen otros ordenadores utilizando ROS 2, se recomienda activar:

```bash
export ROS_LOCALHOST_ONLY=1
```

Por tanto, una ejecución completa sería:

```bash
cd Proyectos3_sprint1
source /opt/ros/humble/setup.bash
export ROS_LOCALHOST_ONLY=1
source install/setup.bash
ros2 launch g14_prii3_turtlesim turtlesim.launch.py
```

El proyecto quedará limitado al ordenador local.

---

# 9. Controlar el dibujo desde una segunda terminal

Mientras Turtlesim está funcionando, mantener abierta la primera terminal.

Abrir una **segunda terminal**.

Entrar otra vez en el proyecto:

```bash
cd Proyectos3_sprint1
```

Cargar ROS 2:

```bash
source /opt/ros/humble/setup.bash
```

Si se está utilizando `ROS_LOCALHOST_ONLY`, ejecutar también:

```bash
export ROS_LOCALHOST_ONLY=1
```

Cargar el workspace:

```bash
source install/setup.bash
```

---

# 10. Comprobar los servicios disponibles

Ejecutar:

```bash
ros2 service list
```

Entre los servicios disponibles deben aparecer:

```text
/detener
/reanudar
/reiniciar
```

También se pueden comprobar únicamente estos tres mediante:

```bash
ros2 service list | grep -E "detener|reanudar|reiniciar"
```

El resultado esperado es:

```text
/detener
/reanudar
/reiniciar
```

---

# 11. Detener el dibujo

Mientras la tortuga está dibujando, ejecutar desde la segunda terminal:

```bash
ros2 service call /detener std_srvs/srv/Trigger "{}"
```

La tortuga se detendrá en la posición en la que se encuentre.

La respuesta será similar a:

```text
success=True
message='Dibujo detenido'
```

---

# 12. Reanudar el dibujo

Para continuar desde el punto en el que se detuvo:

```bash
ros2 service call /reanudar std_srvs/srv/Trigger "{}"
```

La tortuga continuará realizando el dibujo.

La respuesta será similar a:

```text
success=True
message='Dibujo reanudado'
```

---

# 13. Reiniciar el dibujo

Para borrar el dibujo actual y volver a empezar desde el principio:

```bash
ros2 service call /reiniciar std_srvs/srv/Trigger "{}"
```

Turtlesim se reiniciará y la tortuga volverá a comenzar el dibujo del número 14.

La respuesta será similar a:

```text
success=True
message='Dibujo reiniciado'
```

---

# 14. Funcionamiento del programa

El nodo principal se encuentra en:

```text
g14_prii3_turtlesim/control_turtle.py
```

La tortuga obtiene continuamente su posición mediante:

```text
/turtle1/pose
```

Las órdenes de movimiento se publican mediante:

```text
/turtle1/cmd_vel
```

utilizando mensajes:

```text
geometry_msgs/msg/Twist
```

El lápiz de la tortuga se controla mediante:

```text
/turtle1/set_pen
```

El programa utiliza diferentes segmentos para representar el número 14.

El funcionamiento general es:

```text
Inicio
  ↓
Levantar lápiz
  ↓
Moverse al comienzo del segmento
  ↓
Orientarse
  ↓
Bajar lápiz
  ↓
Dibujar segmento
  ↓
Levantar lápiz
  ↓
Pasar al siguiente segmento
  ↓
Repetir hasta terminar el número 14
```

Los movimientos entre trazos se realizan con el lápiz levantado para evitar dibujar líneas no deseadas.

---

# 15. Ejecución rápida

Una vez instalado ROS 2 y compilado el proyecto, únicamente se necesitan dos terminales.

## Terminal 1 - Ejecutar Turtlesim

```bash
cd Proyectos3_sprint1
source /opt/ros/humble/setup.bash
export ROS_LOCALHOST_ONLY=1
source install/setup.bash
ros2 launch g14_prii3_turtlesim turtlesim.launch.py
```

## Terminal 2 - Controlar el dibujo

```bash
cd Proyectos3_sprint1
source /opt/ros/humble/setup.bash
export ROS_LOCALHOST_ONLY=1
source install/setup.bash
```

Detener:

```bash
ros2 service call /detener std_srvs/srv/Trigger "{}"
```

Reanudar:

```bash
ros2 service call /reanudar std_srvs/srv/Trigger "{}"
```

Reiniciar:

```bash
ros2 service call /reiniciar std_srvs/srv/Trigger "{}"
```

---

# 16. Resumen de comandos

Compilar:

```bash

colcon build

```

Ejecutar:

```bash
ros2 launch g14_prii3_turtlesim turtlesim.launch.py
```

Detener:

```bash
ros2 service call /detener std_srvs/srv/Trigger "{}"
```

Reanudar:

```bash
ros2 service call /reanudar std_srvs/srv/Trigger "{}"
```

Reiniciar:

```bash
ros2 service call /reiniciar std_srvs/srv/Trigger "{}"
```

---

# Grupo

**Grupo 14 - Proyecto RII 3**
