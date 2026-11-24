"""Teste da importação de ``py.main`` pela raiz do repositório."""

import subprocess
import sys
import unittest


class TestImportacaoPacote(unittest.TestCase):
    """Garante que o menu pode ser usado tanto como módulo quanto como script."""

    def test_importa_funcoes_do_menu_como_pacote(self):
        """A importação pela raiz não deve depender de alterar ``sys.path``."""
        processo = subprocess.run(
            [
                sys.executable,
                "-c",
                "from py.main import data_valida; print(data_valida('2025-01-01'))",
            ],
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(processo.returncode, 0, processo.stderr)
        self.assertEqual(processo.stdout.strip(), "True")


if __name__ == "__main__":
    unittest.main()
