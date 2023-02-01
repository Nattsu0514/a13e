from pathlib import Path
from typing import List

from a13e.plugin import PluginRegister
from a13e.recognizer import BaseRecognizer, RecognizeResult


@PluginRegister.register
class Test(BaseRecognizer):
    def recognize(self, audio_fp: Path, **kwargs) -> List[RecognizeResult]:
        return kwargs

    @property
    def name(self) -> str:
        return 'test_plugin1'
