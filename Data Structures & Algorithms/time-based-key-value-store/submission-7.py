class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        timestamp_str = str(timestamp)
        if key in self.data:
            current_data = self.data[key] or {}
            current_data[timestamp_str] = value
        else:
            self.data[key] = {timestamp_str: value}

    def get(self, key: str, timestamp: int) -> str:
        timestamp_str = str(timestamp)
        if not key in self.data:
            return ""
        d = self.data.get(key, {})
        if timestamp_str in d:
            return d.get(timestamp_str)
        keys_array = [int(x) for x in d.keys() if int(x) < timestamp]
        return d.get(str(keys_array[-1]), "") if keys_array else ""
