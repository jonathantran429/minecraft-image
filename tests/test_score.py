import pytest
from minecraft_image.score import Scorer

class TestScorerInstance:
    def test_score_mismatched_dimensions1(self):
        scorer = Scorer()
        target = [[1,0],[0,1]]
        rendered = [[1,0],[1,0,0]]
        with pytest.raises(ValueError):
            scorer.silhouette_error(target, rendered)

    def test_score_mismatched_dimensions2(self):
        scorer = Scorer()
        target = [[1,0],[0,1]]
        rendered = [[1,0]]
        with pytest.raises(ValueError):
            scorer.silhouette_error(target, rendered)

    def test_score_mismatched_dimensions3(self):
        scorer = Scorer()
        target = [[1,0],[0,1]]
        rendered = [[]]
        with pytest.raises(ValueError):
            scorer.silhouette_error(target, rendered)

    def test_score_mismatched_dimensions4(self):
        scorer = Scorer()
        target = [[]]
        rendered = [[1,0],[1,0,0]]
        with pytest.raises(ValueError):
            scorer.silhouette_error(target, rendered)

    def test_score_mismatched_dimensions5(self):
        scorer = Scorer()
        target = [[]]
        rendered = [[1,0]]
        with pytest.raises(ValueError):
            scorer.silhouette_error(target, rendered)

    def test_no_error(self):
        scorer = Scorer()
        target = [[1,0],[0,1]]
        rendered = target
        expected_error = 0
        assert scorer.silhouette_error(target, rendered) == expected_error

    def test_extra_line_pixels(self):
        scorer = Scorer()
        target = [[1,0],[0,1]]
        rendered = [[1,1],[1,1]]
        expected_error = 2
        assert scorer.silhouette_error(target, rendered) == expected_error

    def test_missing_line_pixels(self):
        scorer = Scorer()
        target = [[1,0],[0,1]]
        rendered = [[0,0],[0,0]]
        expected_error = 4
        assert scorer.silhouette_error(target, rendered) == expected_error
    
    def test_extra_and_missing_line_pixels(self):
        scorer = Scorer()
        target = [[1,0],[0,1]]
        rendered = [[0,1],[1,0]]
        expected_error = 6
        assert scorer.silhouette_error(target, rendered) == expected_error

    def test_no_error_rectangular(self):
        scorer = Scorer()
        target = [[1,0],[0,1],[0,0]]
        rendered = target
        expected_error = 0
        assert scorer.silhouette_error(target, rendered) == expected_error

    def test_extra_line_pixels_rectangular(self):
        scorer = Scorer()
        target = [[1,0],[0,1],[0,0]]
        rendered = [[1,1],[1,1],[1,1]]
        expected_error = 4
        assert scorer.silhouette_error(target, rendered) == expected_error

    def test_missing_line_pixels_rectangular(self):
        scorer = Scorer()
        target = [[1,0],[0,1],[1,0]]
        rendered = [[0,0],[0,0],[0,0]]
        expected_error = 6
        assert scorer.silhouette_error(target, rendered) == expected_error
    
    def test_extra_and_missing_line_pixels_rectangular(self):
        scorer = Scorer()
        target = [[1,0],[0,1],[0,1]]
        rendered = [[0,1],[1,0],[1,0]]
        expected_error = 9
        assert scorer.silhouette_error(target, rendered) == expected_error