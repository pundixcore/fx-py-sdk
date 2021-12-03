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
Windows: venv\Scripts\activate

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

```
./gen-proto.sh
```
Windows: wsl ./gen-proto.sh


### 5.跑个Demo~
```
python grpc_client_test.py

```

### 6. 如何增加新的业务模块proto文件

1. 把业务模块的proto文件放在 `protos` 下面
2. 如 `dex` 
3. 重新运行 `./gen-proto.sh` 脚本生成python代码文件

结构如下

```
├── protos
│   ├── cosmos
│   ├── dex
│   └── ibc
```

### 已知问题

1. 不知道为啥 gogoproto proto文件生成出来的python文件一定要放在根目录... ？求解决
    会生成, 这些目录文件
    ```
    ├──── confio
    │   ├── proofs_pb2.py
    │   └── proofs_pb2_grpc.py
    ├── cosmos_proto
    │   ├── cosmos_pb2.py
    │   └── cosmos_pb2_grpc.py
    ├── gen-proto.sh
    ├── gogoproto
    │   ├── __pycache__
    │   ├── gogo_pb2.py
    │   └── gogo_pb2_grpc.py
    ├── google
    │   ├── api
        ── tendermint
    │   ├── abci
    │   ├── crypto
    │   ├── libs
    │   ├── p2p
    │   ├── types
    │   └── version
    ```