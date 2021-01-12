from domain.example import Example
from repository.mysql import BaseRepository
from repository.mysql.example import ExampleModel


class ExampleRepository(BaseRepository):

    def model_to_entity(self, model):
        params = {
            "example_id": model.example_id,
            "name": model.name,
            "is_active": model.is_active
        }
        return Example(**params)

    def save(self, example: Example):
        example_model = ExampleModel()
        example_model.name = example.name
        example_model.is_active = example.is_active
        self.__create__(example_model)
        self.__commit__()

    def find_by_id(self, example_id):
        model = self.session.query(ExampleModel).filter(ExampleModel.example_id == example_id).one()
        return self.model_to_entity(model)


if __name__ == '__main__':
    new_example = Example(**{"name": "李四"})

    er = ExampleRepository()
    er.save(new_example)
    example = er.find_by_id('1')
