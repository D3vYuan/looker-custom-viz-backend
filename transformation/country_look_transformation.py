from json_converter.json_mapper import JsonMapper
import json

class CountryTransformation():
    def __init__(self, raw_message):
        self.raw_message = self.pre_processed(raw_message)
        self.specification = {
            '$on': 'result',
            'location': ["country"],
            'total_sales': ["count"]
        }
        self.processed_message = self.transform()

    """
    Original:
    [{'all_sessions.country': 'United States', 'all_sessions.count': 14089813}, {'all_sessions.country': 'Canada', 'all_sessions.count': 789981}, {'all_sessions.country': 'India', 'all_sessions.count': 685718}, {'all_sessions.country': 'United Kingdom', 'all_sessions.count': 551330}, {'all_sessions.country': 'Japan', 'all_sessions.count': 347840}, {'all_sessions.country': 'Germany', 'all_sessions.count': 321820}, {'all_sessions.country': 'Taiwan', 'all_sessions.count': 277761}, {'all_sessions.country': 'Australia', 'all_sessions.count': 257812}, {'all_sessions.country': 'France', 'all_sessions.count': 255745}, {'all_sessions.country': 'Netherlands', 'all_sessions.count': 172602}]
    """
    def pre_processed(self, raw_message):
        if (not raw_message):
            return
        
        pre_processed_message = f"{{'result': {raw_message} }}"
        pre_processed_message = pre_processed_message\
                .replace("all_sessions.", "")\
                .replace("'", '"')
        return pre_processed_message

    """
    Raw: 
    {
        "result": [{"country": "United States", "count": 14089813}, {"country": "Canada", "count": 789981}, {"country": "India", "count": 685718}, {"country": "United Kingdom", "count": 551330}, {"country": "Japan", "count": 347840}, {"country": "Germany", "count": 321820}, {"country": "Taiwan", "count": 277761}, {"country": "Australia", "count": 257812}, {"country": "France", "count": 255745}, {"country": "Netherlands", "count": 172602}]
    }

    Processed:
    {
        "result": [{"location": "United States", "total_sales": 14089813}]
    }
    """
    def transform(self):
        try:
            print(f"{self.raw_message}")
            json_obj = json.loads(self.raw_message)
            # return json.dumps(JsonMapper(json_obj).map(self.specification))
            mapped_obj = JsonMapper(json_obj).map(self.specification)
            print(type(mapped_obj))
            return mapped_obj
        except Exception as e:
            print(f"Processing: unable to parse raw message due to {e}")
            return []