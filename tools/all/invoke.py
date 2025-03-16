from collections.abc import Generator
from typing import Any
import json
from pyairtable import Api
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from tools.common import validate_parameters

class AirtableToolAll(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        required_fields = ["baseId", "tableId"]
        if not validate_parameters(self, tool_parameters, required_fields):
            return
        baseId = tool_parameters["baseId"]
        tableId = tool_parameters["tableId"]
        api = Api(self.runtime.credentials['airtable_token'])
        table = api.table(baseId, tableId)
        try:
            records = table.all()
            result = json.dumps(records, default=str)
            yield self.create_text_message(result)
        except Exception as e:
            yield self.create_text_message(f"Error：{e}")
