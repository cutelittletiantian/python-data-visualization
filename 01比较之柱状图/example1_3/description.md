# example1_3

该示例是``example1_1``的变式。这个问题中我们不再用赞粉比作为y轴数据，而是**直接拿粉丝数和点赞数同时作为y轴直观呈现**。

用途：分析并比较部分网红博主频道的粉丝互动情况。

> 分析：可视化的目的是``比较``，且考虑到可视化的数据较少，故采用柱状图进行绘制，且这个柱状图是``多y轴``的柱状图

## Step 1: 准备数据——网红博主的数据表

省略，与``example1_1``完全相同。

***

## Step 2: 将上述表格中的数据分列提取出来

省略，与``example1_1``完全相同。

***

## Step 3: 使用上述数据，绘制柱状图并保存

**指定x轴数据列表 -> 指定y轴数据列表及其图例 -> 指定保存路径和文件名（.html格式） -> 执行保存**

> 注意，这一次y轴有两个量，一个是粉丝数，一个是点赞量，分别添加

其中上述步骤中还要设置图表配置项，添加标题并且避免横坐标显示不完全（旋转一下横坐标label）

## 附1：做图——想一次到位还是分步组装？

本例子在绘图的时候有一段很长的构造和设置多y轴柱状图的代码。

```python
bar = (Bar()
       .set_global_opts(title_opts=opts.TitleOpts(title="博主粉丝数和点赞数"),
                        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)))
       .add_xaxis(xaxis_data=name)
       .add_yaxis(y_axis=fans, series_name="粉丝数")
       .add_yaxis(y_axis=likes, series_name="点赞数")
       )
```

其实这跟一步一步创建柱状图呈现的效果是一样的，即**上述代码与下述效果等同**。

```python
bar = Bar()
bar.set_global_opts(title_opts=opts.TitleOpts(title="博主粉丝数和点赞数"),
                        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)))
bar.add_xaxis(xaxis_data=name)
bar.add_yaxis(y_axis=fans, series_name="粉丝数")
bar.add_yaxis(y_axis=likes, series_name="点赞数")
```

> 第一种写法是``pyecharts``官方文档给出demo（传送门：https://gallery.pyecharts.org/ ）中惯用的代码写，其实就是把很多步设置一步到位了。
> 我个人觉得第一种写法更好，一句话创建一个图表，显得更聚集一些，省得创建个图表都要写好几行。
> 不过真正地到底哪种写法更好，仁者见仁智者见智的事情而已。

## 附2：全局选项设置——必须一步到位的地方！

本问题对柱状图进行调整的时候，做了**添加标题**和**倾斜横坐标文字**两件事，用到了**配置图表的全局选项设置**，即

```python
bar.set_global_opts(title_opts=opts.TitleOpts(title="博主粉丝数和点赞数"),
                    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)
                    )
```

> 不同于``附1``可以一步到位或者一步步慢慢来，这里若要同时让两个设置同时起效，必须在一个``set_global_opt``函数里同时配置相应参数，必须一步到位。

如果按照下述方式配置柱状图属性：

```python
bar.set_global_opts(title_opts=opts.TitleOpts(title="博主粉丝数和点赞数"))
bar.set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45))
```

可以试试，发现**原来标题的设置消失了，被横坐标label旋转的设置覆盖了**。

## 附3：图表属性选项（options）配置中的等效写法

以横坐标旋转45度为例，下面两种设置写法**效果等价**，均能正常绘图。

* 写法1

```python
bar.set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45))
```

* 写法2

```python
bar.set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate":45}))
```

> 喜欢哪种？还是一样这里仁者见仁智者见智。
> 目前我个人比较习惯写法1，虽然写起来稍微绕一点，但不管怎么说Pycharm中有代码提示引导，也还是挺香的。
> 
> ``pyecharts``官方对此也有相应说明，传送门：https://pyecharts.org/#/zh-cn/parameters
