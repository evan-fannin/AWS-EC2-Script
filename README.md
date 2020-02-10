# AWS-EC2-Script

This script is very similar to the one in my [News-Scraper](https://github.com/evan-fannin/News-Scraper) repository, except that it now has a function to place what it gathers in an S3 bucket as a .csv file.

The majority of the work on this project was not in writing the script, but in navigating the workings of AWS in general, and then specifically of AWS EC2 ([Elastic Compute Cloud](https://en.wikipedia.org/wiki/Amazon_Elastic_Compute_Cloud)), AWS VPC ([Virtual Private Cloud](https://en.wikipedia.org/wiki/Amazon_Virtual_Private_Cloud)), AWS IAM ([Identity and Access Management](https://aws.amazon.com/iam/)), and AWS S3 ([Simple Storage Service](https://en.wikipedia.org/wiki/Amazon_S3)).

I by no means have mastered these services, but I was able to create an instance on EC2, SSH ([Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell)) into it from my terminal, install an updated python, pip, and the dependency packages, and then send a scraped file into an S3 bucket that I created with the necessary access permissions.

While I have found a preexisting news dataset that I plan to use in my exploration of NLP, I thought it would be worthwhile to take the time to get an elementary grasp of these very useful AWS services. With a little more learning, I could schedule a cron job on a EC2 instance and build up a dataset of my own in a S3 bucket with daily web scrapes.

