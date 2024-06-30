from crewai_tools import FileReadTool
from langchain.tools import tool

class DocumentReader():
    @tool
    def read_document(self, file_path):
        """Read the content of a document file."""
        file_reader = FileReadTool(file_path=file_path)
        return file_reader

    def tools():
        return [DocumentReader.read_document]