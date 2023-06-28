import looker_sdk

class Connection():
    def __init__(self) -> None:
        self.sdk = looker_sdk.init40("looker.ini")