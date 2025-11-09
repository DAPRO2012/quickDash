from typing import overload, Union, Optional

class color:
    r: int
    g: int
    b: int

    @overload
    def __init__(self, r: int, g: int, b: int) -> None:
        self.color = (r, g, b)
    @overload
    def __init__(self, hex: str) -> None: 
        pass

    def __init__(self, r: Union[int, str], g: Optional[int] = None, b: Optional[int] = None) -> None: #type: ignore
        if isinstance(r, str):
            hex_str = r.strip("#")
            if len(hex_str) != 6:
                raise ValueError("Hex string must be 6 characters long (e.g. #RRGGBB)")
            self.r = int(hex_str[0:2], 16)
            self.g = int(hex_str[2:4], 16)
            self.b = int(hex_str[4:6], 16)
        elif g is not None and b is not None:
            self.r = r
            self.g = g
            self.b = b
        else:
            raise TypeError("Color must be initialized with (r, g, b) integers or a (hex) string.")


class coordinates:
    def __init__(self, data_name: str | None = None, values: list[tuple[int, int]] | None = None, accents: list[color] | None = None) -> None:
        ...

class data:
    values: list[int | tuple[int, str]]

    def __init__(self, data_name: str | None = None, values: list[int | tuple[int, str]] = []) -> None:
        self.data_name = data_name
        self.values = values

    def add_value(self, value: int | tuple[int, str]):
        self.values.append(value)

    def to_bar_chart(self, accents: list[color] = [], height: int = 500, width: int = 100) -> str:
        html=""
        maxVal = 1
        for value in self.values:
            if isinstance(value, tuple):
                if value[0] > maxVal:
                    maxVal = value[0]
                html += f"<div class='bar' style='background-color: rgb{accents[0]};'>{"<br>"*value[0]}{value[1]}</div>"
            else:
                if value > maxVal:
                    maxVal = value
                html += f"<div class='bar'>{"<br>"*value}</div>"
        html = f"<h4 class='chartTitle'>{self.data_name}</h4><div class='horizontal-bar-chart' style='line-height: {height/maxVal}px; width: calc( {width}% - 10px - 7px - {len(self.values)*2}px );'>"+html
        html += "</div>"
        return html