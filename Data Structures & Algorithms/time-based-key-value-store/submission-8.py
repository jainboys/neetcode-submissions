class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            current_data = self.data[key] or {}
            current_data[timestamp] = value
        else:
            self.data[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        timestamp = timestamp
        if not key in self.data:
            return ""
        d = self.data.get(key, {})
        if timestamp in d:
            return d.get(timestamp)
        keys_array = [x for x in d.keys() if x < timestamp]
        return d.get(keys_array[-1], "") if keys_array else ""
