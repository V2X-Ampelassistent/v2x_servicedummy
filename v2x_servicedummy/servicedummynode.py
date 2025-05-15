from v2x_services.srv import TrafficLightInfo, WarningInfoDisplay

import rclpy
from rclpy.node import Node

class ServiceDummyNode(Node):

    def __init__(self):
        super().__init__('ServiceDummyNode')
        self.srv = self.create_service(TrafficLightInfo, 'TrafficLightInfo', self.TrafficLightInfoCallback)
        self.srv2 = self.create_service(WarningInfoDisplay, 'WarningInfoDisplay', self.WarningInfoDisplayCallback)

    def TrafficLightInfoCallback(self, request, response):
        # To trigger callback, run '''ros2 service call /TrafficLightInfo v2x_services/srv/TrafficLightInfo'''
        self.get_logger().info('received Request')

        return response
    
    def WarningInfoDisplayCallback(self, request, response):
        # To trigger callback, run '''ros2 service call /WarningInfoDisplay v2x_services/srv/WarningInfoDisplay "{type: 1, infomessage: 'This is a Message.'}"'''
        self.get_logger().info(str(request))
        response.ignored = True
        return response

def main(args=None):
    print('Hi from v2x_servicedummy.')
    
    rclpy.init(args=args)
    TrafficLightInfo_dummy = ServiceDummyNode()

    rclpy.spin(TrafficLightInfo_dummy)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
