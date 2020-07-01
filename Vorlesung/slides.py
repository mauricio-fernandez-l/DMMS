import glob
import subprocess

#for notebook in glob.glob("*.ipynb"):
notebooks = [
    '01_Einfuehrung.ipynb',
    ]
for notebook in notebooks:
    print("make slides for: ", notebook)
    command = "jupyter nbconvert " + notebook + " --to slides --SlidesExporter.reveal_scroll=True"
    subprocess.run(command, shell=True)