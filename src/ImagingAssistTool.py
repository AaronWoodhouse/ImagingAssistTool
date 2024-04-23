import socket
import sys
import time

import pyperclip
from getmac import get_mac_address


class Team:
    team = 0
    dp = 0
    member1 = ""
    member2 = ""

    def __init__(self):
        self.team = get_input("Team Number: ")
        self.dp = get_input("DP Number: ")
        self.member1 = get_input("Member Name: ")
        self.member2 = get_input("Member Name: ")

    def __str__(self):
        return "Team {}, DP{}, {} and {}.".format(self.team, self.dp, self.member1, self.member2)


def get_ip():
    for i in range(4):
        try:
            ip = socket.gethostbyname(socket.getfqdn())
            return ip
        except OSError:
            print("Unable to connect to DNS. Check ethernet connection.")
            time.sleep(2)

    sys.exit(1)


def get_mac(ip):
    for i in range(4):
        try:
            mac = get_mac_address(ip=ip)
            return mac
        except OSError:
            print("Unable to fetch MAC address.")
            time.sleep(2)

    sys.exit(1)


def get_input(msg):
    user_input = input(msg)
    # TODO: input validation
    return user_input


def menu(team, ip, mac, school, room):
    options = ["IP and MAC", "Remote Setup", "End of Day", "Exit"]
    print("Please select an option:")

    for i, option in enumerate(options):
        print("{}. {}".format(i + 1, option))

    while True:
        option = int(input("Select Option: "))

        if option == 1:
            # IP and MAC
            msg = ("Hi it's {} and {} at {}, in {}. I have connected my laptop; I have a link. Here is my IP and Mac "
                   "address for my wired connection. Please confirm the port is correct before I connect the imaging "
                   "switch. {}, {}(Preferred) and I have DP{}.").format(team.member1, team.member2, school, room,
                                                                        mac, ip, team.dp)

            pyperclip.copy(msg)
            msg = "\nCopied to clipboard!\n" + msg

            return msg

        elif option == 2:
            # Remote Setup
            position = get_input("Staff Position: ")
            name = get_input("Staff Name: ")
            to_setup = []

            while True:
                # To setup
                to_add = get_input("To setup (0 to finish): ")
                if to_add == "0":
                    if len(to_setup) == 0:
                        print("Setup cannot be empty.")
                        continue
                    break

                to_setup.append(to_add)

            msg = ("Hello BRADLEY UPTON and KISHAN MAHADEVA: It’s {} and {} at {}. "
                   "The {}, {}'s machine is complete and ready remote setup of ").format(team.member1, team.member2,
                                                                                         school, position, name)

            # Add setups to msg
            num_setups = len(to_setup)
            if num_setups == 1:
                msg = msg + to_setup[0]
            else:
                for i in range(len(to_setup) - 1):
                    msg = msg + to_setup[i] + ", "
                msg = msg + "and " + to_setup[num_setups - 1]

            msg = msg + "."

            pyperclip.copy(msg)
            msg = "\nCopied to clipboard!\n" + msg

            return msg

        elif option == 3:
            msg = ("Hi it's {} and {}. {} with DP{} is Complete. "
                   "Network/UEA teams please reconfigure port/server.").format(team.member1, team.member2, school,
                                                                               team.dp)

            pyperclip.copy(msg)
            msg = "\nCopied to clipboard!\n" + msg

            return msg

        elif option == 4:
            # Exit
            return 0

        else:
            print("Please select a valid message type.")


def main():
    print("--- Imaging Assist Tool ---")

    ip = get_ip()
    mac = get_mac(ip)

    print(mac, ",", ip)

    team = Team()
    school = get_input("School Name: ")
    room = get_input("Room: ")
    print()

    while True:
        msg = menu(team, ip, mac, school, room)

        if msg == 0:
            break

        print(msg + "\n")


if __name__ == "__main__":
    main()
