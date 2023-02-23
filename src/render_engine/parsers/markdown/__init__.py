from typing import Any, Type

import frontmatter
from markdown2 import markdown

from ..base_parsers import BasePageParser


class MarkdownPageParser(BasePageParser):
    @staticmethod
    def markup(content: str, page: "Page") -> str:
        """Parses the content with the parser"""
        extras = getattr(page, "parser_extras", {})
        print(f"{extras=}")
        markup = markdown(content, extras=extras.get("markdown_extras", []))
        return markup