class Scorer:
    """Class representing the scorer for comparing images to the minecraft build.
    """

    def silhouette_error(self, target: list[list[int]], rendered: list[list[int]]) -> int:
        """Return error calculated based on (2*missing black pixels + extra black pixels).

        1s represent black pixels and 0 represent white pixels.
        Missing black pixels are defined as 0's in rendered where there is a 1 in target.
        Extra black pixels are defined as 1's in rendered where there is a 0 in target.

        Args:
            target: the target image, a 2D array of 1s and 0s.
            rendered: the rendered image to be scored, a 2D array of 1s and 0s.
        
        Returns:
            The error score of the rendered image when compared against the target image.

        Raises:
            ValueError: If the target and rendered lists don't match in dimensions.
        """
        if (len(target) != len(rendered) or [len(row) for row in target] != [len(row) for row in rendered]):
            raise ValueError("Target and rendered must have the same dimensions.")
        error = 0
        for row in range(len(target)):
            for col in range(len(target[row])):
                if (target[row][col] == 1 and rendered[row][col] == 0):
                    error += 2
                elif (target[row][col] == 0 and rendered[row][col] == 1):
                    error += 1
        return error

