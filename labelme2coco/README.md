# Labelme2COCO

## 准备工作

所有图片文件放置在`images/total2019`文件夹下

所有`labelme`标签后的`json`文件放置在`labelme/total2019`文件夹下

在`labels.txt`中填写标签，如

```
__ignore__
_background_
screw
shim
```

### 数据集生成

首先运行`create_txt.py`，生成数个`txt`文件存储各类数据

而后运行`classify.py`，将数据按照各类`txt`文件进行划分

最后运行`labelme2coco.py`，生成`annotations`文件夹即为数据集