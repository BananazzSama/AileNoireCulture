from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Aile Noire Culture",
    version = "1",
    description = "Votre programme",
    executables = [Executable("aile_noire_culture.py", base = "Win32GUI")],
)

#python setup.py build