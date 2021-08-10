一个简单的自动化测试脚本，该脚本主要有6个包，分别是：Doc,PageObject,Pub_method,TestCases,Report


Doc: 主要是用来存放元素的信息，以及一些appium的配置参数
PageObject: 封装了一些对元素的操作，如获得元素的信息，定位元素，页面动作（click，send_keys）等。
Pub_method: 这个包，主要是存放一些自己写的工具类，比如解析yaml文档的工具类等。
TestCase: 业务逻辑层，存放测试用例。
Report: 这个文件是用来存放allure测试报告的原始数据的，并且里面还包含一个picture包（初始状态也可能没有，当断言失败后，会自动生成），picture包是用来存放断言失败后的截图的。


执行顺序:
1.首先是执行最外层conftest.py中的内容，启动appium，创建好全局使用的driver对象
2.然后进入TestCase层，按照字母顺序，先执行A_Login中的case，在A_login package中，因为这里面也有conftest.py，所以先执行它
3.执行test case中的conf文件，会调用PageObject包中的内容，生成一个ElemActivity对象，然后将这个对象返回给test case使用
4.test case使用返回的ElemActivity对象，调用click_btn等方法。
5.ElemActivity类继承了FindElem类，能够使用FindElem中的find_element方法，然后ElemActivity中又增加了click_btn等操作内容


2021-08-06更新：
新增了一个pub_function的包，这个包中有一个pub_func的模块，里面只要是用来存放一些公共的功能模块，如"登录"功能。
调用方法：通过在test case中的conftest.py，调用这个功能模块。
