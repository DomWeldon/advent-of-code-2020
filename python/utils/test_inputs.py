def test_input_directory():
    # arrange
    from .inputs import INPUT_DIRECTORY

    # act
    # assert
    assert INPUT_DIRECTORY.exists()
