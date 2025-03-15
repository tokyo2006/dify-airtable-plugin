from collections.abc import Generator
from typing import Any
import json
from pyairtable import Api
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class AirtableToolInsert(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        baseId = tool_parameters["baseId"]
        airtable_token = self.runtime.credentials["airtable_token"]
        tableId = tool_parameters["tableId"]
        api = Api(airtable_token)
        table = api.table(baseId, tableId)
        record = tool_parameters["record"]
        if not record:
            yield self.create_text_message("Please provide a record")
        if not baseId:
            yield self.create_text_message("Please provide a baseId")
        if not tableId:
            yield self.create_text_message("Please provide a tableId")
        if isinstance(record, str):
            try:
                record = json.loads(record)
            except json.JSONDecodeError:
                yield self.create_text_message("The record is invalid JSON string")
        try:
            table.create(record)
            yield self.create_text_message("Success")
        except Exception as e:
            yield self.create_text_message(f"Error：{e}")
