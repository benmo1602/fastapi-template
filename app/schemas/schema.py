# -*- coding: utf-8 -*-
#
# 通用schema
# Author: kunyu.cao
# Email: kunyu.cao@hlifetech.com
# Created Time: 2023-11-13
from typing import Any
from pydantic import BaseModel, Field


class MessageResp(BaseModel):
    message: str = Field(..., title='提示信息', description='提示信息')


class VersionResp(BaseModel):
    version: str = Field(..., title='版本信息', description='版本信息')


class StatusCodeResp(BaseModel):
    code: int = Field(..., title='异常状态值', description='异常状态值')
    message: str = Field(..., title='异常状态值说明', description='异常状态值说明')
    data: Any = Field(None, title='异常状态值数据', description='异常状态值数据')
