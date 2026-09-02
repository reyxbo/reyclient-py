[中文](README_zh.md)

# reyclient

**reyclient** is a Python method integration package for calling third-party APIs.

It provides unified methods for calling third-party platform APIs such as Alibaba and Baidu, and can be used to integrate common third-party API services such as text translation, large language model AI content generation, and SMS verification code sending.

Through modular API method encapsulation, it simplifies the calling and integration of third-party services.

## Features

* Provides unified methods for calling third-party APIs
* Supports Alibaba APIs
* Supports Baidu APIs
* Provides text translation APIs
* Provides large language model AI content generation APIs
* Provides SMS verification code sending APIs
* Provides unified handling methods for HTTP request and response data
* Supports writing API request and response data to the database
* Modular design, allowing different platform APIs to be called as needed
* Provides unified method export interfaces

---

## Installation

Requires **Python 3.12 or higher**.

```bash
pip install reyclient
```

---

# Folders

reyclient is organized into multiple folders by third-party platform, with each folder responsible for encapsulating the API methods of the corresponding platform.

## `rali` — Alibaba API methods directory

**Alibaba API methods directory.**

Provides methods for calling third-party APIs related to Alibaba.

Mainly includes:

* SMS verification code sending API
* Large language model AI content generation API
* Other Alibaba platform APIs

---

## `rbaidu` — Baidu API methods directory

**Baidu API methods directory.**

Provides methods for calling third-party APIs related to Baidu.

Mainly includes:

* Text translation API
* Other Baidu platform APIs

---

# Modules

reyclient is divided into multiple modules by functionality, with each module responsible for different API calls and common functions.

## `rall` — All import methods

**Unified export module.**

Provides convenient exports of all reyclient module methods and objects. It allows the functionality provided by the package to be imported centrally, reducing the need to import from multiple modules separately.

---

## `rbase` — Base methods

**Base methods module.**

Provides common base methods and shared dependencies used by other modules.

Mainly includes:

* Global standard methods for HTTP requests
* Global standard methods for HTTP response data
* Writing HTTP request data to the database
* Writing HTTP response data to the database
* Other base methods related to API calls

---

# Module Overview

| Module   | Function                                        |
| -------- | ----------------------------------------------- |
| `rall`   | Unified export of all methods                   |
| `rbase`  | HTTP request, response, and common base methods |
| `rali`   | Alibaba API methods                             |
| `rbaidu` | Baidu API methods                               |

---

# Dependencies

Main dependencies:

* `alibabacloud_dypnsapi20170525`
* `alibabacloud_tea_openapi>=0.4.3`
* `reydb`
* `reykit`

---

# Project Information

| Project    | Information                                                   |
| ---------- | ------------------------------------------------------------- |
| Name       | `reyclient`                                                   |
| Version    | `1.0.47`                                                      |
| Python     | `>=3.12`                                                      |
| Author     | `Rey`                                                         |
| Email      | `reyxbo@163.com`                                              |
| Homepage   | [REYXBO](https://www.reyxbo.com/release/python/reyclient)     |
| Repository | [reyclient-py](https://github.com/reyxbo/reyclient-py.git)    |

## Keywords

`rey` · `reyxbo` · `client` · `request` · `API` · `ali` · `baidu` · `AI`
