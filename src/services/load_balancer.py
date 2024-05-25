import boto3
from services.instance import Instance
from utils.singleton import singleton


@singleton
class LoadBalancer:
    def __init__(self,
                 aws_access_key_id: str,
                 aws_secret_access_key: str,
                 region_name: str,
                 image_id: str,
                 security_group_ids: list[str],
                 key_name: str,
                 subnet_id: str,
                 instance_type: str = 't2.micro'):
        self.instances: list[Instance] = []
        self.image_id: str = image_id
        self.security_group_ids: list[str] = security_group_ids
        self.key_name: str = key_name
        self.subnet_id: str = subnet_id
        self.instance_type: str = instance_type
        self.__aws = boto3.client(
            'ec2',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )

    def get_instance(self) -> Instance:
        if not self.instances:
            return self.spawn_instance()
        # TODO: don't forget to check instance status
        return min(self.instances, key=lambda instance: instance.get_load())

    def spawn_instance(self) -> Instance:
        response = self.__aws.run_instances(
            ImageId=self.image_id,
            InstanceType=self.instance_type,
            MinCount=1,
            MaxCount=1,
            SecurityGroupIds=self.security_group_ids,
            KeyName=self.key_name,
            SubnetId=self.subnet_id
        )
        instances = response['Instances']
        instance = instances[0]
        public_ip = instance.get('PublicIpAddress')
        return Instance(endpoint=public_ip, instance=instance)
