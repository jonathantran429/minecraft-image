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

    def test_project_invalid_point1(self):
        position = (0,0,0)
        focal_length = 1
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point1 = (0,0,1) # z > camera_z
        with pytest.raises(ValueError):
            camera.project_point(point1)

    def test_project_invalid_point2(self):
        position = (0,0,0)
        focal_length = 1
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point2 = (0,0,0) # z == camera_z
        with pytest.raises(ValueError):
            camera.project_point(point2)

    def test_project_invalid_point3(self):
        position = (0,0,0)
        focal_length = 1
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point3 = (1, -1, 5) # z > camera_z
        with pytest.raises(ValueError):
            camera.project_point(point3)

    def test_project_invalid_point4(self):
        position = (0,0,0)
        focal_length = 1
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point4 = (-123, 10, 0) # z == camera_z
        with pytest.raises(ValueError):
            camera.project_point(point4)

    def test_project_direct_point1(self):
        position = (0,0,0)
        focal_length = 1
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point1 = (0,0,-10)
        expected_projection = (0,0)
        assert camera.project_point(point1) == expected_projection

    def test_project_direct_point2(self):
        position = (0,0,0)
        focal_length = 1
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point2 = (0,0,-100)
        expected_projection = (0,0)
        assert camera.project_point(point2) == expected_projection

    def test_project_direct_point3(self):
        position = (0,0,0)
        focal_length = 1
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point3 = (0,0, -1) 
        expected_projection = (0,0)
        assert camera.project_point(point3) == expected_projection

    def test_project_indirect_point1(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point1 = (1,0,0)
        expected_projection1 = (5,0)
        assert camera.project_point(point1) == expected_projection1

    def test_project_indirect_point2(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point2 = (0,1,0)
        expected_projection2 = (0,5)
        assert camera.project_point(point2) == expected_projection2

    def test_project_indirect_point3(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point3 = (1,0,5)
        expected_projection3 = (10,0)
        assert camera.project_point(point3) == expected_projection3

    def test_invalid_coordinate_to_image_indices1(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point1 = (50,0)
        with pytest.raises(IndexError):
            camera.image_index(point1)

    def test_invalid_coordinate_to_image_indices2(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point2 = (0,50)
        with pytest.raises(IndexError):
            camera.image_index(point2)

    def test_invalid_coordinate_to_image_indices3(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point3 = (50,50)
        with pytest.raises(IndexError):
            camera.image_index(point3)

    def test_invalid_coordinate_to_image_indice4(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point4 = (100, 100)
        with pytest.raises(IndexError):
            camera.image_index(point4)

    def test_invalid_coordinate_to_image_indices5(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point5 = (-51, 0)
        with pytest.raises(IndexError):
            camera.image_index(point5)

    def test_invalid_coordinate_to_image_indices6(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point6 = (0,- 51)
        with pytest.raises(IndexError):
            camera.image_index(point6)

    def test_invalid_coordinate_to_image_indices7(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point7 = (-51, -51)
        with pytest.raises(IndexError):
            camera.image_index(point7)

    def test_invalid_coordinate_to_image_indices8(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point8 = (-100, -100)
        with pytest.raises(IndexError):
            camera.image_index(point8)

    # def test_invalid_coordinate_to_image_indices9(self):
    #     position = (0,0,0)
    #     focal_length = 50
    #     image_dim = (3,3)
    #     #      0      1      2
    #     # 0 (-1,1)  (0,1)  (1,1)
    #     # 1 (-1,0)  (0,0)  (1,0)
    #     # 2 (-1,-1) (0,-1) (1,-1)
    #     # 
    #     # Something like (0.99, 0.99) still maps to (0,0) in img coordinates which maps to (1,1) in array indices
    #     # Something like (-1.99, 1.99) still maps to (-1, 1) in img coordinates which maps to (0,0) in array indices
    #     camera = Camera(position, image_dim, focal_length)
    #     point9 = ()
    #     with pytest.raises(IndexError):
    #         camera.image_index(point9)

    def test_valid_coordinate_to_image_indices1(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point1 = (0,0)
        expected_image_index1 = (50,50)
        assert camera.image_index(point1) == expected_image_index1

    def test_valid_coordinate_to_image_indices2(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point2 = (5,0)
        expected_image_index2 = (55,50)
        assert camera.image_index(point2) == expected_image_index2

    def test_valid_coordinate_to_image_indices3(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point3 = (0,5)
        expected_image_index3 = (50,55)
        assert camera.image_index(point3) == expected_image_index3

    def test_valid_coordinate_to_image_indices4(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point4 = (-50,0)
        expected_image_index4 = (0,50)
        assert camera.image_index(point4) == expected_image_index4

    def test_valid_coordinate_to_image_indices5(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point5 = (0,-50)
        expected_image_index5 = (50,0)
        assert camera.image_index(point5) == expected_image_index5

    def test_valid_coordinate_to_image_indices6(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point6 = (-50,-50)
        expected_image_index6 = (0,0)
        assert camera.image_index(point6) == expected_image_index6

    def test_valid_coordinate_to_image_indices7(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point7 = (49,0)
        expected_image_index7 = (99,50)
        assert camera.image_index(point7) == expected_image_index7

    def test_valid_coordinate_to_image_indices8(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point8 = (0,49)
        expected_image_index8 = (50,99)
        assert camera.image_index(point8) == expected_image_index8

    def test_valid_coordinate_to_image_indices9(self):
        position = (0,0,10)
        focal_length = 50
        image_dim = (100,100)
        camera = Camera(position, image_dim, focal_length)
        point9 = (49,49)
        expected_image_index9 = (99,99)
        assert camera.image_index(point9) == expected_image_index9