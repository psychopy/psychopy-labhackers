def test_import():
    """
    Test that classes can import without error
    """
    from psychopy_labhackers.millikey import MillikeyHIDButtonGroup, MillikeySerialButtonGroup

def test_entry_points():
    """
    Test that classes are available from the correct locations after registering entry points
    """
    # activate plugins
    from psychopy.plugins import activatePlugins
    activatePlugins()
    # import from entry points
    from psychopy.hardware import MillikeyHIDButtonGroup, MillikeySerialButtonGroup
