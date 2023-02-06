# JTMC(Json to model converter)
## What can the program do?
- Converts json to models
- Can read stdin
- Can read usual file with args: -f or --file

## Examples
1. Combine httpie/curl with the jtms:
- Getting usual json:
```https https://dummy.restapiexample.com/api/v1/employees
{
    "data": [
        {
            "employee_age": 61,
            "employee_name": "Tiger Nixon",
            "employee_salary": 320800,
            "id": 1,
            "profile_image": ""
        },
        ...
    ],
    "message": "Successfully! All records has been fetched.",
    "status": "success"
}
```
- Getting a model
```https https://dummy.restapiexample.com/api/v1/employees | ./jtms.py        
ROOT
status
data
message

DATA
employee_name
profile_image
id
employee_salary
employee_age

```
2. Read json from a file and make a model
```jtms.py -f test.json 
ROOT
data
status
message

DATA
id
employee_salary
employee_age
employee_name
profile_image

```
## How to install
1. Needed python3.8+
2. Make git clone
3. Add the script to your shell config, like:
```
vim vim .zshrc
# Add path tou the script
export PATH=/path/to/script:$PATH
```