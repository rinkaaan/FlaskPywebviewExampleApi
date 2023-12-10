WORKPLACE="$HOME/workplace/FlaskPywebviewExample"

(
  cd "$WORKPLACE/FlaskPywebviewExampleApi"
  pyinstaller mac.spec --clean --noconfirm
)
