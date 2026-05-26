# ESP32 目录功能说明

## 概览

本目录是 Mini Pupper 2 的 ESP32-S3 固件工程，负责机器人底层控制、传感器数据读取、主机通信、命令调试和 OTA 升级。工程使用 ESP-IDF 构建，应用名为 `mini_pupper_app`。

## 配置与分区

- `sdkconfig.defaults`：ESP-IDF 默认配置，例如目标配置、FreeRTOS 配置、编译优化和分区表设置。
- `partitions_mini_pupper.csv`：自定义 flash 分区表，包含 NVS、OTA 数据、两个 OTA app 分区和 FAT storage 分区。
- `server_certs/`：HTTPS OTA 使用的证书文件。

## 核心源码模块

主要源码位于 `main/`：

- `mini_pupper_app.cpp`：应用初始化、控制台启动和全局状态管理。
- `mini_pupper_servos.cpp`：舵机通信、位置控制、扭矩控制、校准和状态读取。
- `mini_pupper_imu.cpp`：IMU 数据读取和错误统计。
- `mini_pupper_power.cpp`：电源与电池状态读取。
- `mini_pupper_host.cpp`：与 Raspberry Pi 或上位机通信。
- `mini_pupper_protocol.h`：通信帧解析、校验和错误率统计。
- `mini_pupper_cmd.cpp`：注册控制台调试命令，例如舵机扫描、校准、状态读取和 OTA。
- `mini_pupper_ota.cpp`：HTTPS OTA 固件升级逻辑。

## 常用命令

```sh
source ~/esp/esp-idf/export.sh
idf.py build
idf.py -p PORT flash
idf.py monitor
```

`PORT` 需要替换为实际串口，例如 `/dev/ttyUSB0`。
