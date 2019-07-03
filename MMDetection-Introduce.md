#MMDetection-Introduce

##Introduce
以open-mmlab发布的mmdetection 为基础，分为train、inference以及annotation三个部分。

##Major features
- ###mmdetection-train
   #####此模块主要介绍使用mmdetection框架如何训练，以cascade_rcnn为例。
   #####1、数据集转换
   #####2、configs/***.py 修改
   #####3、训练时，命令行参数解析
- ###mmdetection-inference
  #####此模块主要提供及解析模型接口，使用高级api进行inference
  #####*demo.py*: 包含对单张图片、多张图片以及视频流进行检测。
- ###mmdetection-annotation
  #####此模块包含对整体框架、backbone、one-stage detector等代码的解读 。
