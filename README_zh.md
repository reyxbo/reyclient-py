[English](README.md)

# reyclient

**reyclient** 是一个用于调用第三方 API 的 Python 方法集成包。

提供阿里、百度等第三方平台 API 的统一调用方法，可用于集成文本翻译、大语言模型 AI 内容生成、手机验证码发送等常用第三方 API 服务。

通过模块化的 API 方法封装，简化第三方服务接口的调用和集成。

## 特性

* 提供第三方 API 的统一调用方法
* 支持阿里 API
* 支持百度 API
* 提供文本翻译 API
* 提供大语言模型 AI 内容生成 API
* 提供手机验证码发送 API
* 提供 HTTP 请求及响应数据的统一处理方法
* 支持 API 请求及响应数据写入数据库
* 模块化设计，可按需调用不同平台的 API
* 提供统一的方法导出接口

---

## 安装

要求 **Python 3.12 或更高版本**。

```bash
pip install reyclient
```

---

# 文件夹

reyclient 按第三方平台划分为多个文件夹，各文件夹负责对应平台的 API 方法封装。

## `rali` — Ali website methods folder

**阿里 API 方法目录。**

提供阿里相关第三方 API 的调用方法。

主要包括：

* 手机验证码发送 API
* 大语言模型 AI 内容生成 API
* 其它阿里平台 API

---

## `rbaidu` — Baidu website methods folder

**百度 API 方法目录。**

提供百度相关第三方 API 的调用方法。

主要包括：

* 文本翻译 API
* 其它百度平台 API

---

# 模块

reyclient 按功能划分为多个模块，各模块负责不同的 API 调用及公共功能。

## `rall` — All import methods

**统一导出模块。**

提供 reyclient 所有模块方法和对象的便捷导出，可以通过该模块集中导入框架提供的功能，减少从多个模块分别导入的代码。

---

## `rbase` — Base methods

**基础方法模块。**

提供其它模块共用的基础方法和公共依赖。

主要包括：

* HTTP 请求相关的全局标准方法
* HTTP 响应数据相关的全局标准方法
* HTTP 请求数据写入数据库
* HTTP 响应数据写入数据库
* 其它 API 调用相关的基础方法

---

# 模块概览

| 模块       | 功能                |
| -------- | ----------------- |
| `rall`   | 所有方法的统一导出         |
| `rbase`  | HTTP 请求、响应及公共基础方法 |
| `rali`   | 阿里 API 方法         |
| `rbaidu` | 百度 API 方法         |

---

# 依赖

主要依赖：

* `alibabacloud_dypnsapi20170525`
* `alibabacloud_tea_openapi>=0.4.3`
* `reydb`
* `reykit`

---

# 项目信息

| 项目         | 信息                                                            |
| ---------- | ------------------------------------------------------------- |
| 名称         | `reyclient`                                                   |
| 版本         | `1.0.47`                                                      |
| Python     | `>=3.12`                                                      |
| 作者         | `Rey`                                                         |
| 邮箱         | `reyxbo@163.com`                                              |
| Homepage   | [REYXBO](https://www.reyxbo.com/release/python/reyclient)     |
| Repository | [reyclient-py](https://github.com/reyxbo/reyclient-py.git)    |

## 关键词

`rey` · `reyxbo` · `client` · `request` · `API` · `ali` · `baidu` · `AI`
