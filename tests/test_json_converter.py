import pytest

from src.FitToJson import converter


class TestFitToJSON:
    def __int__(self):
        pass

    def test_converter_parameters_and_return_types(self):
        input_file = "tests/data/fitfiles/Activity/2020-12-31-12-00-00.fit"
        output_file = "tests/data/fitfiles/Activity/2020-12-31-12-00-00.json"

        conversion = converter.converter(
            input_file,
            output_file
        )

        assert type(conversion) == type(dict())

    def test_fit_csv_tool_return_successfully(self):
        input_file = "data/fitfiles/Activity/2023-04-13-20-25-48.fit"
        output_file = "data/parsed/2020-12-31-12-00-00.csv"

        conversion = converter.run_fit_csv_tool(
            input_file,
            output_file
        )

        assert conversion["code"] == 0
