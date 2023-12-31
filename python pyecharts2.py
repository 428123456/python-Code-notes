from pyecharts import options as opts
from pyecharts.charts import Bar
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

# 准备数据
x_data = ['一月', '二月', '三月', '四月', '五月']
y_data = [10, 20, 15, 25, 30]

# 创建柱状图
bar_chart = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 初始主题为亮色系
bar_chart = Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))  # 设置初始主题为暗色系

bar_chart.add_xaxis(x_data)
bar_chart.add_yaxis("销售额", y_data)

# 配置图表
bar_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="月度销售额柱状图"),
    xaxis_opts=opts.AxisOpts(name="月份"),
    yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
)

# 渲染图表
bar_chart.render("themed_bar_chart.html")