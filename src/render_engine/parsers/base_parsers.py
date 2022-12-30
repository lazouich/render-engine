from abc import ABC, abstractmethod


class BasePageParser(ABC):
    def __init__(self, page: "Page", **kwargs):
        for value in self.configuration_values:
            setattr(self, value, kwargs.get(value, None))

    @property
    @abstractmethod
    def configuration_values(self) -> list[str]:
        """The configuration values that the parser needs"""
        pass

    @staticmethod
    @abstractmethod
    def attrs_from_content_path(self, content_path):
        """
        Fething content from a content_path and set attributes.
        """
        pass

    @abstractmethod
    def markup_from_content_path(self, content_path):
        """
        Fetching content from a content_path and render markup.
        Often you will likely return the results of `self.parse` where `content` is the fetched content.
        """
        pass

    @abstractmethod
    def parse(self, content):
        """Convert the raw_content into HTML or the finalized format"""
        pass
