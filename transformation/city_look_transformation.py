from json_converter.json_mapper import JsonMapper
import json

class CityTransformation():
    def __init__(self, raw_message):
        self.raw_message = self.pre_processed(raw_message)
        self.specification = {
            '$on': 'result',
            'location': ["country"],
            'city': ["city"],
            'total_sales': ["count"]
        }
        self.processed_message = self.transform()

    """
    Original:
    [{'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Zhongli District', 'all_sessions.count': 3255}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Minxiong Township', 'all_sessions.count': 656}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Neipu Township', 'all_sessions.count': 469}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Mountain View', 'all_sessions.count': 393}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Palo Alto', 'all_sessions.count': 207}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Toufen City', 'all_sessions.count': 195}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Dacun Township', 'all_sessions.count': 181}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Shinjuku', 'all_sessions.count': 173}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Longtan District', 'all_sessions.count': 140}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Singapore', 'all_sessions.count': 136}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Sunnyvale', 'all_sessions.count': 106}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Zhudong Township', 'all_sessions.count': 105}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Shanghai', 'all_sessions.count': 103}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Taoyuan District', 'all_sessions.count': 93}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Santa Clara', 'all_sessions.count': 77}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Ningbo', 'all_sessions.count': 53}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'San Jose', 'all_sessions.count': 52}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Hukou Township', 'all_sessions.count': 48}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Hong Kong', 'all_sessions.count': 30}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'New York', 'all_sessions.count': 20}]
    """
    def pre_processed(self, raw_message):
        if (not raw_message):
            return
        
        pre_processed_message = f"{{'result': {raw_message} }}"
        pre_processed_message = pre_processed_message\
                .replace("all_sessions.", "")\
                .replace("'", '"')\
                .replace('"s', "'s") # handle case where the text has apostrophe (e.g 's)
        
        # import re
        # pattern = r'"((\w{1})\s)'
        # replace = r"'$1"
        # pre_processed_message = re.sub(pattern, replace, pre_processed_message)

        return pre_processed_message

    """
    Raw: 
    {
        "result": [{'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Zhongli District', 'all_sessions.count': 3255}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Minxiong Township', 'all_sessions.count': 656}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Neipu Township', 'all_sessions.count': 469}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Mountain View', 'all_sessions.count': 393}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Palo Alto', 'all_sessions.count': 207}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Toufen City', 'all_sessions.count': 195}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Dacun Township', 'all_sessions.count': 181}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Shinjuku', 'all_sessions.count': 173}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Longtan District', 'all_sessions.count': 140}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Singapore', 'all_sessions.count': 136}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Sunnyvale', 'all_sessions.count': 106}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Zhudong Township', 'all_sessions.count': 105}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Shanghai', 'all_sessions.count': 103}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Taoyuan District', 'all_sessions.count': 93}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Santa Clara', 'all_sessions.count': 77}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Ningbo', 'all_sessions.count': 53}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'San Jose', 'all_sessions.count': 52}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Hukou Township', 'all_sessions.count': 48}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'Hong Kong', 'all_sessions.count': 30}, {'all_sessions.country': 'Taiwan', 'all_sessions.city': 'New York', 'all_sessions.count': 20}]
    }

    Processed:
    {
        "result": [{"location": "Taiwan", "city": "Zhongli District", "total_sales": 3255}]
    }
    """
    def transform(self):
        print(f"{self.raw_message}")
        print(f"{self.specification}")
        try:
            json_obj = json.loads(self.raw_message)
            # return json.dumps(JsonMapper(json_obj).map(self.specification))
            mapped_obj = JsonMapper(json_obj).map(self.specification)
            return mapped_obj
        except Exception as e:
            print(f"Processing: unable to parse raw message due to {e}")
            # return json.dumps({ 'result': []})
            return []