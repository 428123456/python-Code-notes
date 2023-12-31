from pyecharts import options as opts
from pyecharts.charts import Bar

# 准备数据
x_data = ['一月', '二月', '三月', '四月', '五月']
y_data = [10, 20, 15, 25, 30]

# 创建柱状图
bar_chart = Bar()
bar_chart.add_xaxis(x_data)
bar_chart.add_yaxis("销售额", y_data)

# 配置图表
bar_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="月度销售额柱状图"),
    xaxis_opts=opts.AxisOpts(name="月份"),
    yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
)

# 渲染图表
bar_chart.render("bar_chart.html")

'''
说明：

Bar()：创建一个柱状图对象。
add_xaxis 和 add_yaxis：分别用于添加横轴和纵轴的数据。
set_global_opts：配置全局选项，包括标题、坐标轴的名称等。
生成的图表将保存为 "bar_chart.html" 文件，你可以在浏览器中打开该文件，查看生成的柱状图。
'''