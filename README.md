# pi-car

- [x] 远程控制小车
- [x] PWM变速
- [x] 超声波自动避障

![](https://img.sanzo.top/img/pi/car.jpg)

## 远程控制小车

> 搭建过程

- 将[server.py](https://github.com/Sanzo00/pi-car/blob/master/server.py)、[control.html](https://github.com/Sanzo00/pi-car/blob/master/control.html)部署到服务器。
- 树莓派端运行[car.py](https://github.com/Sanzo00/pi-car/blob/master/car.py)。
- 用户访问[control.html](https://github.com/Sanzo00/pi-car/blob/master/control.html)对小车进行远程控制。



> 注意事项

在运行前，你需要将[car.py: L64](https://github.com/Sanzo00/pi-car/blob/82efdb26c4d6dbb4e48b8a65cdb08b3b4e218dd8/control.html#L64)和[control.html: L28](https://github.com/Sanzo00/pi-car/blob/82efdb26c4d6dbb4e48b8a65cdb08b3b4e218dd8/car.py#L28)修改为你的服务器地址。



> 效果展示

https://user-images.githubusercontent.com/36565277/130321858-450953d6-38b8-404e-91dc-64b7e3ac592c.mp4





## PWM变速

小车在低电压情况下跑的比较慢，因此增加变速的功能，可以随时调整小车的速度。

![](https://img.sanzo.top/img/pi/pwm-speed-control.png)





## 超声波自动避障

这里使用超声波测距模块（HC-SR04）实现距离检测，在此基础上实现一个简单的自动避障逻辑。



> 效果展示


https://user-images.githubusercontent.com/36565277/130325569-bc4e0d2f-b80e-4e83-a0ac-8cc5889755b7.mp4




## 代码设计

- 通信采用websocket，control和car向server发送数据包，server根据数据包的`device`区分发送方，然后交给对应的事件处理函数。
- [control.html](https://github.com/Sanzo00/pi-car/blob/master/control.html)是用户与小车的交互页面，每个按钮对应一个消息，消息先发往server端，由server端对消息进行处理，如果是控制小车的命令，需要将消息转发给小车。
- [car.py](https://github.com/Sanzo00/pi-car/blob/master/car.py)是小车运行的主程序，通过接收server端发送的消息执行对应的指令，有时也需要将数据返回给server端。
- [server.py](https://github.com/Sanzo00/pi-car/blob/master/server.py)是服务端的主程序，主要用于用户与小车的消息同步。
- 在实现自动避障时，需要注意以下几点：
  - 超声波测距有时不太准确，特别是当小车距离障碍物很近的时候，距离往往会固定为一个很大的值，我的解决方案是，记录1.5秒前的距离，如果当前距离和1秒前的距离很近，可以判断为卡在障碍物无法前进，这是需要主动后退进行躲避。
  - [control.html](https://github.com/Sanzo00/pi-car/blob/master/control.html)界面同时包括远程控制和自动避障，我的自动避障逻辑是一个死循环检测，因此当用户切到自动避障后，将无法使用其他按钮进行控制，我的解决方案是使用线程执行自动避障，同时维护一个状态变量，当用户按下`stop`时，自动避障线程退出。

我的python代码比较烂，感觉异步处理还有多用户同时访问实现的不太优雅，有时间还需要重构下，欢迎各位大佬提issue和pr。

如果你喜欢这个项目，请赏个⭐！
