# decrypt_logs.py
# Reads Caesar-encrypted logs, decrypts them (left shift of 3),
# saves all lines to a master file, and BREACH lines to an alert file.

infile = open("raw_logs.txt", "r")
master = open("decrypted_master.txt", "w")
alerts = open("security_alerts.txt", "w")

total_lines = 0
alert_lines = 0

for line in infile:
    decrypted = ""

    for ch in line:
        if ch == " " or ch == "\n":
            # keep spaces and newlines as they are
            decrypted = decrypted + ch
        elif ch >= "A" and ch <= "Z":
            # left shift of 3 with wrap-around for capital letters
            decrypted = decrypted + chr((ord(ch) - ord("A") - 3) % 26 + ord("A"))
        elif ch >= "a" and ch <= "z":
            # left shift of 3 with wrap-around for small letters
            decrypted = decrypted + chr((ord(ch) - ord("a") - 3) % 26 + ord("a"))
        else:
            # digits and punctuation were not encrypted
            decrypted = decrypted + ch

    decrypted = decrypted.strip()

    master.write(decrypted + "\n")
    total_lines = total_lines + 1

    if "BREACH" in decrypted.upper():
        alerts.write(decrypted + "\n")
        alert_lines = alert_lines + 1

infile.close()
master.close()
alerts.close()

print("Lines decrypted:", total_lines)
print("Alert lines written:", alert_lines)
