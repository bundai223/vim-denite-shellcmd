from .base import Base
import subprocess

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'shellcmd'
        self.kind = 'file'

    def gather_candidates(self, context):
        cmd = ['ls', '-l']
        return [{'word': path, 'action__path': path}
                for path
                in subprocess.run(cmd,
                    check=True,
                    universal_newlines=True,
                    stdout=subprocess.PIPE
                    ).stdout.split()]
