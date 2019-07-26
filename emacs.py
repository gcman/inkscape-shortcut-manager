import os
import tempfile
import subprocess
from constants import TARGET
from clipboard import copy
from config import config
from Xlib import X

<<<<<<< HEAD:emacs.py
def open_emacs(self, compile_latex):
    f = tempfile.NamedTemporaryFile(mode='w+', suffix='.inkmath',delete=False)
=======
def open_vim(self, compile_latex):
    f = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.tex')
>>>>>>> upstream/master:vim.py

    f.write('\(\)')
    f.close()

<<<<<<< HEAD:emacs.py
    subprocess.run([
        'emacsclient',
        '-c',
        '-F', '((width . 60) (height . 5) (title . \"floatingEmacs\"))',
        f"{f.name}",
    ])
=======
    config['open_editor'](f.name)
>>>>>>> upstream/master:vim.py

    latex = ""
    with open(f.name, 'r') as g:
        latex = g.read().strip()

    os.remove(f.name)

    if latex != '$$':
        if not compile_latex:
            svg = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
            <svg>
              <text
<<<<<<< HEAD:emacs.py
                 style="font-size:10px; font-family:'Hack';-inkscape-font-specification:'Hack, Normal';fill:#000000;fill-opacity:1;stroke:none;"
=======
                 style="font-size:{config['font_size']}px; font-family:'{config['font']}';-inkscape-font-specification:'{config['font']}, Normal';fill:#000000;fill-opacity:1;stroke:none;"
>>>>>>> upstream/master:vim.py
                 xml:space="preserve"><tspan sodipodi:role="line" >{latex}</tspan></text>
            </svg> """
            copy(svg, target=TARGET)
        else:
            m = tempfile.NamedTemporaryFile(mode='w+', delete=False)
<<<<<<< HEAD:emacs.py
            m.write(r"""
                \documentclass[12pt,border=12pt]{standalone}
                \usepackage[utf8]{inputenc}
                \usepackage[T1]{fontenc}
                \usepackage{gm-math}
                \begin{document}
            """ + latex + r"""\end{document}""")
=======
            m.write(config['latex_document'](latex))
>>>>>>> upstream/master:vim.py
            m.close()

            working_directory = tempfile.gettempdir()
            subprocess.run(
                ['pdflatex', m.name],
                cwd=working_directory,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            subprocess.run(
                ['pdf2svg', f'{m.name}.pdf', f'{m.name}.svg'],
                cwd=working_directory
            )

            with open(f'{m.name}.svg') as svg:
                subprocess.run(
                    ['xclip', '-selection', 'c', '-target', TARGET],
                    stdin=svg
                )

        self.press('v', X.ControlMask)
    self.press('Escape')
