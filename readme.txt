一个简单的自动化测试脚本，该脚本主要有6个包，分别是：ActivityObject, Base, Doc, Pub_method, TestCase，Report

ActivityObject: 这个包，将对元素的操作，重新进行了封装；我们在TestCase中使用的Click_btn等方法，都是通过conftest.py，调用的这个包中重新封装的方法。
Base: 这个包，主要存放了selenium或者appium的一些工具类，方便调用。
Pub_method: 这个包，主要是存放一些自己写的工具类，比如解析yaml文档的工具类，重新封装的定位元素的工具类。
Doc: 主要是用来存放元素的信息，当然也可以存放一些其他的配置文件
TestCase: 存放测试用例的包。
Report: 这个文件是用来存放allure测试报告的原始数据的，并且里面还包含一个picture包（初始状态也可能没有，当断言失败后，会自动生成），picture包是用来存放断言失败后的截图的。


执行顺序:
1.首先是执行最外层conftest.py中的内容，启动appium，创建好全局使用的driver对象
2.然后进入TestCase层，按照字母顺序，先执行A_Login中的case，在A_login package中，因为这里面也有conftest.py，所以先执行它
3.执行testcase中的conf文件，会调用ActivityObject包中的内容，生成一个ElemActivity对象，然后将这个对象返回给testcase使用
4.testcase使用返回的ElemActivity对象，调用click_btn等方法。
5.ElemActivity继承了Pub_method中的findElem类，并且调用了read_yaml中的类，所以在ElemActivity中，可以读取元素信息，并对元素进行操作
6.当testcase中调用了click_btn方法时，先是调用read_yaml中的方法查找该元素
7.然后再用父类中重新封装的click方法。


