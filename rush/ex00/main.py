from checkmate import checkmate

config = {
    "Debug": False
}

def test_():
    test_boards = [
        """\
        .... 
        .K..
        R...
        ....\
        """,

        """\
        .... 
        ..K.
        .P..
        ....\
        """,

        """\
        .... 
        .K..
        ..B.
        ....\
        """,

        """\
        .... 
        ..K.
        .P..
        .P..
        ....\
        """,

        """\
        .... 
        .K..
        .B..
        ....\
        """, 

        """\
        ..Q.
        .K..
        ....
        ....\
        """,

        """\
        .... 
        ..K.
        R...
        ....\
        """,

        """\
        ..R.
        .K..
        ....
        ....\
        """,

        """\
        ..Q.
        .K..
        ....
        ....\
        """,

        """\
        ..K.
        .R..
        ....
        ....\
        """, 

        """\
        .... 
        K...
        .R..
        ....\
        """,
        
        """\
        .... 
        .K..
        .P..
        P...
        ....\
        """,

        """\
        .B..
        .K..
        ....
        ....\
        """,
    ]

    for board in test_boards:
        print("\nTesting board:")
        print(board)
        checkmate(board, config)

if __name__ == "__main__":
    test_()
