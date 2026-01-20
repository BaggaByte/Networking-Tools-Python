import os
import platform

def single_ping():
    target = input("Enter the IP or Domain to ping: ")
    
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    print(f"\n--- Checking connectivity to {target} ---")
    
    command = f"ping {param} 1 {target}"
    response = os.system(command)
    
    # Final Verdict
    print("-" * 35)
    if response == 0:
        print(f"RESULT: [✅] {target} is REACHABLE")
    else:
        print(f"RESULT: [❌] {target} is UNREACHABLE")
    print("-" * 35)

if __name__ == "__main__":
    single_ping()