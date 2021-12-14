## 如何使用

### 1. 克隆代码到本地

```shell
git clone https://github.com/falcons-x/fx-py-sdk

cd fx-pay-sdk
```


### 2. 构建当前项目的Python虚拟环境

1. 创建虚拟目录 venv

Mac 电脑示例

```
python3 -m venv venv
```

2. 激活虚拟环境

```
source ./venv/bin/activate
```
> Windows: venv\Scripts\activate

### 3. 安装项目依赖

```
pip install -r requirements.txt
```

> 如果网速不行,可以使用腾讯云的pip镜像加速
```
pip install -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple
```

### 4. 编译Proto文件为python文件

> 如果gen-proto.sh没有执行权限,使用 `chmo +x gen-proto.sh`

```shell
cd fx_py_sdk
./scripts/gen-proto.sh
```

>Windows: wsl ./gen-proto.sh

> 编译的py文件默认输出到codec模块, 并且已添加__init__.py

> 编译出的python文件需要更改导入包的路径，如下：
>
```shell
cd fx_py_sdk
./scripts/imports.sh
```

### 5.跑个Demo~

```
python grpc_client_test.py
```

### 6. 安装sdk

> 从其他开发仓库导入sdk包，需要安装sdk, 默认安装到本地python版本的site-packages

```shell
 python setup.py install
```


### 7.使用sdk

> 在开发仓库执行easy_install, 加载到venv环境

```shell
easy_install  --find-links="$Install_PATH/site-packages" fx_py_sdk

from fx_py_sdk.grpc_client import GRPCClient

```
