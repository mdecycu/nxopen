在 CoppeliaSim 中執行 Python zmqRemoteAPI 程式之前要先確定:

1. Modules 下拉式功能表中的 Connectivity 中的 ZMQ remoteAPI server 是否已經 running

2. Python 系統是否已經安裝 pyzmq cbor 與 keyboard 模組, 若尚未安裝, 可以利用

pip install pyzmq cbor keyboard

將此三個模組配置到可攜 Python 系統中.