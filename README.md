# KDAutoApiTest_be

# 前后端分离的接口自动化测试框架，这个是后端

### 文件目录介绍
#### model——中存放接口测试的模型，目前完成了REST和SOAP的模型，每个模型可以单独拿出来使用。

##### REST接口模型——传递json数据，返回检查json数据
##### SOAP接口模型——传递XML数据，返回检查将xml转为json后，进行检查