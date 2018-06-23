# UnClique
the community needs to meet itself


## Overview
UnClique is a program started by the 2017 AASUper Lit Executive Board that will foster Coalition Building and attempt to alleviate the issues of 'Cliques' in the BSO.

This is an opt-in program and by submitting your contact information, you agree to be randomly paired, on a weekly basis (pending) with another user who has opted into the UnClique Program. This will be done in an effort to meet new people outside of your immediate social sphere. You are encouraged to go get coffee, lunch in the student center, set up a study date, or whatever you two agree upon in an effort to meet. Engagements can last 15 min, 30 min, 1 hour, or however long you both deem comfortable.

If you feel that your match is a threat to your personal safety, you are encouraged to reach out to the AASU President at gtaasu.president@gmail.com



## Developer OnBoarding

### Database setup instructions
- `brew install mysql`
- `brew services start mysql`
- `mysql -u root -p`
- Enter your password
- mysql > `create database unclique`

### Python install instructions (for mac)
- `brew install python3` # need python 3.6
- `brew install caskroom/cask/mysql-connector-python`
- `cd` /<PATH_TO_THE_UNCLIQUEPORTAL_PROJECT_ROOT/
- `python3 -m virtualenv venv`
- `source venv/bin/activate`
- `pip install --upgrade pip`
- `pip install -r requirements.txt`

### Start Django Application
- `python manage.py migrate`
- `python manage.py runserver`
