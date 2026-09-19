from src.ai import generate_ideas,generate_package
from src.config import Settings
def test_ideas(): assert len(generate_ideas(3))==3
def test_package(): assert generate_package("AI automation").title
def test_defaults(): assert Settings.from_env().upload_privacy=="private"
