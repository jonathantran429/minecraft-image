from minecraft_image.blockstate import BlockState
from minecraft_image.scene import Scene

class TestSceneInstance:
    def test_empty_get_block(self):
        scene = Scene()
        coordinate = (0,0,0)
        assert scene.get_block(coordinate) is None

    def test_empty_remove_block(self):
        scene = Scene()
        coordinate = (0,0,0)
        assert scene.remove_block(coordinate) == False

    def test_add_block1(self):
        scene = Scene()
        block = BlockState(1)
        coordinate = (0,0,0)
        assert scene.add_block(coordinate, block) is None

    def test_add_block2(self):
        scene = Scene()
        block = BlockState(3)
        coordinate = (0,0,1)
        assert scene.add_block(coordinate, block) is None 

    def test_get_block1(self):
        scene = Scene()
        block = BlockState(1)
        coordinate = (0,0,0)
        assert scene.add_block(coordinate, block) is None
        assert scene.get_block(coordinate) == block

    def test_get_block2(self):
        scene = Scene()
        block = BlockState(3)
        coordinate = (0,0,1)
        assert scene.add_block(coordinate, block) is None 
        assert scene.get_block(coordinate) == block

    def test_override_block(self):
        scene = Scene()
        block1 = BlockState(1)
        block2 = BlockState(3)
        coordinate1 = (0,0,0)
        assert scene.add_block(coordinate1, block1) is None
        assert scene.get_block(coordinate1) == block1
        assert scene.add_block(coordinate1, block2) is None 
        assert scene.get_block(coordinate1) == block2

    def test_multiple_blocks(self):
        scene = Scene()
        block1 = BlockState(1)
        block2 = BlockState(2)
        block3 = BlockState(3)
        coordinate1 = (0,0,0)
        coordinate2 = (0,0,1)
        assert scene.add_block(coordinate1, block1) is None
        assert scene.get_block(coordinate1) == block1
        assert scene.add_block(coordinate1, block2) is None 
        assert scene.get_block(coordinate1) == block2 
        assert scene.add_block(coordinate2, block3) is None 
        assert scene.get_block(coordinate2) == block3
        assert scene.get_block(coordinate1) == block2

    def test_remove_block(self):
        scene = Scene()
        block = BlockState(1)
        coordinate = (0,0,0)
        assert scene.add_block(coordinate, block) is None
        assert scene.remove_block(coordinate) == True 
        assert scene.remove_block(coordinate) == False
        assert scene.get_block(coordinate) is None 
        

