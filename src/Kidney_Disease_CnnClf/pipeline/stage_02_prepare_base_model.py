from Kidney_Disease_CnnClf import logger
from Kidney_Disease_CnnClf.config import ConfigurationManager
from Kidney_Disease_CnnClf.components.prepare_base_model import PrepareBaseModel

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
