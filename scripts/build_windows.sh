WORKPLACE="$HOME/workplace/FlaskPywebviewExample"

(
  cd "$WORKPLACE/FlaskPywebviewExampleApi"
  # pyinstaller --onefile api/run.py --icon=dist\\Icon.ico --clean  --noconfirm
  pyinstaller windows.spec --clean --noconfirm
)
