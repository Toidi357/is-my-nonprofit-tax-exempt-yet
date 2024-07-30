# is-my-nonprofit-tax-exempt-yet
IRS: "We issue 80% of Form 1023-EZ application determinations within 22 days."
![output](https://github.com/user-attachments/assets/4763d987-291d-40ab-9b94-57e3e246c93f)

## It's been a month, I'm impatient
A Python script on an Ubuntu service to check every 8 hours to see if an EIN's determination letter has been published or not

## config.json
You must create a config.json with the following information in it
```
{
   "EIN": "XXXXXXXXX",
   "Webhook": "https://discord.com/api/webhooks/....."
}
```
