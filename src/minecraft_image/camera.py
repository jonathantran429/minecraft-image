class Camera:
    """Class representing the camera for the minecraft build.

    Attributes:
        x (int): the x position of the camera
        y (int): the y position of the camera
        z (int): the z position of the camera
        width (int): the width of the image
        height (int): the height of the image
        focal_length (int): the focal length of the camera
    """

    def __init__(self, position: tuple[int, int, int], image_dim: tuple[int, int], focal_length: int) -> None:
        self.x, self.y, self.z = position
        self.width, self.height = image_dim
        self.focal_length = focal_length


    def project_point(self, coordinate: tuple[int, int, int]) -> tuple[float, float]:
        """Project a 3D point onto a 2D image that this camera sees.
                
        Args:
            coordinate: The (x,y,z) coordinate to project onto the camera's image.
        
        Returns:
            The 2D coordinate of the 3D point as it appears on the camera's image.

        Raises:
            ValueError: if the z value of the coordinate is at or behind the camera's image.
        """
        x, y, z = coordinate
        depth = self.z - z

        if (depth <= 0):
            raise ValueError("Z coordinate cannot be at or behind the camera's image.")

        screen_x = self.focal_length * (x - self.x) / depth
        screen_y = self.focal_length * (y - self.y) / depth
        return (screen_x, screen_y)

        
