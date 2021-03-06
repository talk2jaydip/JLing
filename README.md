## JLing  
JLing是一个可以工作在Linux的自定义中文语音对话机器人  
(csdn ：[https://blog.csdn.net/weixin_40490238](https://blog.csdn.net/weixin_40490238))  
(github: [https://github.com/Kingzhoudk/JLing](https://github.com/Kingzhoudk/JLing))

## 目录
* [特点](#特点)
* [运行环境](#运行环境)
* [工作模式](#工作模式)
* [Demo](#Demo)
* [配置](#配置)
* [运行](#运行)
* [联系](#联系)

## 特点  
JLing的将所有的功能都模块化：

* 语音识别、语音合成、语音唤醒都做到了高度模块化，方便继承和开发第三方的插件。
* 对话机器人的支持，可以使用自己的语料库进行问答，也可以接入第三方的图灵机器人和Emotibot。
* 本地离线唤醒机器人，采用了Snowboy进行离线语音唤醒支持，唤醒词条可自行选择。
* 中文支持，集成百度、科大讯飞、阿里等国内这几家中文语音识别和语音合成比较优秀的技术。
* 智能家居，暂时利用Agora提供的SDK开发了P2P的视频监控和通信。

## 运行环境  
* Linux操作系统（测试PC的Ubuntu18、Raspberry Pi）
* USB麦克风
* 音响
* 摄像头(可选)

## 工作模式
* JLing通过用户唤醒。  
* 将用户的中文语音经过（阿里、百度、科大讯飞）STT引擎进行ASR识别形成文本。  
* 本先在自己本地的语料库进行匹配，若匹配成功，则返回对应的指令去交给模块处理，模块处理成功之后的返回结果再交给TTS引擎合成语音，最后播放给用户。  
* 若本地的语料库检索不中，就提交给图灵机器人或Emotibot，以提高机器人对话的灵活度。

## Demo
github: https://github.com/Kingzhoudk/JLing

## 配置
```powershell
pip3 install aiml
pip3 install webrtcvad
pip3 install baidu-aip
pip3 install logging
pip3 install configparser
sudo apt-get install python3-pyaudio
sudo apt-get install python3-serial
sudo apt-get install swig
sudo apt-get install libatlas-base-dev
[树莓派还需安装]：
sudo apt-get install sox
sudo apt-get install alsa-utils
sudo apt-get install pulseaudio
```

## 运行

```powershell
./JLing.sh
```

## 联系
* JLing只作个人学习研究，如因使用JLing造成任何损失，本人概不负责。
* 邮箱：zhoudk@ccitrobot.com

