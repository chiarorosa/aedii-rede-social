"""Teste de execução do programa como script pelo comando documentado."""

import subprocess
import sys
import unittest


class TestExecucaoDireta(unittest.TestCase):
    """Verifica a importação dos módulos ao executar ``python py/main.py``."""

    def test_abre_menu_quando_executado_como_script(self):
        """O comando do README deve carregar o programa e aceitar a saída."""
        processo = subprocess.run(
            [sys.executable, "py/main.py"],
            input="0\n",
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(processo.returncode, 0, processo.stderr)
        self.assertIn("1 - Sugerir usuários", processo.stdout)
        self.assertIn("Programa encerrado.", processo.stdout)


if __name__ == "__main__":
    unittest.main()
