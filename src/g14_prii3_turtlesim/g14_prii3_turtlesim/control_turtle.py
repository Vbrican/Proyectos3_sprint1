import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from std_srvs.srv import Empty
from g14_prii3_interfaces.srv import ControlDibujo

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.pen = self.create_client(SetPen, '/turtle1/set_pen')
        self.reset = self.create_client(Empty, '/reset')
        while not self.pen.wait_for_service(timeout_sec=1.0):
            pass
        while not self.reset.wait_for_service(timeout_sec=1.0):
            pass
        self.create_service(ControlDibujo, '/control_dibujo', self.servicio)

        self.pose = None
        self.pausado = False
        self.segmento = 0
        self.estado = 'mover'
        self.espera = 0

        # x_inicio, y_inicio, x_final, y_final
        self.segmentos = [
            (3.0, 8.2, 3.0, 2.8),      # 1
            (8.0, 8.2, 5.5, 5.2),      # 4 diagonal
            (5.5, 5.2, 8.8, 5.2),      # 4 horizontal
            (8.0, 8.2, 8.0, 2.8)       # 4 vertical
        ]

        self.lapiz(True)
        self.create_timer(0.05, self.control)

    def pose_callback(self, msg):
        self.pose = msg

    def lapiz(self, apagado):
        req = SetPen.Request()
        req.r = 255
        req.g = 255
        req.b = 255
        req.width = 3
        req.off = 1 if apagado else 0
        self.pen.call_async(req)

    def parar(self):
        self.pub.publish(Twist())

    def normalizar(self, angulo):
        return math.atan2(math.sin(angulo), math.cos(angulo))

    def servicio(self, request, response):
        comando = request.comando.lower().strip()

        if comando == 'detener':
            self.pausado = True
            self.parar()
            response.success = True
            response.mensaje = 'Dibujo detenido'

        elif comando == 'reanudar':
            self.pausado = False
            response.success = True
            response.mensaje = 'Dibujo reanudado'

        elif comando == 'reiniciar':
            self.pausado = True
            self.parar()
            futuro = self.reset.call_async(Empty.Request())
            futuro.add_done_callback(self.reinicio_terminado)
            response.success = True
            response.mensaje = 'Reiniciando dibujo'

        else:
            response.success = False
            response.mensaje = 'Comando no valido'

        return response

    def reinicio_terminado(self, future):
        try:
            future.result()
            self.segmento = 0
            self.estado = 'mover'
            self.espera = 3
            self.pose = None
            self.pausado = False
            self.lapiz(True)
        except Exception as error:
            self.get_logger().error(str(error))

    def mover_hacia(self, x, y, velocidad=0.8, giro=2.5):
        dx = x - self.pose.x
        dy = y - self.pose.y
        distancia = math.hypot(dx, dy)
        objetivo = math.atan2(dy, dx)
        error = self.normalizar(objetivo - self.pose.theta)

        msg = Twist()
        msg.linear.x = 0.0 if abs(error) > 0.35 else (
            0.3 if distancia < 0.6 else velocidad
        )
        msg.angular.z = giro * error
        self.pub.publish(msg)
        return distancia

    def orientar(self, x1, y1, x2, y2):
        objetivo = math.atan2(y2 - y1, x2 - x1)
        error = self.normalizar(objetivo - self.pose.theta)

        if abs(error) < 0.03:
            self.parar()
            return True

        msg = Twist()
        msg.angular.z = 2.5 * error
        self.pub.publish(msg)
        return False

    def control(self):
        if self.pausado or self.pose is None:
            self.parar()
            return

        if self.espera > 0:
            self.espera -= 1
            return

        if self.segmento >= len(self.segmentos):
            self.parar()
            self.lapiz(True)
            return

        x1, y1, x2, y2 = self.segmentos[self.segmento]

        if self.estado == 'mover':
            if self.mover_hacia(x1, y1, 0.8, 2.5) < 0.20:
                self.parar()
                self.estado = 'orientar'

        elif self.estado == 'orientar':
            if self.orientar(x1, y1, x2, y2):
                self.lapiz(False)
                self.espera = 3
                self.estado = 'dibujar'

        elif self.estado == 'dibujar':
            if self.mover_hacia(x2, y2, 0.75, 3.0) < 0.08:
                self.parar()
                self.lapiz(True)
                self.segmento += 1
                self.espera = 3
                self.estado = 'mover'

def main(args=None):
    rclpy.init(args=args)
    nodo = TurtleController()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()