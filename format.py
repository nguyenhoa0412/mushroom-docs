import os
import subprocess

def format_rst_files(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".rst"):
                full_path = os.path.join(dirpath, filename)
                print(f"Formatting: {full_path}")
                
                env = os.environ.copy()
                env["PYTHONUTF8"] = "1"
                subprocess.run(["python", "-m", "rstfmt", full_path], env=env)

                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                normalized = content.replace('\r\n', '\n').replace('\r', '\n')
                with open(full_path, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(normalized)

if __name__ == "__main__":
    format_rst_files(".")