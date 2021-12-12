# Adjust assignment

### Given test scenarios:
   1. [http://127.0.0.1:8001/api/app_performances/?date_to=2017-05-31&group_by=channel,country&fields=channel,country,impressions,clicks&ordering=-clicks](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi)
   2. [http://127.0.0.1:8001/api/app_performances/?date_from=2017-05-01&date_to=2017-05-31&os=ios&group_by=date&ordering=-date&fields=date,installs](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi)
   3. [http://127.0.0.1:8001/api/app_performances/?date=2017-06-01&country=US&group_by=os&ordering=-revenue&fields=os,revenue](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi)
   4. [http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi]([http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi))


### Login in to admin and create your superuser to add data:
    python manage.py createsuperuser
    url: http://127.0.0.1:8001/admin/

##  Steps

1. 
2. Open shell/terminal and run following command to clone the project:
    <br>`git clone https://github.com/hamzafaisaljarral/Adjustment.git`

## Versions
3. <b>python3</b> and <b>pip3</b> are installed .
## run the project

4. source djangoenv/bin/activate
5. cd adjust
6. pip3 install -r requirments.txt
7. python3 manage.py migrate
8. python3 manage.py runserver 8000

9.Following URL will open swagger UI from where all the project APIs can be accessed:
     http://127.0.0.1:8000/api/pattern/swagger/

10.Here are the URLs for 4 mentioned scenarios:
    1. [http://127.0.0.1:8001/api/app_performances/?date_to=2017-05-31&group_by=channel,country&fields=channel,country,impressions,clicks&ordering=-clicks](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi)
    2. [http://127.0.0.1:8001/api/app_performances/?date_from=2017-05-01&date_to=2017-05-31&os=ios&group_by=date&ordering=-date&fields=date,installs](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi)
    3. [http://127.0.0.1:8001/api/app_performances/?date=2017-06-01&country=US&group_by=os&ordering=-revenue&fields=os,revenue](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi)
    4. [http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi]([http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi](http://127.0.0.1:8001/api/app_performances/?country=CA&group_by=channel&ordering=-cpi&fields=channel,spend,cpi))

### Data import from excel
User can import the Excel data into the system from admin panel first create a super user to login in to admin:
    python3 manage.py createsuperuser
    url: http://127.0.0.1:8001/admin/
    

Once logged in, go to **App Performance** and use import/export actions to import or export data.

## Tests
Following command can be used to run test cases:


    python manage.py test


