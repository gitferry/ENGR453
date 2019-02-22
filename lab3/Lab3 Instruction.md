# Lab3 Instruction

-- by Fangyu Gai. Any questions --> fangyu.gai@ubc.ca

---

For lab3, we will get our hands on the Raspberry Pi!
Due to some limitations, we only have 14 Raspberry Pis for each section, so you need to find a partner to get lab3 and future labs done.
What's more, you can only finish them in the lab.
**Raspberry Pis must stay in the lab**, except that you can use your own Raspberry Pi and you can finish them out of the lab.

Lab3 is super duper easy. The ultimate goal is to log into the Raspberry Pi using SSH clients, very similar to lab2, where we aim to log into the EC2 instance.
By doing that, you will no longer need a monitor, keyboard and mouse to controll your Raspberry Pi.
Give commands to the Raspberry Pi using your own computer.

## Part 1 Setup the Raspberry Pi

A Raspberry Pi is basically a tiny computer running a linux operation system.
Please follow this video to learn some basics about the Raspberry Pi and how to set it up.

[Getting Started With The Raspberry Pi 3](https://www.youtube.com/watch?v=gbJB3387xUw)

## Part 2 Log in the Raspberry Pi with SSH

To log in the Raspberry Pi, we need do some preparatory work:

1. Both the Raspberry Pi and your computer should be under the same LAN (Local Area Network), e.g. under the same Wi-Fi.
2. Get the IP address of the Raspberry Pi.
3. Get the username and the password of the Raspberry Pi. The default is "Pi" and "Raspberry", respectively.
4. Turn on the ssh port on the Raspberry Pi, which is shown in the video [Getting Started With The Raspberry Pi 3](https://www.youtube.com/watch?v=gbJB3387xUw)
5. Have SSH client installed on your computer, e.g. Putty for Windows and built-in ssh client for Mac OS and linux.

Here is a video turtorial showing how to remotely connect the Pi from Windows with Putty SSH.

[Remotely Connect from Windows with Putty SSH Telnet Client](https://www.youtube.com/watch?v=nQo5Qhvx5nc)

For Mac OS or Linux users, you can follow the above turtorial to get the IP address of the Pi, then open your terminal and type out the following command:

```
ssh pi@<IP>
```

If you receive a connection timed out error it is likely that you have entered the wrong IP address for the Raspberry Pi.

When the connection works you will see a security/authenticity warning. Type `yes` to continue. You will only see this warning the first time you connect.

In the event your Pi has taken the IP address of a device to which your computer has connected before (even if this was on another network), you may be given a warning and asked to clear the record from your list of known devices.
Following this instruction and trying the ssh command again should be successful.

Next you will be prompted for the password for the `pi` login: the default password is `raspberry`. 
