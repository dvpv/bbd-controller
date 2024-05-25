from services.instance import Instance
from utils.singleton import singleton


@singleton
class LoadBalancer:
    def __init__(self):
        self.instances: list[Instance] = []

    def get_instance(self) -> Instance:
        if not self.instances:
            return self.spawn_instance()
        return min(self.instances, key=lambda instance: instance.get_load())

    def spawn_instance(self) -> Instance:
        raise NotImplementedError
