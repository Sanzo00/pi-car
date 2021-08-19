# pi-car

- [x] 远程控制小车
- [ ] 自动避障



## 2021/8/19 远程控制小车

> 搭建过程

- 将[server.py](https://github.com/Sanzo00/pi-car/blob/master/server.py)、[control.html](https://github.com/Sanzo00/pi-car/blob/master/control.html)部署到服务器。
- 树莓派端运行[car.py](https://github.com/Sanzo00/pi-car/blob/master/car.py)。
- 用户访问[control.html](https://github.com/Sanzo00/pi-car/blob/master/control.html)对小车进行远程控制。



> 注意事项

在运行前，你需要将[car.py: L64](https://github.com/Sanzo00/pi-car/blob/82efdb26c4d6dbb4e48b8a65cdb08b3b4e218dd8/control.html#L64)和[control.html: L28](https://github.com/Sanzo00/pi-car/blob/82efdb26c4d6dbb4e48b8a65cdb08b3b4e218dd8/car.py#L28)修改为你的服务器地址。



> 效果展示

![](https://img.sanzo.top/img/pi/remote-control-car.gif)





