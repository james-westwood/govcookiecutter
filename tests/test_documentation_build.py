from pathlib import Path
import subprocess


class TestDocumentation:
    def test_build(self, tmp_path: Path) -> None:
        """Test the build of the main `govcookiecutter` repository."""
        result = subprocess.run(["mkdocs", "build", "--site-dir", str(tmp_path.joinpath("site"))], check=True)
        assert result.returncode == 0