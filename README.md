# wize
A simple duty manager for organizations.

## Installation
1. Install python3, pip, virtualenv in your system.
2. Clone the project https://github.com/kahoor/wize.git.
3. Make development environment ready using commands below;

```bash
git clone https://github.com/kahoor/wize.git
virtualenv project-env
source project-env/bin/activate
cd kernel
pip install -r requirements.txt
cd kernel
python manage.py migrate
```
4. Run Wize using ```python manage.py runserver```
5. Go to ```http://localhost:8000``` to see your Wize version.


## APIs

1. accounts

* Show Accessible Accounts : `GET /api/accounts/usersinfo`
* Create Account : `POST /api/accounts/register`
* Show An Account : `GET /api/accounts/:pk/`
* Update An Account : `PUT /api/accounts/:pk/` 

                     SiteAdmin or Director of an Organization can change some users(`GET /api/accounts/usersinfo` these users) role or organization.
                     SiteAdmin can do both but Director of an Organization can change role from EO to EE(fire employee).


2. organization

* Show Organizations : `GET /api/organization` Permission: SiteAdmin
* Create Organization : `POST /api/organization` Permission: SiteAdmin
* Show UpgradeRequests : `GET /api/organization/upgraderequest/` 

                    SiteAdmin : every upgradereques from Employee to Director.
                    Director : every upgradereques from Employee of same organization to Director, or from Employee to Employee of same organization.
                    Employee : only his/her requests.                    
* Create UpgradeRequests : `POST /api/organization/upgraderequest/` any Employee can create UpgradeRequest.
* Show An UpgradeRequest : `GET /api/upgraderequest/:pk/` 

                    SiteAdmin and Director can see one's upgraderequest.
* Update An UpgradeRequest : `Put /api/upgraderequest/pk/` 

                    SiteAdmin and Director can accept or reject one's upgraderequest.
                    Employee can update his request.


3. organization

* Show Accessible Duties : `GET /api/duties` 

                    SiteAdmin : all Duties.
                    Director : all Duties for his/her Employee(same organization).
                    Employee : only his/her Duties.   
* Create Duties : `POST /api/duties` 

                    SiteAdmin : can't create anything.
                    Director : can create a duty for his/her Employee(same organization).
                    Employee : can only create a duty for himself/herself.  
* Show A Duty : `GET /api/duties/:pk/` 

                    SiteAdmin : all Duties.
                    Director : all Duties for his/her Employee(same organization).
                    Employee : only his/her Duties.
* Update A Duty : `PUT /api/duties/:pk/` 

                    SiteAdmin : all Duties.
                    Director : all Duties for his/her Employee(same organization).
                    Employee : only his/her Duties.
* Delete A Duty : `DELETE /api/duties/:pk/` 


## Database

I used Postgresql because I had some experienced with that.
And it's easy to use.





