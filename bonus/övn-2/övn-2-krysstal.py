

# exercise 1
def rectangle_area(height, width):
    """
    :param height: height of rectangle
    :param width: width of rectangle
    :return: area of a rectangle with the specified width and height
    """
    assert isinstance(width, int) or isinstance(width, float), "Width has to be a number!"
    assert isinstance(height, int) or isinstance(height, float), "Height has to be a number!"
    assert (not isinstance(width, bool)) and (not isinstance(height, bool)), "Width/height can't be a boolean"
    return height*width


# exercise 2
def rectangle_circumference(height, width):
    """
    :param height: height of rectangle
    :param width: width of rectangle
    :return: circumference of a rectangle with the specified width and height
    """
    assert isinstance(width, int) or isinstance(width, float), "Width has to be a number!"
    assert isinstance(height, int) or isinstance(height, float), "Height has to be a number!"
    assert (not isinstance(width, bool)) and (not isinstance(height, bool)), "Width/height can't be a boolean"

    # Since the sides are parallel, we multiply the height and width by two and add them together.
    return height * 2 + width * 2


# exercise 3
def third_character_of_string(string):
    """
    :param string: string to get the third character of
    :return: the third character of the given string
    """
    if len(string) < 3:
        return False
    else:
        # Since indexing starts at 0, the third character will have the index 2
        return string[2]


def main():
    # Making sure that the functions return the proper results
    assert third_character_of_string("abcdef") == "c"
    assert third_character_of_string("hi") is False
    assert rectangle_area(2, 5) == 10
    assert rectangle_circumference(2, 6) == 16


if __name__ == "__main__":
    main()

