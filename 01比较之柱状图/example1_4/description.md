# example1_4

用途：比较统计5名学生的BMI指数。公式：``bmi = weight/(height*height)``

> 分析：可视化的目的是``比较``，且考虑到可视化的数据较少，故采用柱状图进行绘制。

看完前3个example了以后，这个不是简单的一批吗？

## Step 1: 读表，取各列数据

学生姓名可作为柱状图x轴，在这一步取出。

## Step 2: 利用身高、体重数据算出BMI指数

作为y轴的BMI数据在这一步得出

## Step 3: 制图

> Note: 制图时对图像的设置，最好是留下注释，不然时间久了全忘了。

以本例为例，简要交代一些图表设置信息即可。

```python
"""作图

标题：BMI数据统计
x轴：学生姓名
y轴：bmi值计算结果，图例无
存储位置：./result/bmi.html
"""
resultFileName = "bmi.html"
bar = (Bar().set_global_opts(title_opts=opts.TitleOpts(title="BMI数据统计"))
       .add_xaxis(xaxis_data=name)
       .add_yaxis(y_axis=bmiList, series_name="")
       .render(path=os.path.join(resultPath, resultFileName))
       )
```