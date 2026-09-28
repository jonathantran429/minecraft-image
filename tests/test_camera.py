import pytest
from minecraft_image.camera import Camera

class TestCameraInstance:
    def test_get_position(self):
        position = (0,0,0)
        focal_length = 1
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        assert (camera.x, camera.y, camera.z) == position

    def test_get_focal_length(self):
        position = (0,0,0)
        focal_length = 1
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        assert camera.focal_length == focal_length

    def test_get_image_dim(self):
        position = (0,0,0)
        focal_length = 1
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        assert (camera.width, camera.height) == image_dim

    def test_project_invalid_point(self):
        position = (0,0,0)
        focal_length = 1
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point1 = (0,0,1) # z > camera_z
        point2 = (0,0,0) # z == camera_z
        point3 = (1, -1, 5) # z > camera_z
        point4 = (-123, 10, 0) # z == camera_z
        with pytest.raises(ValueError):
            camera.project_point(point1)
        with pytest.raises(ValueError):
            camera.project_point(point2)
        with pytest.raises(ValueError):
            camera.project_point(point3)
        with pytest.raises(ValueError):
            camera.project_point(point4)

    def test_project_direct_point(self):
        position = (0,0,0)
        focal_length = 1
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point1 = (0,0,-10)
        point2 = (0,0,-100)
        point3 = (0,0, -1) 
        expected_projection = (0,0)
        assert camera.project_point(point1) == expected_projection
        assert camera.project_point(point2) == expected_projection
        assert camera.project_point(point3) == expected_projection

    def test_project_indirect_point(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point1 = (1,0,0)
        point2 = (0,1,0)
        point3 = (1,0,5)
        expected_projection1 = (5,0)
        expected_projection2 = (0,5)
        expected_projection3 = (10,0)
        assert camera.project_point(point1) == expected_projection1
        assert camera.project_point(point2) == expected_projection2
        assert camera.project_point(point3) == expected_projection3
        
