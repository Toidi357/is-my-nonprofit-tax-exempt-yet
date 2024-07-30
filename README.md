# is-my-nonprofit-tax-exempt-yet
IRS: "We issue 80% of Form 1023-EZ application determinations within 22 days." <br>
![output](https://github.com/user-attachments/assets/4763d987-291d-40ab-9b94-57e3e246c93f)

## It's been a month, I'm impatient
A Python script on an Ubuntu service to check every 8 hours to see if an EIN's determination letter has been published or not and notifies you via Discord webhook if there's something.

## config.json
You must create a config.json with the following information in it
```
{
   "EIN": "XXXXXXXXX",
   "Webhook": "https://discord.com/api/webhooks/....."
}
```

## Ubuntu service setup
Create a file called \<your desired service name>.service in /etc/systemd/system with the contents
```
#! /usr/bin/python3
[Unit]
Description=is-my-nonprofit-tax-exempt-yet

[Service]
ExecStart=/usr/bin/python3 -u path/to/main.py
Restart=always
User=root

# Note Debian/Ubuntu uses 'nogroup', RHEL/Fedora uses 'nobody'
Group=nogroup
Environment=PATH=/usr/bin:/usr/local/bin
WorkingDirectory=path/to/repository

[Install]
WantedBy=multi-user.target
```
Then run `systemctl daemon-reload`, `systemctl enable <service name>`, `systemctl start <service name>` <br>
You can view logs with `systemctl status <service name>`
