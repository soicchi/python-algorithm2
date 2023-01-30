from typing import NewType


Json = NewType("Json", str)


class ValidateJson:
    def __init__(self) -> None:
        self.stack = []

    def is_valid(self, json: Json) -> bool:
        patterns = { "(": ")", "[": "]", "{": "}" }
        for s in json:
            if s in patterns:
                self.stack.append(patterns[s])
                continue

            if s in patterns.values():
                if not self.stack or s != self.stack.pop():
                    return False

        if self.stack:
            return False

        return True

if __name__ == "__main__":
    valid_format = "{'key1': 'value1', 'key2': (1,2,3)}"
    invalid_format = "{'key1': ['value1', 'key2': [1,2,3], 'key3': (1,2,3)}"
    validate_json = ValidateJson()
    print(validate_json.is_valid(valid_format))
    print(validate_json.is_valid(invalid_format))
