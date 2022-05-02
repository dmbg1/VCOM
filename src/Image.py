class Image():
  # filename name of the image's file
  # type = list containing traffic sign types of the image
  # classifications = list containing traffic sign type predictions
    def __init__(self, filename: str, type: str) -> None:
        self.filename = filename
        self.types = [type]
        self.classifications = []

    def add_classification(self, classification: str) -> None:
        self.classifications.append(classification)

    def add_type(self, type: str) -> None:
        self.types.append(type)

    def get_types(self) -> list:
        return self.types

    def get_classifications(self) -> list:
        return self.classifications

    def get_filename(self) -> str:
      return self.filename