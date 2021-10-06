# Labelme2COCO

### 准备工作

所有图片文件放置在`images/total2019`文件夹下

所有`labelme`标签后的`json`文件放置在`labelme/total2019`文件夹下

在`labels.txt`中填写标签，如

```
__ignore__
screw
shim
```

### 数据集生成

首先运行`create_txt.py`，生成数个`txt`文件存储各类数据

而后运行`classify.py`，将数据按照各类`txt`文件进行划分

最后运行`labelme2coco.py`，生成`annotations`文件夹即为数据集

```bash
python ./labelme2coco.py --input_dir ./labelme/train2019 --output_dir ./annotations/train2019 --filename instances_train2019 --labels labels.txt

python ./labelme2coco.py --input_dir ./labelme/val2019 --output_dir ./annotations/val2019 --filename instances_val2019 --labels labels.txt

python ./labelme2coco.py --input_dir ./labelme/test2019 --output_dir ./annotations/test2019 --filename instances_test2019 --labels labels.txt
```



### 数据集生成2

在train2019文件夹中放置img和json

```
python labelme2coco2.py train2019 --output train2019.json
```

得到train2019.json

运行COCO_Image_Viewer.ipynb查看数据集情况

参考：https://github.com/Tony607/labelme2coco
