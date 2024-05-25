class Instance:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def get_load(self) -> int:
        '''
            Return the load of an instance which consists of
            the remaining number of queries to the blockchain
        '''
        raise NotImplementedError

    def handle_request(self, data: dict) -> dict:
        '''
            Handle a request to the instance
        '''
        raise NotImplementedError
