from looker_connection import Connection
from typing import cast, Dict, List, Union
from looker_sdk import models, error
from json.decoder import JSONDecodeError
from looker_sdk.rtl.serialize import DeserializeError
import json

class LookQuery():
    def __init__(self, id: int, filters: Dict[str, str]) -> None:
        self.id = id
        self.sdk = self.generate_sdk()
        self.filters = self.generate_look_filters(filters)
        self.look_parameters = self.generate_look_parameters()
        self.request = self.generate_query_request()

    def generate_sdk(self):
        connection = Connection()
        return connection.sdk

    def generate_look_filters(self, filters):
        # print(f"type: {type(filters)} - {type(filters) is dict}")
        if (type(filters) is list):
            look_filters={}
            if (filters):
                for filter_name in filters:
                    look_filters[filter_name] = next(filters)
            return look_filters
        else:
            return filters
        
    def generate_look_parameters(self):
        """Returns the query associated with a given look id."""
        try:
            look = self.sdk.look(str(self.id))
        except error.SDKError as e:
            raise Exception(f"Processing: Look #{self.id} not generated due to {e}")
        else:
            query = look.query
        return query

    def generate_query_request(self):
        print(f"Processing: Generating Query for Look #{self.id}")
        query_request = models.WriteQuery(
            model=self.look_parameters.model,
            view=self.look_parameters.view,
            fields=self.look_parameters.fields,
            pivots=self.look_parameters.pivots,
            fill_fields=self.look_parameters.fill_fields,
            filters=self.filters,
            sorts=self.look_parameters.sorts,
            limit=self.look_parameters.limit,
            column_limit=self.look_parameters.column_limit,
            total=self.look_parameters.total,
            row_total=self.look_parameters.row_total,
            subtotals=self.look_parameters.subtotals,
            dynamic_fields=self.look_parameters.dynamic_fields,
            query_timezone=self.look_parameters.query_timezone,
        )
        print(f"Processing: Look #{self.id} - {query_request}")
        return query_request

    def execute(self):
        """Runs the specified query with the specified filters."""
        print(f"Processing: Extracting Data for Look #{self.id}")
        
        try:
            TJson = List[Dict[str, Union[str, int, float, bool, None]]]
            json_ = self.sdk.run_inline_query("json", self.request, cache=False)
            json_resp = cast(TJson, json.loads(json_))
            return json_resp
        except Exception as e:
            print(f"Processing: Failed to get look #{self.id} due to {e}")
        return json.loads("{}")
        