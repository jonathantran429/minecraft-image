from minecraft_image.blockstate import BlockState

class Scene:
    """Class representing a 3D scene of minecraft blocks.

    Attributes:
        scene (dict): sparse dictionary mapping (x,y,z) coordinates to BlockState objects
    """

    def __init__(self) -> None:
        self._scene = {}

    def get_block(self, coordinate: tuple[int, int, int]) -> BlockState | None:
        """Get a block from the scene at a (x,y,z) coordinate.
        
        Args:
            coordinate: The (x,y,z) coordinate to get a block from.
        
        Returns:
            The BlockState if there is a block at that coordinate, None if not.
        """
        if coordinate not in self._scene:
            return None
        return self._scene[coordinate]

    def add_block(self, coordinate: tuple[int, int, int], block: BlockState) -> None:
        """Add a block to the scene at a (x,y,z) coordinate. Overwrites existing blocks.
        
        Args:
            coordinate: The (x,y,z) coordinate to add the block to.
            block: The block to add to the coordinate.
        """
        self._scene[coordinate] = block 

    def remove_block(self, coordinate: tuple[int, int, int]) -> bool:
        """Remove a block from the scene at a (x,y,z) coordinate. 
        
        Args:
            coordinate: The (x,y,z) coordinate to remove the block from.

        Returns:
            True if there was a block to remove, False otherwise.
        """
        if (coordinate not in self._scene):
            return False
        del self._scene[coordinate]
        return True

