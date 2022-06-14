1,新建comme
    -创建基类（启动浏览器）
    -创建页面类（basepage 页面操作查找，点击，输入等）
2，创建configs
    -配置文件 （地址，浏览器参数等）
3，创建docs
    -文档，搭建框架记录
4，pageObjects
    -业务层 （业务流），+ element元素定位器
5, test_case
    -需要参数（建立参数文件）
6，utils
    -日志/文件 路径
7，test_cases
    -测试用例

业务流程：
1，建立基类层：
    1.1启动浏览器-- 创建启动浏览器类，为防止启动多个，使用单例模式，浏览器类继承单例
                  需要的地址、变量参数等，可以写入配置文件中 
    1.2创建操作方法-- 对浏览器的操作打开浏览器、打开网页、点击元素、输入内容等方法封装
                    一般对对元素方法添加显示等待
2，创建业务层：
    2.1登录页面-- 建立登录类,继承基类，
                 业务：调用基类封装的方法，启动浏览器，打开网址，编辑业务方法等
                 定位元素：yml文件，以业务类为名区分各页面的元素， 在基类，初始化方法中取得类名，获取元素
                 由于登录后是主页(操作的页面)可在登录后直接返回主页实例，（主页=登录后操作的页面，要创建该页面的类）
    注：定位元素：(属于表现层)
    2.2 页面层-- 添加商品和商品列表两个页面，建立页面类，
        2.2.1添加商品方法：
                 业务：从菜单栏到添加商品，操作添加商品，
                 逻辑：添加方法中，主页点击元素到添加商品，返回一个添加商品类实例，
                 添加商品类：创建添加方法，操作添加流程（调用基类，操作添加，数据使用yml）
        2.2.2商品列表方法：
                 业务：从添加完商品，点击菜单，到商品列表
                 逻辑：添加完数据后页面，点击菜单，点击列表，返回一个商品列表类实例
                 商品列表类：获取第一个数据，取数据名称
                 

3，测试用例层：
    3.1登录用例--创建测试类，建立测试方法
        3.1.1调试用例： 
                 内容：实例化登录的业务类，得到登录的实例，调用登录业务的方法，断言结果
                 逻辑：得到登录业务类的实例 ，调用登录的方法
                 数据：少数数据，可建立数据的py文件
        3.1.2参数化用例：
                 内容：实例化登录的业务类，得到登录的实例，调用登录业务的方法，断言结果，退出登录页面
                 逻辑：得到登录业务类的实例 ，调用登录的方法，断言，再通过登录方法实例调用基类封装的方法，退出登录。
                 数据：调用pytest.mark.parametrize("参数，参数",[(数据)，(数据)])，可从少数数据py文件中取数据
                 问题：会打开多个浏览器
                 解决：封装的浏览器方法继承单例模式
        3.1.3参数化用例--用例组合：
                 内容：正确用例，错误用例组合，登录系统，正确的用例需要退出，错误的不需要
                 逻辑：得到登录的实例，调用登录方法，断言，正确的用例在操作退出，失败的直接断言结束
                 数据：yml文件，-[]  -[] 
                 读取数据：utils工具层读取方法，导入到测试用例，将数据传入parametrize
                 传入数据：parametrize和用例函数参数一致，参数传入用例步骤中
        执行用例：pytest.main([]) , allure
    3.2添加商品页面用例：
        3.2.1 登录--添加：
                调用登录实例的对象，调用登录的方法，返回一个总页面类mainpage，
                用返回的总页面类mainpage对象调动 进入 添加商品页面的方法，返回一个对象（添加商品实例），
                再用该对象调用 添加商品类中的方法，
        3.2.2 --断言：
                 用调用 进入 添加商品的方法，返回的对象（添加商品实例）去进入菜单栏，
                 在用总页面类mainpage对象调用 进入 商品列表的方法，返回一个对象
                 再用该对象调用获得第一个商品的方法
                 断言----
        3.2.3 -- 提取登录到fixtrue
                   问题:
                        如果有两个业务，每个用例都需要调用登录，第一个执行后没有退出，
                         第二个执行时在登录就没有登录入口，
                    解决：
                        使用fixtrue，提取登录，返回对下对象，在用例中调用
4，处理浏览器：
    4.1 初始化 和 清理
        4.1.1 conftest.py:  测试用例层，创建该文件
                 需使用pytest.fixture(scope='作用域'，autouse='boole')
                 初始化数据等操作
                 yield
                 清理工作，如关闭浏览器
5，datas层：
    5.1 临时数据：用于调试或者非参数化使用
    5.2 测试用例：用于执行多数据或参数化
        
6，utils层：
    6.1 路径：都区路径
    6.2 读取yml：读取测试数据，用于传入测试用例中
    6.3 日志： 获取日志文件
    。。。
7，ENV层:
    7.1 配置文件： 地址，环境，时间参数等
8，outfiles层：
    8.1 报告
    8.2 错误截图
    8.3 错误日志

6.10号：
    两个插件：
        base_url:处理rul, 需要配置文件pytest.ini文件
        [pytets]:
         base_url = http://.......   不需要引号
。        
         pytest-assume:断言失败，继续run
            断言用 
            with pytest.assume:
                assert........
            注： 多个断言用多个 with pytest.assume

6.11号:
    品牌管理-查询
    先列好测试用例--分析需要增加一个页面--在mainpage封装的进入该页面的方法，返回值为该页面类的实例
    该页面类分两步：
        1，获得当前列表的商品的名字（需要find_elements的封装）
        2，输入框输入搜索的名字 --- 点击查询
    测试用例：
        1，调用fixtrue实现登录， 返回mainpage实例
        2，通过返回的basepage实例，直接调用该类下的可以进入品牌管理的方法
        3，然后调用获得列表商品方法，
        4，从该列表中随机获取一个名字
        5，该名字传入查询方法内，查询
        6，获得查询结果与 与随机得到的结果对比
        filter ===》 过滤
        assert filter(lambda x:预期结果 in x ,预期结果)==实际结果