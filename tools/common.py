from typing import Any, Generator, Optional
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin import Tool


def validate_parameters(tool: Tool, params: dict[str, Any], required_fields: list[str]) -> Generator[Optional[ToolInvokeMessage], None, bool]:
    """
    通用参数验证方法
    :param tool: Tool实例
    :param params: 参数字典
    :param required_fields: 必需字段列表
    :return: 验证是否通过
    """
    for field in required_fields:
        if not params.get(field):
            yield tool.create_text_message(f"Please provide {field}")
            return False
    return True
