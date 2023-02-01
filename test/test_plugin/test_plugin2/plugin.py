from pathlib import Path
from typing import List

from a13e.plugin import PluginRegister
from a13e.recognizer import RecognizeResult, BaseRecognizer


@PluginRegister.register
class Test(BaseRecognizer):
    def recognize(self, audio_fp: Path, **kwargs) -> List[RecognizeResult]:
        pass

    @property
    def name(self) -> str:
        return 'test_plugin2'
