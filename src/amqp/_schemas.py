import json


class UpdateStageQuery:

    def __init__(self,
                 user_id: int,
                 new_stage: str
                 ):
        self.user_id = user_id
        self.new_stage = new_stage

    @property
    def data(self) -> dict:
        return {'user_id': self.user_id, 'new_stage': self.new_stage}

    def to_json(self):
        return json.dumps(self.data, ensure_ascii=True)

    @classmethod
    def from_json(cls, json_data: str) -> 'UpdateStageQuery':
        data = json.loads(json_data)
        return cls(**data)
