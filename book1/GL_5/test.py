#!/usr/bin/env python3

import CharGrid

CharGrid.resize(14, 50)
CharGrid.add_rectangle(0,0, *CharGrid.get_size())

CharGrid.add_vertical_line(5, 10 ,13)

CharGrid.render(False)
