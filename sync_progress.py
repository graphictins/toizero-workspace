
    
import os
import tomllib
import tomli_w
import platform
from pathlib import Path

def sync_progress():
    auto_dir = Path(__file__).parent
    note_path = auto_dir.parent / "note.md"
    toml_path = auto_dir / "data.toml"
    
    if not note_path.exists(): return

    lines = note_path.read_text(encoding='utf-8').splitlines()
    current = sum(1 for l in lines if "⚛️" in l or "🆘" in l)

    prev = None
    if toml_path.exists():
        with open(toml_path, "rb") as f:
            prev = tomllib.load(f).get("stats", {}).get("task_left")

    if current != prev:
        # Update file
        content = [f"### TaskLeft == {current}" if "### TaskLeft ==" in l else l for l in lines]
        note_path.write_text("\n".join(content), encoding='utf-8')

        # Update TOML
        with open(toml_path, "wb") as f:
            tomli_w.dump({"stats": {"task_left": current}}, f)

        # Popup
        send_popup(f"TaskLeft == {current}. Keep it up champ!")

def send_popup(msg):
    sys_name = platform.system()
    if sys_name == "Windows":
        # Fast, non-blocking notification using PowerShell
        os.system(f'powershell -WindowStyle Hidden -Command "ls; [reflection.assembly]::loadwithpartialname(\'System.Windows.Forms\'); [System.Windows.Forms.MessageBox]::Show(\'{msg}\', \'Progress\')" &')
    elif sys_name == "Darwin":
        os.system(f"osascript -e 'display notification \"{msg}\" with title \"TOIZero\"' &")
    else:
        os.system(f'notify-send "TOIZero" "{msg}" &')

if __name__ == "__main__":
    sync_progress()