# Repository Guidelines

## 项目结构与模块组织
本仓库是 Mini Pupper 2 的 BSP（板级支持包）。仓库根目录包含 Raspberry Pi 安装与配置脚本，例如 `install.sh`、`setup.sh`、`prepare_dkms.sh`。硬件相关内容按功能分目录维护：`Audio/`、`Display/`、`FuelGauge/`、`IO_Configuration/`、`RPiCamera/`、`System/`、`rpi-i2s-audio/`。ESP32-S3 固件位于 `esp32/`，主程序源码在 `esp32/main/`，证书在 `esp32/server_certs/`，分区表为 `esp32/partitions_mini_pupper.csv`。Python 包位于 `Python_Module/MangDang/`，可 mock 的 API 与单元测试位于 `mock_api/`，可运行示例位于 `demos/`，图片和文档素材位于 `imgs/`。

## 构建、测试与开发命令
- `./install.sh`：在目标 Raspberry Pi 上安装 BSP 组件。
- `./setup.sh`：执行本地 BSP 配置步骤。
- `cd esp32 && source ~/esp/esp-idf/export.sh && idf.py build`：编译 ESP32-S3 固件。
- `cd esp32 && idf.py -p PORT flash`：将固件烧录到开发板，`PORT` 替换为实际串口。
- `cd mock_api && python3 -m pytest`：运行 mock API 单元测试。
- `python3 demos/python_api_getimu.py`：安装后运行单个硬件示例。

## 代码风格与命名约定
遵循各模块已有风格。ESP32 固件使用 C/C++、4 空格缩进、`mini_pupper_*` 文件命名，并优先使用 ESP-IDF API。Python 代码位于 `MangDang/` 包路径下，函数和变量使用 `snake_case`，模块名保持清晰具体。硬件常量应靠近实际使用模块。不要提交生成物，例如 `esp32/build/`、`sdkconfig`、本地编辑器配置等。

## 测试指南
Python API 行为变更应添加或更新 `mock_api/tests/` 下的测试，测试文件命名为 `test_*.py`。需要固定输出时，将期望结果放在 `mock_api/tests/expected_results/`。固件变更至少运行 `idf.py build`；涉及硬件行为时，在 PR 中说明已验证的设备或功能，例如舵机、IMU、显示屏、摄像头、电源检测或 OTA。

## 提交与 Pull Request 规范
近期提交信息多为简短描述，例如 `Added getCalibrate...`、`Moved testing script...`。提交应聚焦单一改动，必要时在标题中标明子系统。Pull Request 应目标分支为 `main`，说明改动内容，关联 issue 或讨论，列出测试结果；涉及界面、显示、烧录或硬件行为变化时，附上截图、日志或验证说明。

## 安全与配置提示
不要提交 Wi-Fi 密码、设备专属校准数据、私有证书或本地工具配置。`.codex`、`.vscode/`、`esp32/.vscode/`、生成固件、`esp32/build/` 和本地 `sdkconfig` 应保持在版本控制之外。
