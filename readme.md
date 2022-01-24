## Advent Calendar solved entierly using python

### How to use

First you need to git clone the repository. You need to make sure that python is installed. Next install the requirements.txt to make sure that it works

`pip install -r requirements.txt`

Next you setup the config file from `config-template.py`! There are detailed steps in the file so it shouldn't that hard.

Then you can run the script with the following command:

`python main.py --year [year] --day [day]`

Running a day that doesn't exsits will create a runner file for the day. This is a public repo meaning you can create your own answers and commit to the repo.

### Journey of advent calendar

When I first learnt about advent calendar, I was sure I could solve it under minutes. Turns out I was wrong. I solved a lot of my problems in JS at start not really documenting or saving my answers. After a year or so I came back with a fresh start and I have made this github repo to track my progress.

#### TODO

- Add a `requirements.txt` file with al the dependencies
- If the `config.py` doesn't exist, create it from the template
- Create a github workflow that generates a site to logs all the progress
- Complete all the days	from all the years
- Change the folder structure to [year] -> [day].py and [year] -> inputs -> [day].txt
- Make it so the `split_data` can also be a function