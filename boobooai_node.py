#!/usr/bin/env python3
"""
BooBooAI-Corps Core Execution Node
Owner: boobooaicorps-arch (boobooaicorps@gmail.com)
"""
import subprocess, shlex, json, sys

def execute_system_payload(command: str) -> dict:
    args = shlex.split(command)
    if not args:
        return {"exit_code": -1, "stdout": "", "stderr": "Null payload."}
    try:
        res = subprocess.run(args, capture_output=True, text=True, timeout=30)
        return {
            "exit_code": res.returncode,
            "stdout": res.stdout.strip(),
            "stderr": res.stderr.strip()
        }
    except Exception as e:
        return {"exit_code": -1, "stdout": "", "stderr": str(e)}

if __name__ == "__main__":
    print("[+] BooBooAI-Corps Node Initialized.")
    print(json.dumps(execute_system_payload("uname -a"), indent=2))
