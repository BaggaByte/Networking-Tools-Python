
import matplotlib.pyplot as plt

def ip_to_binary(ip_add):
    octets = ip_add.split(".")
    binary_ip = []
    for octet in octets:
        binary_ip.append(bin(int(octet))[2:].zfill(8))  # convert to 8-bit binary
    return ".".join(binary_ip)

def visualize_subnet(binary_ip, user_cidr):
    clean_binary = binary_ip.replace(".", "")
    colors = []
    for i in range(32):
        if i < user_cidr:
            colors.append("green")   # network bits
        else:
            colors.append("skyblue") # host bits

    fig, ax = plt.subplots(figsize=(10, 2))
    for i, bit in enumerate(clean_binary):
        ax.add_patch(plt.Rectangle((i, 0), 0.8, 1, color=colors[i]))
        ax.text(i + 0.4, 0.5, bit, color='white', ha='center', va='center', fontweight='bold')

    plt.xlim(0, 32)
    plt.ylim(0, 1)
    plt.title(f"SUBNET MAP (CIDR /{user_cidr}) - Green: Network | Blue: Host")
    plt.axis('off')
    plt.show()

# Main program
user_ip = input("Enter an IP Address (e.g. 192.168.1.1): ")
user_cidr = int(input("Enter CIDR (e.g. 24): "))
binary_ip = ip_to_binary(user_ip)

print(f"\nTarget IP: {user_ip}")
print(f"Binary Version: {binary_ip}")
print(f"Network Bits: {user_cidr}")
print(f"Host Bits: {32 - user_cidr}")

visualize_subnet(binary_ip, user_cidr)

